import numpy as np


def naive_predict_user(users_count, products_count, distance_matrix, train_data_matrix, top=10):
    top_similar_ratings = np.zeros((users_count, top, products_count))

    for i in range(users_count):
        top_sim_users = distance_matrix[i].argsort()[1:top + 1]

        top_similar_ratings[i] = train_data_matrix[top_sim_users]

    pred = np.zeros((users_count, products_count))
    for i in range(users_count):
        pred[i] = top_similar_ratings[i].sum(axis=0) / top

    return pred


def naive_predict_product(users_count, products_count, distance_matrix, train_data_matrix, top=10):
    top_similar_ratings = np.zeros((products_count, top, users_count))

    for i in range(products_count):
        top_sim_products = distance_matrix[i].argsort()[1:top + 1]
        top_similar_ratings[i] = train_data_matrix.T[top_sim_products]

    pred = np.zeros((products_count, users_count))
    for i in range(products_count):
        pred[i] = top_similar_ratings[i].sum(axis=0) / top

    return pred.T