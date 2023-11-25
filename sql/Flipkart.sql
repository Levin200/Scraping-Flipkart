create database Flipkart;

use Flipkart;

create table Category(
category_id int primary key auto_increment,
category_name varchar(100)
);

create table Products (
product_id varchar(100) primary key,
product_name varchar(200) ,category
url varchar(1000),
feature varchar(100),
category_id int,
foreign key (category_id) references Category(category_id)
);

alter table Products change `url` `URL` varchar(1000);

create table Image_url (
product_id varchar(100) primary key,
img_url varchar(1000),
foreign key (product_id) references Products(product_id)
);

create table Ratings (
product_id varchar(100),
rating_id int primary key auto_increment,
rating float,
count_of_people int, 
created_at datetime, 
foreign key (product_id) references Products(product_id)
);

create table Stars (
rating_id int,
star_id int primary key auto_increment,
star_5 integer,
star_4 integer,
star_3 integer,
star_2 integer,
star_1 integer,
foreign key (rating_id) references Ratings(rating_id)
);

create table Review (
product_id varchar(100),
review_id int primary key auto_increment,
review text,
created_at datetime,
foreign key (product_id) references Products(product_id)
);

create table Price(
product_id varchar(100),
price_id int primary key auto_increment,
price int,
actual_price int,
created_at datetime,
foreign key (product_id) references Products(product_id)
);

create table Ranking(
ranking_id int primary key auto_increment,
product_id varchar(100),
ranking int,
created_at datetime,
foreign key (product_id) references Products(product_id)
);

Alter table Ratings 
Drop column created_at;

insert into Category (category_id,category_name) 
values(1, "headphones");