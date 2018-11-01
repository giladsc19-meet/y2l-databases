from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(price, metirial, size, company, color):
		ball = Basketball(price = price, 
			metirial = metirial, 
			size = size, 
			company = company, 
			color = color)
		session.add(ball)
		session.commit()

def update_product():
  pass

def delete_product(id):
  session.query(Basketball).filter_by(id = id).delete()
  session.commit()

def get_product(id):
  pass

create_product(15,"metal", 7, "nike", "orange")
delete_product(1)