drop database if exists uzdevsbot;
create database uzdevsbot;

\c uzdevsbot;

create extension citext;
create extension "uuid-ossp";
create extension pgcrypto;
create extension tcn;
create extension plv8;

create table if not exists users (
  id bigint primary key,
  first_name citext not null,
  last_name citext,
  username citext unique,
  is_admin boolean default false,
  is_active boolean default true,
  joined timestamptz default timezone('Asia/Tashkent'::text, now())
);
