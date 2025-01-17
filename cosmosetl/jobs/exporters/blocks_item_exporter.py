from blockchainetl_common.jobs.exporters.composite_item_exporter import CompositeItemExporter

BLOCK_FIELDS_TO_EXPORT = [
    'height',
    'hash',
    'last_block_hash',
    'data_hash',
    'validators_hash',
    'consensus_hash',
    'app_hash',
    'proposer_addr',
    'timestamp',
    'num_txs',
]

def blocks_item_exporter(blocks_output):
    return CompositeItemExporter(
        filename_mapping={
            'block': blocks_output
        },
        field_mapping={
            'block': BLOCK_FIELDS_TO_EXPORT
        }
    )
