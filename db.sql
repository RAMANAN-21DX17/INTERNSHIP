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
SELECT * FROM meetings ;
truncate table company;
drop table accounts;
insert into accounts values ( 1, "Admin" , "12345678" ,"Admin@gmail.com" , "Coimbatore" , "psg", "Admin");
insert into accounts values ( 2, "Emp1", "12345678","emp1@gmail.com","Coimbatore","psg","Employee");
create table company(
	name varchar(100) not null,
    location varchar(100) not null,
    no_of_rooms int not null,
    primary key (name)
)engine = InnoDB default charset = utf8;
insert into company values ("psg","Coimbatore",4);
select * from company ;
create table room(
	company varchar(100) not null,
    name varchar(100) ,
    time1 varchar(50) ,
    time2 varchar(50) ,
    time3 varchar(50) ,
    time4 varchar(50) ,
    time5 varchar(50) ,
    foreign key (company) references company(name)
)engine = InnoDB default charset = utf8;
insert into room values ("psg",null,null,null,null,null,null);
drop table room;
create table meetings(
	user varchar(50) not null,
    meeting1 varchar(50),
    meeting2 varchar(50),
    meeting3 varchar(50),
    meeting4 varchar(50),
    meeting5 varchar(50)
)engine = InnoDB default charset = utf8;
drop table meetings;
select * from meetings




    

    
	
	
