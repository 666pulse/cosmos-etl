create table events
(
  event_type varchar(50),
  height bigint,
  tx_hash varchar(64),
  attributes text
);

-- attributes jsonb

alter table events add constraint events_pk primary key (tx_hash);
