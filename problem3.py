import numpy as np 
def normalize_numbers(arr):
  """
  arr -> arr normalized 
  function takes in a two-dimensional array of numerical data and normalizes the data so that all values are between 0 and 1.
    >>> normalize_numbers(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]))
    array([[0.        , 0.14285714, 0.28571429, 0.42857143],
           [0.57142857, 0.71428571, 0.85714286, 1.        ]])
    >>> normalize_numbers(np.array([[7, 6, 7], [8, 7, 8]]))
    array([[0.5, 0. , 0.5],
           [1. , 0.5, 1. ]])
    >>> normalize_numbers(np.array([[-7, 6, 7], [8, -7, 8]]))
    array([[0.        , 0.86666667, 0.93333333],
           [1.        , 0.        , 1.        ]])
    >>> sample = np.array([[200, 4, 400, 100], [150, 230, 215, 350]])
    >>> normalize_numbers(sample)
    array([[0.49494949, 0.        , 1.        , 0.24242424],
           [0.36868687, 0.57070707, 0.53282828, 0.87373737]])

    """
  if np.max(arr) == 0:
    return arr
  if np.max(arr) == np.min(arr):
    return arr / np.max(arr)
  else:

    arr_numerator = (arr - np.min(arr))
    arr_denominator = (np.max(arr) - np.min(arr))
    arr_normalized = arr_numerator / arr_denominator
    return(arr_normalized)
  

normalize_numbers(np.array([[200,4,400,100],[150,230,215,350]]))
print(normalize_numbers(np.array([[1,1,1,1],[1,1,1,1]])))
print(normalize_numbers(np.array([[0, 0, 0], [0, 0, 0]])))
print(normalize_numbers(np.array([[0, 0, 0], [0, 0, 0]])))