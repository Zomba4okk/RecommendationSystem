from random import randint
import os
import sys

BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
sys.path.append(BASE_PATH)

from app.base import Session
from app.product.models import Product, Rating
from app.user.models import User


if __name__ == '__main__':
    session = Session()

    users = []
    products = []
    ratings = []

    for i in range(2000):
        users.append(User(
            username='user_' + str(i),
            first_name='fn_' + str(i),
            last_name='ln_' + str(i),
        ))

    for i in range(20000):
        products.append(Product(
            name='product_' + str(i),
            price=randint(1, 1000),
            param_1=randint(1, 10),
            param_2=randint(1, 10),
            param_3=bool(randint(0, 1)),
        ))

    for i in range(20000):
        ratings.append(Rating(
            rate=randint(1, 10),
            user_id=randint(1, 1000),
            product_id=randint(1, 20000)
        ))

    session.add_all(users)
    session.add_all(products)
    session.commit()

    session.add_all(ratings)
