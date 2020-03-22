import numpy as np


def ratings_to_np_array(ratings):
    return np.mat(ratings)


def split_for_training(data, test_selection_size=0.25):
    test_selection_concrete_size = round(len(data) * test_selection_size)
    if len(data) <= test_selection_concrete_size:
        raise Exception('Invalid test selection size.')
    return data[:test_selection_concrete_size], data[test_selection_concrete_size:]

