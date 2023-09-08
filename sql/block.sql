create table blocks
(
  height bigint,
  hash varchar(64),
  last_block_hash varchar(64),
  data_hash varchar(64),
  validators_hash varchar(64),
  consensus_hash varchar(64),
  app_hash varchar(64),
  proposer_addr varchar(40),
  timestamp timestamp,
  num_txs integer
);

alter table blocks add constraint blocks_pk primary key (hash);

create index blocks_timestamp_index on blocks (timestamp desc);

create unique index blocks_number_uindex on blocks (height desc);

-- https://github.com/blockchain-etl/ethereum-etl-postgres
