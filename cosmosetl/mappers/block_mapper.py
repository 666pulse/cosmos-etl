from cosmosetl.domain.block import CosmBlock
from cosmosetl.utils import str_to_dec

class CosmBlockMapper:

    def json_dict_to_block(self, json_dict):
        block = CosmBlock()
        block.height = str_to_dec(json_dict['block']['header'].get('height'))
        block.hash = json_dict['block_id'].get('hash')
        block.last_block_hash = json_dict['block']['header'].get('last_block_id', {}).get('hash')
        block.data_hash = json_dict['block']['header'].get('data_hash')
        block.validators_hash = json_dict['block']['validators_hash']
        block.consensus_hash = json_dict['block']['consensus_hash']
        block.app_hash = json_dict['block']['app_hash']
        block.proposer_addr = json_dict['block']['header'].get('proposer_address')
        block.timestamp = json_dict['block']['header'].get('time')
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
