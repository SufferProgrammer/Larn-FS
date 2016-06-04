from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

eng = create_engine('sqlite:///management/database/database.db', echo=True)
base = declarative_base()

class User(base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    passwd = Column(String)

    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd



base.metadata.create_all(eng)
