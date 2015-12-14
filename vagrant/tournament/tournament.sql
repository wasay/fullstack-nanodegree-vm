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

\c tournament

DROP VIEW standings_view;

DROP TABLE tournaments;
DROP TABLE players;
DROP TABLE matches;

\c vagrant;
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
	player_id_winner integer NOT NULL,
	player_id_loser integer NOT NULL,
	start_date timestamp without time zone default (now() at time zone 'est')
);

CREATE VIEW standings_view  AS
	SELECT
		players.player_id as id,
		players.player_name as name,
		coalesce((
			select count(matches.player_id_winner)
			from matches
			where
				matches.player_id_winner = tournament_players.player_id
			group by matches.player_id_winner
		),0) as wins,
		coalesce((
			select count(matches.match_id)
			from matches
			where
				matches.tournament_id = tournament_players.tournament_id AND
				(
					matches.player_id_winner = tournament_players.player_id OR
					matches.player_id_loser = tournament_players.player_id
				)
		),0) as matches,
		coalesce((
			select matches.match_id
			from matches
			where
				matches.tournament_id = tournament_players.tournament_id AND
				(
					matches.player_id_winner = tournament_players.player_id OR
					matches.player_id_loser = tournament_players.player_id
				)
			limit 1
		),0) as match_id,
		tournament_players.tournament_id
	FROM
		players
	LEFT JOIN
		tournament_players
	ON
		tournament_players.player_id = players.player_id
;

--test that the view select is working
SELECT * FROM standings_view;

--switch back to default database
\c vagrant;