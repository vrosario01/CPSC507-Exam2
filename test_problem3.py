import numpy as np

from problem3 import normalize_numbers


def test_normalize_all_values_are_negative():
    assert np.allclose(normalize_numbers(np.array([[-1, -2, -3], [-4, -5, -6]])),np.array([[1.0, 0.8, 0.6], [0.4, 0.2, 0.0]]))


def test_normalize_all_values_are_the_same():
    assert np.allclose(normalize_numbers(np.array([[5, 5, 5]])),np.array([[1., 1., 1.]]))


def test_normalize_values_are_zero():
    assert np.allclose(normalize_numbers(np.array([[0, 0, 0], [0, 0, 0]])),np.array([[0, 0, 0], [0, 0, 0]]))
