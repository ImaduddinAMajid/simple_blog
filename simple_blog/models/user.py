import datetime
from simple_blog.models.meta import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy import DateTime

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(Unicode(255), unique=True, nullable=False)
	password = Column(Unicode(255), nullable=(False))
	last_logged = Column(DateTime, default=datetime.datetime.utcnow)
