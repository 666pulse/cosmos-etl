from cosmosetl.domain.block import CosmBlock
from cosmosetl.utils import str_to_dec

class CosmBlockMapper:

    def json_dict_to_block(self, json_dict):
        block = CosmBlock()
        header = json_dict['block']['header']

        block.height = str_to_dec(header.get('height'))
        block.hash = json_dict['block_id'].get('hash')
        block.last_block_hash = header.get('last_block_id', {}).get('hash')
        block.data_hash = header.get('data_hash')
        block.validators_hash = header.get('validators_hash')
        block.consensus_hash = header.get('consensus_hash')
        block.app_hash = header.get('app_hash')
        block.proposer_addr = header.get('proposer_address')
        block.timestamp = header.get('time')
        block.num_txs = len(json_dict['block']['data'].get('txs', []))
        return block

    def block_to_dict(self, block):
        return {
            'type': 'block',
            'height': block.height,
            'hash': block.hash,
            'last_block_hash': block.last_block_hash,
            'data_hash': block.data_hash,
            'validators_hash': block.validators_hash,
            'consensus_hash': block.consensus_hash,
            'app_hash' : block.app_hash,
            'proposer_addr': block.proposer_addr,
            'timestamp': block.timestamp,
            'num_txs': block.num_txs,
        }
