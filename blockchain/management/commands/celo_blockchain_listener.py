from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path

from blockchain.listener import BlockchainListener

BASE_DIR = settings.BASE_DIR

class Command(BaseCommand):
    help = "CELO BLOCKCHAIN LISTENER"

    def handle(self, *args, **options):

        listener = BlockchainListener("wss://alfajores-forno.celo-testnet.org/ws/",
                                      "0x49064284379aCAc2b27Cf2afd9CA2f2c18278463",
                                      BASE_DIR / Path('blockchain/abi.json'))

        listener.loop()
