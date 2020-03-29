from math import sqrt

import numpy as np
from sklearn.metrics.pairwise import pairwise_distances


def prepare_ratings(ratings):
    return np.mat(ratings)


def split_for_training(data, test_selection_size=0.25):
    test_selection_concrete_size = round(len(data) * test_selection_size)
    if len(data) <= test_selection_concrete_size:
        raise Exception('Invalid test selection size.')
    return data[:test_selection_concrete_size], data[test_selection_concrete_size:]


def rmse(predictions, real_values):
    mse = np.average(
        (predictions - real_values) ** 2,
        axis=0,
        weights='uniform_average')
    return sqrt(mse)


def cosine_distance(u, v):
    uv = np.average(u * v)
    uu = np.average(np.square(u))
    vv = np.average(np.square(v))
    dist = 1.0 - uv / np.sqrt(uu * vv)
    return dist


def get_distances(items):
    distances = np.zeros(
        (len(items), len(items))
    )
    for i in range(len(items)):
        for j in range(len(items)):
            distances[i][j] = cosine_distance(items[i], items[j])

    return distances

