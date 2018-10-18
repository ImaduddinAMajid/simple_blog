import datetime
from simple_blog.models.meta import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy import DateTime


class BlogRecord(Base):
	__tablename__ = 'entries'
	id = Column(Integer, primary_key=True)
	title = Column(Unicode(255), unique=True, nullable=False)
	body = Column(UnicodeText, default=u'')
	created = Column(DateTime, default=datetime.datetime.utcnow)	
