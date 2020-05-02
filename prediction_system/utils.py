from math import sqrt

import numpy as np


def prepare_ratings(users_count, products_count, ratings):
    data_matrix = np.zeros((users_count, products_count))
    for rate in ratings:
        data_matrix[rate.user_id - 1][rate.product_id - 1] = rate.rate
    return data_matrix


def split_for_training(data, test_selection_size=0.25):
    test_selection_concrete_size = round(len(data) * test_selection_size)
    if len(data) <= test_selection_concrete_size:
        raise Exception('Invalid test selection size.')
    return data[:test_selection_concrete_size], data[test_selection_concrete_size:]


def rmse(predictions, real_values):
    prediction = np.nan_to_num(predictions)[real_values.nonzero()].flatten()
    ground_truth = np.nan_to_num(real_values)[real_values.nonzero()].flatten()
    mse = np.average(np.average((prediction - ground_truth) ** 2, axis=0))
    return sqrt(mse)


def cosine_distance(u, v):
    uv = np.average(u * v)
    uu = np.average(np.square(u))
    vv = np.average(np.square(v))
    dist = 1.0 - uv / np.sqrt(uu * vv) if np.sqrt(uu * vv) else 0.0
    return dist


def get_distances(items):
    length = len(items)
    distances = np.zeros(
        (length, length)
    )

    for i in range(length):
        for j in range(length):
            distances[i][j] = cosine_distance(items[i], items[j])

    return distances

