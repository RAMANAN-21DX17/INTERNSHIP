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
	
create table bookings(
company varchar(50) not null ,
room varchar(100) not null ,
timing varchar(50) not null ,
available varchar(20) not null ,
primary key (id)
)
SELECT * FROM bookings;
insert into bookings values('p','q','9-10','yes');
insert into bookings values('p','q','10-11','yes');
insert into bookings values('p','q','11-12','N0');
insert into bookings values('p','q','12-1','yes');
insert into bookings values('p','q','1-2','No');
insert into bookings values('p','q','2-3','yes');
insert into bookings values('p','q','3-4','yes');    
	
