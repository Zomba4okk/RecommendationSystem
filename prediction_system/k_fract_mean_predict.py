import numpy as np


def k_fract_mean_predict_user(rating, users_count, products_count, distance_matrix, train_data_matrix):
    top_similar = np.zeros((users_count, rating))

    for i in range(users_count):
        user_sim = distance_matrix[i]
        top_sim_users = user_sim.argsort()[1:rating + 1]

        for j in range(rating):
            top_similar[i, j] = top_sim_users[j]

    abs_sim = np.abs(distance_matrix)
    pred = np.zeros((users_count, products_count))

    for i in range(users_count):
        indexes = top_similar[i].astype(np.int)
        numerator = distance_matrix[i][indexes]

        mean_rating = np.array([x for x in train_data_matrix[i] if x > 0]).mean()
        diff_ratings = train_data_matrix[indexes] - train_data_matrix[indexes].mean()
        numerator = numerator.dot(diff_ratings)
        denominator = abs_sim[i][top_similar[i].astype(np.int)].sum()

        pred[i] = mean_rating + numerator / denominator

    return pred


def k_fract_mean_predict_item(rating, users_count, products_count, distance_matrix, train_data_matrix):
    top_similar = np.zeros((products_count, rating))

    for i in range(products_count):
        product_sim = distance_matrix[i]
        top_sim_products = product_sim.argsort()[1:rating + 1]

        for j in range(rating):
            top_similar[i, j] = top_sim_products[j]

    abs_sim = np.abs(distance_matrix)
    pred = np.zeros((products_count, users_count))

    for i in range(products_count):
        indexes = top_similar[i].astype(np.int)
        numerator = distance_matrix[i][indexes]

        mean_rating = np.array([x for x in train_data_matrix.T[i] if x > 0]).mean()
        mean_rating = 0 if np.isnan(mean_rating) else mean_rating

        diff_ratings = train_data_matrix.T[indexes] - mean_rating
        numerator = numerator.dot(diff_ratings)
        denominator = abs_sim[i][top_similar[i].astype(np.int)].sum()
        denominator = denominator if denominator != 0 else 1

        pred[i] = mean_rating + numerator / denominator

    return pred.T
