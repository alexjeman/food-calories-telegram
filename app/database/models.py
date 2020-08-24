from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # User id in telegram
    telegram = Column(Integer, unique=True)

    # Food-calories username
    username = Column(String, unique=True)

    # Food-calories api key
    api_key = Column(String, unique=True)
