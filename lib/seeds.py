#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Review, Customer

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Review).delete()
    session.query(Customer).delete()


    fake = Faker()

    # name = ['KFC', 'Burger King', 'Art-Caffe', 'Bwibo']
    
    restaurants = []
    for i in range(50):
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(5, 600),
            star_rating=random.randint(0, 5)
        )

        # add and commit individually to get IDs back
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)

    customers = []
    for i in range(50):
                 
        customer = Customer(
            first_name=fake.unique.first_name(),
            last_name=fake.unique.last_name(),
        )
        session.add(customer)
        session.commit()

        customers.append(customer)


    reviews = []
    for restaurant in restaurants:          
            review = Review(
                star_rating=random.randint(0, 10),
                comment=fake.sentence(),
                # restaurant_id=restaurants.id,
                # customer_id=customers.id,
            )
            session.add(review)
            session.commit()

            reviews.append(review)


    session.bulk_save_objects(reviews)
    session.commit()
    session.close()
