create table transactions
(
  hash varchar(64),
  height bigint,
  tx_index integer,
  code text,
  gas_used  bigint,
  gas_wanted bigint,
  root_hash varchar(64),
  num_events integer
);


alter table transactions add constraint transactions_pk primary key (tx_hash);

create unique index transactions_number_uindex on transactions (height desc);
