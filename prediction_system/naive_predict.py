import numpy as np


def naive_predict_user(rating, users_count, products_count, distance_matrix):
    top_similar_ratings = np.zeros((users_count, rating, products_count))

    for i in range(users_count):
        top_sim_users = distance_matrix[i].argsort()[1:rating + 1]

        top_similar_ratings[i] = distance_matrix[top_sim_users]

    pred = np.zeros((users_count, products_count))
    for i in range(users_count):
        pred[i] = top_similar_ratings[i].sum(axis=0) / rating

    return pred


def naive_predict_product(rating, users_count, products_count, distance_matrix):
    top_similar_ratings = np.zeros((products_count, rating, users_count))

    for i in range(products_count):
        top_sim_movies = distance_matrix[i].argsort()[1:rating + 1]
        top_similar_ratings[i] = distance_matrix.T[top_sim_movies]

    pred = np.zeros((products_count, users_count))
    for i in range(products_count):
        pred[i] = top_similar_ratings[i].sum(axis=0) / rating

    return pred.T