import os
import sys

sys.path.append(os.getcwd())

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)


# class Review(Base):
#     pass

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)
    star_rating = Column(Integer())
    reviews = relationship('Review', backref=backref('restaurant'))

    def __repr__(self):
        return f'Restaurant: {self.name}'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    reviews = relationship('Review', backref=backref('customer'))

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
        return f'Review: (id={self.id},' +\
            f'star_rating={self.star_rating},' +\
            f'restaurant_id={self.restaurant_id})'

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    