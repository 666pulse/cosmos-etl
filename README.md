# Cosmos ETL
Cosmos ETL lets you convert cosmos blockchain data into convenient formats like CSV and JSON. This project was inspired by [ethereum etl](https://github.com/blockchain-etl/ethereum-etl).

## Quickstart

Install cosmos-etl

```bash
pip install cosmos-etl
```

## Export blocks

```
$rpc
```

```bash
rpc=https://rpc.cosmos.directory/stargaze

cosmosetl export_blocks -s 5131001 -e 5141001 -p $rpc -o blocks.csv
```

### Export transactions and events

```bash
cosmosetl export_transactions_and_events -s 5131001 -e 5141001 -p $rpc  -to transactions.csv -eo events.csv
```

### Get block range for date

```bash
cosmosetl get_block_range_for_date -p $rpc -d 2022-05-12
```

### Get block range for timestamps

```bash
cosmosetl get_block_range_for_timestamps -p $rpc -s 1963733 -e 5141001
```
