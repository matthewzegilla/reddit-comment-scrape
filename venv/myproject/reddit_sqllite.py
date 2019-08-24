from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

BASE = declarative_base()
SQL_LITE_DB_NAME = 'Reddit' + '.db'
SQL_LITE_ENGINE_URL = 'sqlite:///' + SQL_LITE_DB_NAME


def get_engine():
    engine_url = SQL_LITE_ENGINE_URL
    engine = create_engine(engine_url)
    return engine


def get_session():
    engine = get_engine()
    BASE.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()


class User(BASE):
    __tablename__ = "reddit_comments"
    id = Column('id', Integer, primary_key=True)
    reddit_id = Column('reddit_id', String)
    comment_context = Column('comment_context', String)


def add_comment(discord_id_in, comment_in):
    session = get_session()
    reddit_user = User()
    reddit_user.reddit_id = discord_id_in
    reddit_user.comment_context = comment_in
    session.add(reddit_user)
    session.commit()
    session.close()