from . import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, engine, Categories, Items

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


try:
    print 'Start of Categories'
    try:

        newCat = Categories(name='Soccer')
        session.add(newCat)

        newCat = Categories(name='Basketball')
        session.add(newCat)

        newCat = Categories(name='Baseball')
        session.add(newCat)

        newCat = Categories(name='Frisbee')
        session.add(newCat)

        newCat = Categories(name='Snowboarding')
        session.add(newCat)

        newCat = Categories(name='Rock Climbing')
        session.add(newCat)

        newCat = Categories(name='Foosball')
        session.add(newCat)

        newCat = Categories(name='Skating')
        session.add(newCat)

        newCat = Categories(name='Hockey')
        session.add(newCat)
        session.commit()


        category = session.query(Categories.id).filter_by(name='Soccer').limit(1).one()
        category_id = category.id
        newItem = Items(title='Soccer Cleats',
            description='''Cleats or studs are protrusions on the sole of a shoe,
            or on an external attachment to a shoe, that provide additional traction on a soft or slippery surface.
            In American English the term cleats is used synecdochically to refer to shoes featuring such protrusions.
            This does not happen in British English; the term "studs" is never used to refer to the shoes,
            which would instead be known as "football boots", "rugby boots", and so on.''',
            category_id=category_id)
        session.add(newItem)
        #session.commit()

        category = session.query(Categories.id).filter_by(name='Soccer').limit(1).one()
        category_id = category.id
        newItem = Items(title='Jersey',
            description='''Mostly refered as Kit, the kit in association football,
            as in a number of other sports, kit refers to the standard equipment and attire worn by players.
            The terms "kit", "strip", and in North American English "uniform" are used interchangeably.''',
            category_id=category_id)
        session.add(newItem)
        #session.commit()

        category = session.query(Categories.id).filter_by(name='Baseball').limit(1).one()
        category_id = category.id
        newItem = Items(title='Bat',
            description='''Bat''',
            category_id=category_id)
        session.add(newItem)
        #session.commit()

        category = session.query(Categories.id).filter_by(name='Frisbee').limit(1).one()
        category_id = category.id
        newItem = Items(title='Frisbee',
            description='''Frisbee''',
            category_id=category_id)
        session.add(newItem)
        #session.commit()

        category = session.query(Categories.id).filter_by(name='Soccer').limit(1).one()
        category_id = category.id
        newItem = Items(title='Shinguards',
            description='''Shinguards''',
            category_id=category_id)
        session.add(newItem)
        #session.commit()

        category = session.query(Categories.id).filter_by(name='Soccer').limit(1).one()
        category_id = category.id
        newItem = Items(title='Two shinguards',
            description='''Two shinguards''',
            category_id=category_id)
        session.add(newItem)
        #session.commit()

        category = session.query(Categories.id).filter_by(name='Snowboarding').limit(1).one()
        category_id = category.id
        newItem = Items(title='Snowboard',
            description='''Snowboard''',
            category_id=category_id)
        session.add(newItem)
        #session.commit()

        category = session.query(Categories.id).filter_by(name='Snowboarding').limit(1).one()
        category_id = category.id
        newItem = Items(title='Goggles',
            description='''Goggles''',
            category_id=category_id)
        session.add(newItem)
        #session.commit()

        category = session.query(Categories.id).filter_by(name='Hockey').limit(1).one()
        category_id = category.id
        newItem = Items(title='Stick',
            description='''Stick''',
            category_id=category_id)
        session.add(newItem)
        session.commit()
    except:
        session.rollback()
        raise

except:
    session.rollback()
    raise
