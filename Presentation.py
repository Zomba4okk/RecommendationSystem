from app.base import Session
from app.product.models import Product
from app.user.models import User
from prediction_system.naive_predict import *
from prediction_system.k_fract_predict import *
from prediction_system.k_fract_mean_predict import *
from prediction_system.utils import *


if __name__ == '__main__':
    session = Session()

    users_count = User.count()
    products_count = Product.count()

    ratings = prepare_ratings(users_count, products_count, User.get_ratings())
    test, train = split_for_training(ratings)

    # Naive, user based
    dist = get_distances(train)
    naive_user_pred = naive_predict_user(len(train), products_count, dist, train)
    naive_user_rmse = rmse(naive_user_pred, test)
    print('Naive, user based: ' + str(naive_user_rmse))

    # Naive, product based
    dist = get_distances(train.T)
    naive_item_pred = naive_predict_product(len(train), products_count, dist, train)
    naive_item_rmse = rmse(naive_item_pred, test)
    print('Naive, product based: ' + str(naive_item_rmse))

    print('\n')

    # Average ratings of similar users, user based
    dist = get_distances(train)
    k_fract_user_pred = k_fract_predict_user(len(train), products_count, dist, train)
    k_fract_user_rmse = rmse(k_fract_user_pred, test)
    print('Average ratings of similar users, user based: ' + str(k_fract_user_rmse))

    # Average ratings of similar users, product based
    dist = get_distances(train.T)
    k_fract_item_pred = k_fract_predict_item(len(train), products_count, dist, train)
    k_fract_item_rmse = rmse(k_fract_item_pred, test)
    print('Average ratings of similar users, product based: ' + str(k_fract_item_rmse))

    print('\n')

    # Average user ratings and similarity matrix, user based
    dist = get_distances(train)
    k_fract_mean_user_pred = k_fract_mean_predict_user(len(train), products_count, dist, train)
    k_fract_mean_user_rmse = rmse(k_fract_mean_user_pred, test)
    print('Average user ratings and similarity matrix, user based: ' + str(k_fract_mean_user_rmse))

    # Average user ratings and similarity matrix, product based
    dist = get_distances(train.T)
    k_fract_mean_item_pred = k_fract_mean_predict_item(len(train), products_count, dist, train)
    k_fract_mean_item_rmse = rmse(k_fract_mean_item_pred, test)
    print('Average user ratings and similarity matrix, product based: ' + str(k_fract_mean_item_rmse))

