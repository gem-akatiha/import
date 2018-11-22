drop database kridathon;
create database kridathon;
use kridathon;
ALTER DATABASE kridathon CHARACTER SET utf8 COLLATE utf8_unicode_ci;

/*1-user*/
create table user
(
id int unsigned not null auto_increment,
username varchar(25) unique not null,
password varchar(25) default '12345',
name varchar(50) default 'Sportee',
dob varchar(20),
weight float (7,3),
age int(3),
sport varchar(30),
phone bigint(13),/*It may cause problem later.Check the datatype again*/
email varchar(100),
city varchar(25),
image varchar(100),
account_number varchar(20),
ifsc_code varchar(11),
creation_timestamp datetime default CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);
ALTER TABLE user auto_increment 10000;

/*2-event*/
create table event
(
id int unsigned not null auto_increment,
event_name varchar(50),
event_game varchar(250),
event_logo varchar(30),
location varchar(100),
organiser_id int unsigned not null,
event_start datetime,
event_end datetime,
description varchar(1000),
creation_timestamp datetime default CURRENT_TIMESTAMP,
PRIMARY KEY (id),
FOREIGN KEY (organiser_id) REFERENCES user (id)
);


/*3-tournament*/
create table tournament
(
id int unsigned not null auto_increment,
tournament_name varchar(100),
game varchar(30),
tournament_mode varchar(10),
tournament_type varchar(30),
event_id int unsigned not null,
number_of_teams int(3),
number_of_round int(3),
number_of_matches int(3),
tournament_image varchar(100),
tournament_start datetime,
tournament_end datetime,
location varchar(100),
organiser_id int unsigned not null,
creation_timestamp datetime default CURRENT_TIMESTAMP,
PRIMARY KEY (id),
FOREIGN KEY (organiser_id) REFERENCES user (id),
FOREIGN KEY (event_id) REFERENCES event (id)
);

/*4-team*/
create table team
(
id int unsigned not null auto_increment,
team_name varchar(30),
team_logo varchar(100),
creation_timestamp datetime default CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);

/*5-team-info*/
create table team_information
(
id int unsigned not null auto_increment,
team_id int unsigned not null,
event_id int unsigned not null,
tournament_id int unsigned not null,
player_id int unsigned not null,
creation_timestamp datetime default CURRENT_TIMESTAMP,
PRIMARY KEY(id),
FOREIGN KEY (team_id) REFERENCES team (id),
FOREIGN KEY (tournament_id) REFERENCES tournament (id),
FOREIGN KEY (player_id) REFERENCES user (id),
FOREIGN KEY (event_id) REFERENCES event (id)
);

/*6-summary*/
create table result
(
id int unsigned not null auto_increment,
event_id int unsigned not null,
tournament_id int unsigned not null,
winner_team_id int unsigned not null,
runner_up_team_id int unsigned not null,
creation_timestamp datetime default CURRENT_TIMESTAMP,
PRIMARY KEY(id),
FOREIGN KEY (event_id) REFERENCES event (id),
FOREIGN KEY (tournament_id) REFERENCES tournament (id),
FOREIGN KEY (winner_team_id) REFERENCES team (id),
FOREIGN KEY (runner_up_team_id) REFERENCES team (id)
);
show tables;