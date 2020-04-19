import numpy as np


def k_fract_predict_user(rating, users_count, products_count, distance_matrix, train_data_matrix):
    top_similar = np.zeros((users_count, rating))

    for i in range(rating):
        user_sim = distance_matrix[i]
        top_sim_users = user_sim.argsort()[1:rating + 1]

        for j in range(rating):
            top_similar[i, j] = top_sim_users[j]

    abs_sim = np.abs(distance_matrix)
    pred = np.zeros((users_count, products_count))

    for i in range(users_count):
        indexes = top_similar[i].astype(np.int)
        numerator = distance_matrix[i][indexes]

        product = numerator.dot(train_data_matrix[indexes])

        denominator = abs_sim[i][top_similar[i].astype(np.int)].sum()

        pred[i] = product / denominator

    return pred


def k_fract_predict_item(rating, users_count, products_count, distance_matrix, train_data_matrix):
    top_similar = np.zeros((products_count, rating))

    for i in range(products_count):
        products_sim = distance_matrix[i]
        top_sim_products = products_sim.argsort()[1:rating + 1]

        for j in range(rating):
            top_similar[i, j] = top_sim_products.T[j]

    abs_sim = np.abs(distance_matrix)
    pred = np.zeros((products_count, users_count))

    for i in range(users_count):
        indexes = top_similar[i].astype(np.int)
        numerator = distance_matrix[i][indexes]

        product = numerator.dot(train_data_matrix.T[indexes])

        denominator = abs_sim[i][indexes].sum()
        denominator = denominator if denominator != 0 else 1

        pred[i] = product / denominator

    return pred.T