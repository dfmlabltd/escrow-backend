from pathlib import Path
from typing import Dict
from web3 import Web3
import asyncio
import json
from .enums import EventType
from . import tasks


class BlockchainListener:

    provider: Web3.WebsocketProvider

    web3: Web3

    contract = None

    def __init__(self, rpc_url: str, contract_address: str,  abi_file_path: Path):

        self.provider = Web3.WebsocketProvider(rpc_url)

        self.web3 = Web3(self.provider)

        self.contract = self.get_contract(
            contract_address, self.load_abi(abi_file_path))

    def load_abi(self, abi_file_path: Path) -> Dict:

        with open(abi_file_path, 'r') as abi:

            contract_abi = json.loads(abi.read())

        return contract_abi

    def get_contract(self, contract_address: str, contract_abi: str):

        return self.web3.eth.contract(address=contract_address, abi=contract_abi)

    # deposit event
    def handle_deposit_event(self, event):
        transactionHash = event.get('transactionHash').hex()
        blockHash = event.get('blockHash').hex()
        args = event.get('args')
        identifier = args.get('identifier')
        contract_address = args.get('contract_address')
        trustee = args.get('trustee')
        amount = args.get('amount')
        tasks.deposit.delay(identifier, contract_address, trustee, amount, transactionHash, blockHash)

    # payment request event
    def handle_withdrawal_event(self, event):
        transactionHash = event.get('transactionHash').hex()
        blockHash = event.get('blockHash').hex()
        args = event.get('args')
        identifier = args.get('identifier')
        contract_address = args.get('contract_address')
        amount = args.get('amount')
        tasks.withdrawal.delay(
            identifier, contract_address, transactionHash, blockHash)

    # payment request event
    def handle_reject_withdrawal_event(self, event):
        args = event.get('args')
        identifier = args.get('identifier')
        contract_address = args.get('contract_address')
        tasks.reject_withdrawal.delay(identifier, contract_address)
        
    # payment request event
    def handle_withdrawal_approval_event(self, event):
        args = event.get('args')
        identifier = args.get('identifier')
        contract_address = args.get('contract_address')
        tasks.approve_withdrawal.delay(identifier, contract_address)

    # payment request event
    def handle_request_for_withdrawal_event(self, event):
        args = event.get('args')
        identifier = args.get('identifier')
        contract_address = args.get('contract_address')
        amount = args.get('amount')
        description = args.get('description')
        trustee = args.get('trustee')
        tasks.request_for_withdrawal.delay(identifier, contract_address, trustee, amount, description)

    def event_reducer(self, event, event_type):

        if event_type == EventType.DEPOSIT:

            self.handle_deposit_event(event)
            
        elif event_type == EventType.REQUEST:
            
            self.handle_reject_withdrawal_event(event)
            
        elif event_type == EventType.REJECTED:
            
            self.handle_reject_withdrawal_event(event)
            
        elif event_type == EventType.WITHDRAW:
            
            self.handle_withdrawal_event(event)

        elif event_type == EventType.APPROVED:
            
            self.handle_withdrawal_approval_event(event)

    async def loop_event(self, event_filter, poll_interval, event_type: EventType):
        while True:
            for event in event_filter.get_new_entries():
                self.event_reducer(event, event_type)
            await asyncio.sleep(poll_interval)

    @property
    def events(self):

        return self.contract.events

    def loop(self):

        events = self.events

        deposit_event = events.OwnerSet.createFilter(fromBlock='latest')
        request_event = events.OwnerX.createFilter(fromBlock='latest')
        reject_event = events.OwnerX.createFilter(fromBlock='latest')
        withdraw_event = events.OwnerX.createFilter(fromBlock='latest')
        approve_event = events.OwnerX.createFilter(fromBlock='latest')

        loop = asyncio.get_event_loop()

        try:
            loop.run_until_complete(
                asyncio.gather(
                    self.loop_event(deposit_event, 2, EventType.DEPOSIT),
                    self.loop_event(request_event, 2, EventType.REQUEST),
                    self.loop_event(reject_event, 2, EventType.REJECTED),
                    self.loop_event(withdraw_event, 2, EventType.WITHDRAW),
                    self.loop_event(approve_event, 2, EventType.APPROVED),
                ))
        finally:
            loop.close()
