#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.models import Customer, Restaurant, Review
import ipdb;


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///db/restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()
