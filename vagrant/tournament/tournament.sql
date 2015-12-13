-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- psql
-- \l list of databases
-- \dt *.*
-- \c database_name
-- \d+ tablename
-- \i tournament.sql
-- ctrl + D to exit
-- python tournament_test.py


DROP TABLE tournaments;
DROP TABLE players;
DROP TABLE matches;
DROP TABLE standings;
DROP DATABASE tournament;

CREATE DATABASE tournament;

--switch to newly created tournament database
\c tournament;


CREATE TABLE tournaments(
	tournament_id serial PRIMARY KEY,
	tournament_name varchar(100),
	start_date timestamp without time zone default (now() at time zone 'est')
);

CREATE TABLE players(
	player_id serial PRIMARY KEY,
	player_name varchar(100)
);

CREATE TABLE tournament_players(
	player_id integer NOT NULL,
	tournament_id integer NOT NULL
);

CREATE TABLE matches(
	match_id serial PRIMARY KEY,
	tournament_id integer NOT NULL,
	start_date timestamp without time zone default (now() at time zone 'est')
);

CREATE TABLE standings(
	standing_id serial PRIMARY KEY,
	player_id integer NOT NULL,
	match_id integer NOT NULL,
	score int,
	start_date timestamp without time zone default (now() at time zone 'est')
);

--switch back to default database
\c vagrant;