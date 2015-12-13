#
# Database access functions for the web forum.
#

import time
import psycopg2

## Database connection
DB = []
try:
    conn = psycopg2.connect('dbname=forum')
    cur = conn.cursor()
except:
    print "Database connection error"

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''

    posts = []

    try:
        print "GetAllPosts"

        query = "SELECT time, content from posts;"
        print "query: %s" % query
        cur.execute(query)
        DB = cur.fetchall()

        posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
        posts.sort(key=lambda row: row['time'], reverse=True)

    except:
        print "Error"

    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    t = time.strftime('%c', time.localtime())
    try:
        print "Add Post: %s" % content
        #query = "INSERT INTO posts(time, content) values('%s', '%s');", (t, (content,))
        #cur.execute(query)
        cur.execute("INSERT INTO posts(content) values (%s);", (content,))
        conn.commit()
    except:
        print "I can't Add Post"

    #DB.append((t, content))

