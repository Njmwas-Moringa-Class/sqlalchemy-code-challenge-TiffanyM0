import os
import sys

import sqlite3
CONN = sqlite3.connect('restaurants.db')
CURSOR = CONN.cursor()

sys.path.append(os.getcwd())

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy import ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()
engine = create_engine('sqlite:///lib/db/restaurants.db', echo=True)


# class Review(Base):
#     pass

restaurant_user=Table(
    'restaurant_users',
    Base.metadata,
    Column('restaurant_id',ForeignKey('restaurants.id'),primary_key=True),
    Column('customer_id',ForeignKey('customers.id'),primary_key=True),
     extend_existing=True,
    
)

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)
    star_rating = Column(Integer())
    reviews = relationship('Review', backref=backref('restaurant'))
    customers = relationship('Customer', secondary=restaurant_user, back_populates='restaurants')

    def __repr__(self):
        return f'Restaurant: {self.name}'


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    reviews = relationship('Review', backref=backref('customer'))
    restaurants = relationship('Restaurant', secondary=restaurant_user, back_populates='customers')

    def __repr__(self):
        return f'Customer: {self.name}'


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    comment = Column(String())
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    def __repr__(self):
        return f'star_rating={self.star_rating},'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    