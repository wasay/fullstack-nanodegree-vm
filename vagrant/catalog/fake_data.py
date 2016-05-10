from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app

from models import Categories, Base, Items, User

engine = create_engine('sqlite:///itemcatalog.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Category Soccer
category1 = Categories(user_id=1, name="Soccer")

session.add(category1)
session.commit()

item1 = Items(user_id=1, title="Soccer Cleats",
              description="Cleats or studs are protrusions on the sole of a shoe, "\
              "or on an external attachment to a shoe, that provide additional traction on a soft or slippery surface. "\
              "In American English the term cleats is used synecdochically to refer to shoes featuring such protrusions. "\
              "This does not happen in British English; the term 'studs' is never used to refer to the shoes, "\
              "which would instead be known as 'football boots', 'rugby boots', and so on.",
              category_id=1, categories=category1)

session.add(item1)
session.commit()


item2 = Items(user_id=1, title="Jersey",
              description="Mostly refered as Kit, the kit in association football, "\
              "as in a number of other sports, kit refers to the standard equipment and attire worn by players. "\
              "The terms 'kit', 'strip', and in North American English 'uniform' are used interchangeably.",
              category_id=1, categories=category1)

session.add(item2)
session.commit()


print "added menu items!"
