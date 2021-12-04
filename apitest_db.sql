CREATE DATABASE apidb;
CREATE USER apitest WITH PASSWORD 'apitest';
GRANT ALL PRIVILEGES ON DATABASE "apidb" to apitest;
\c apidb
set role apitest;
create table birthday
(name varchar(50), 
date1 date);
insert into birthday (name, date1) values ('John', '1975-04-13');
insert into birthday (name, date1) values ('Jane', '1984-04-18');
insert into birthday (name, date1) values ('Robert', '2008-11-28');
commit;

