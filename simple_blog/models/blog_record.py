import datetime
from simple_blog.models.meta import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy import DateTime
from webhelpers2.text import urlify
from webhelpers2.date import distance_of_time_in_words


class BlogRecord(Base):
	__tablename__ = 'entries'
	id = Column(Integer, primary_key=True)
	title = Column(Unicode(255), unique=True, nullable=False)
	body = Column(UnicodeText, default=u'')
	created = Column(DateTime, default=datetime.datetime.utcnow)	

	@property
	def slug(self):
		return urlify(self.title)

	@property
	def created_in_words(self):
		return distance_of_time_in_words(self.created, datetime.datetime.utcnow())

