create database makemymeeting default character set utf8 collate utf8_general_ci;
use makemymeeting;
create table accounts(
id int(11) not null auto_increment,
username varchar(50) not null,
password varchar(255) not null,
email varchar(255) not null,
location varchar(100) not null,
company varchar(100) not null ,
positon varchar(50) not null,
primary key (id)
) engine = InnoDB auto_increment = 2 default charset = utf8;
SELECT * FROM ACCOUNTS;
drop table accounts;
insert into accounts values ( 3, "employee" , "12345678" ,"shutlight7@gmail.com" , "coimbatore" , "psg", "Employee");
	
	
