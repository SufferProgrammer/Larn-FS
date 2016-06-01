import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cDbTable import *


eng = create_engine('sqlite:///database/database.db', echo = True)

sess = sessionmaker(bind=eng)
insert = sess()

user = User("admin", "admin")
insert.add(user)

user = User("piji", "piji")
insert.add(user)

insert.commit()
insert.commit()
