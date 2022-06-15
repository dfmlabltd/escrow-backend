from enum import Enum
from pathlib import Path
from typing import Dict
from web3 import Web3
import asyncio
import json


class EventType(Enum):

    DEPOSIT = 0

    REQUEST = 1

    REJECTED = 2

    VOTE = 3

    APPROVED = 4

    WITHDRAW = 5


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
        print(transactionHash, args, blockHash)

    # payment request event
    def handle_request_event(self, event):
        transactionHash = event.get('transactionHash').hex()
        blockHash = event.get('blockHash').hex()
        args = event.get('args')
        print(transactionHash, args, blockHash)

    # payment request event
    def handle_request_rejected_event(self, event):
        transactionHash = event.get('transactionHash').hex()
        blockHash = event.get('blockHash').hex()
        args = event.get('args')
        print(transactionHash, args, blockHash)

    # payment request event
    def handle_vote_event(self, event):
        transactionHash = event.get('transactionHash').hex()
        blockHash = event.get('blockHash').hex()
        args = event.get('args')
        print(transactionHash, args, blockHash)

    # payment request event
    def handle_approval_event(self, event):
        transactionHash = event.get('transactionHash').hex()
        blockHash = event.get('blockHash').hex()
        args = event.get('args')
        print(transactionHash, args, blockHash)
    
    # payment request event
    def handle_withdrawal_event(self, event):
        transactionHash = event.get('transactionHash').hex()
        blockHash = event.get('blockHash').hex()
        args = event.get('args')
        print(transactionHash, args, blockHash)

    def event_reducer(self, event, event_type):

        if event_type == EventType.DEPOSIT:

            self.handle_deposit_event(event)

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

        loop = asyncio.get_event_loop()

        try:
            loop.run_until_complete(
                asyncio.gather(
                    self.loop_event(deposit_event, 2, EventType.DEPOSIT),
                    self.loop_event(request_event, 2, EventType.REQUEST),
                ))
        finally:
            loop.close()


listener = BlockchainListener("wss://alfajores-forno.celo-testnet.org/ws/",
                              "0x964bEd47B63A03c613019d7aFE935fFA80bde7F4",
                              Path("./abi.json")
                              )


listener.loop()
