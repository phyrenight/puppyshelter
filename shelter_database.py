import sys
from datetime import datetime, date, timedelta
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__= 'Shelter'
    name = Column(String(80), nullable = False)
    address = Column(String(80))
    city = Column(String(20))
    state = Column(String(20))
    zipcode = Column(Integer(5))
    website = Column(String(80))
    id = Column(Integer, primary_key = True)
    maximum_capacity = Column(Integer)
    current_capacity = Column(Integer)
	
class Puppy(Base):
    __tablename__ = 'Puppy'
    name = Column(String(80), nullable = False)
    gender = Column(String)
    dateOfBirth = Column(Date,nullable = False, primary_key = True)
    gender = Column(String(7))
    weight = Column(Integer(3), primary_key = True)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('Shelter.id'))
    shelter = relationship(Shelter)
	
engine = create_engine('sqlite:///shelterspuppy.db')

Base.metadata.create_all(engine)	
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

for name, in session.query(Puppy.name).order_by(Puppy.name):
    print name

for name, weight in session.query(Puppy.name, Puppy.weight).order_by(Puppy.name,Puppy.weight):
    print name, weight
	
for Puppy.name, Shelter.name, in session.query(Puppy.name, Shelter.name).order_by(Shelter.name):
    print Puppy.name, Shelter.name

today = datetime.today()
six_month = (today - timedelta(365/2))  
for  dateOfBirth, in session.query(Puppy.dateOfBirth).filter(Puppy.dateOfBirth > six_month).order_by(Puppy.dateOfBirth):
    print  dateOfBirth