create database makemymeeting default character set utf8 collate utf8_general_ci;
use makemymeeting;
create table accounts(
id int(11) not null auto_increment,
username varchar(50) not null,
password varchar(255) not null,
location varchar(100) not null,
company varchar(100) not null,
primary key (id)
) engine = InnoDB auto_increment = 2 default charset = utf8;
SELECT * FROM ACCOUNTS
insert into accounts values(