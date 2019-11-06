create database register;
use register;

create table users(id serial primary key,name varchar(50),username varchar(50), password varchar(300));
describe users;

insert into users(id,username,password)values('1','nidhi','pass');
insert into users(id,username,password)values('2','nidh','pass1');
insert into users(id,username,password)values('3','nid','pass2');
insert into users(id,username,password)values('4','ni','pass3');
insert into users(id,username,password)values('5','n','pass4');
select * from users;