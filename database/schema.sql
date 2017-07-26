create extension if not exists citext;
create extension if not exists "uuid-ossp";
create extension if not exists pgcrypto;
create extension if not exists plv8;

create table if not exists users (
  id bigint primary key,
  first_name citext not null,
  last_name citext,
  username citext unique,
  is_admin boolean default false,
  is_active boolean default true,
  joined timestamptz default timezone('Asia/Tashkent'::text, now())
);


create table if not exists history (
  id bigint primary key,
  sender jsonb,
  timestamp timestamptz default timezone('Asia/Tashkent'::text, now()),
  text citext
);
