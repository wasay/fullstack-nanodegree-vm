#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

""" Default tournament id assigned"""
tournament_id = 1


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    global conn
    global dbcur

    try:
        conn_string = "dbname='tournament' user='vagrant' password='vagrant'"
        conn = psycopg2.connect(conn_string)
        dbcur = conn.cursor()

    except ValueError, Argument:
        print "I am unable to connect to the database.", Argument

    return conn


def createTournament(name):
    """Adds a new tournament to the tournament database.

    The database assigns a unique serial id number for the tournament."""
    global tournament_id

    try:
        dbcur.execute("""SELECT tournament_id FROM tournaments""")

        query = """INSERT INTO tournaments(tournament_name) VALUES('%s');"""

        dbcur.execute(query % (name))
        conn.commit()
    except ValueError, Argument:
        print "Database relation issue.", Argument

    """ Retrieve generated ID (just one of the possible options)"""
    dbcur.execute("SELECT LASTVAL()")
    tournament_id = dbcur.fetchone()
    '''print "Tournament ID: %s" % tournament_id'''


def deleteMatches():
    """Remove all the match records from the database."""
    dbcur.execute("DELETE FROM matches;")
    conn.commit()


def deletePlayers():
    """Remove all the player records from the database."""
    dbcur.execute("DELETE FROM players;")
    conn.commit()


def countPlayers():
    """Returns the number of players currently registered."""
    global tournament_id

    query = """
    SELECT *
    FROM players
    LEFT JOIN tournament_players
    ON tournament_players.player_id = players.player_id
    WHERE tournament_players.tournament_id = %s; """
    dbcur.execute(query % (tournament_id))
    result = len(dbcur.fetchall())
    return result


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
        name: the player's full name (need not be unique).
    """
    global tournament_id

    query = """INSERT INTO players(player_name) VALUES($$%s$$);"""

    dbcur.execute(query % (name))
    conn.commit()

    """ Retrieve generated ID (just one of the possible options)"""
    dbcur.execute("SELECT LASTVAL()")
    player_id = dbcur.fetchone()

    """Convert tuple value to integer"""
    '''print """Tournament ID: %s""" % (tournament_id)'''
    tournament_id = str(tournament_id)
    tournament_id = filter(str.isdigit, tournament_id)
    '''print """Tournament ID: %s""" % (tournament_id)'''

    """Convert tuple value to integer"""
    '''print """Player ID: %s""" % (player_id)'''
    player_id = str(player_id)
    player_id = filter(str.isdigit, player_id)
    '''print """Player ID: %s""" % (player_id)'''

    query = """INSERT INTO tournament_players(player_id, tournament_id)
    VALUES(%s, %s);""" % (player_id, tournament_id)
    '''print query'''

    dbcur.execute(query)
    conn.commit()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    global tournament_id

    query = """
        SELECT
            id,
            name,
            wins,
            matches
        FROM
            standings_view
        WHERE
            tournament_id = %s;
    """ % (tournament_id)

    dbcur.execute(query)
    result = dbcur.fetchall()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    global tournament_id

    query = """INSERT INTO matches(tournament_id, player_id_winner, player_id_loser)
    VALUES(%s, %s, %s);""" % (tournament_id, winner, loser)

    dbcur.execute(query)
    conn.commit()

    conn.commit()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
        A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    global tournament_id

    query = """
    SELECT
        id, name,
        match_id, wins
    FROM standings_view
    WHERE standings_view.tournament_id = %s
    ORDER BY wins DESC """ % (tournament_id)

    dbcur.execute(query)
    standings = dbcur.fetchall()

    row = 0
    counter = 0

    result = [1, 3]

    for (i, n, m, s) in standings:

        if counter % 2 == 0:
            item = []
        else:
            item = result[row]

        item.append(i)
        item.append(n)

        result[row] = item

        counter += 1

        if counter % 2 == 0:
            row += 1

    return result


try:
    connect()

    """ Call to createTournament() is optional """
    createTournament('Tournament')

except ValueError, Argument:
        print "Initialization issue.", Argument
