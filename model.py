from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Basketball(Base):
	__tablename__ = "Basketball"
	id = Column(Integer, primary_key=True)
	price = Column(Integer)
	metirial = Column(String)
	size = Column(Integer)
	company = Column(String)
	color = Column(String)
