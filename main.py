"""
main.py
This module is a test
"""
import pandas as pd
def calculate_x_squared(x):
    """
    Calculates x squared
    :param x:  int
    :return: int
    """
    print("x squared calcualted")
    return x*x

def calculate_difference(x, y):
    """
    Calculates difference between y and x
    :param x: int
    :param y: int
    :return: difference int
    """
    print("difference calculated")
    return y - x


def create_dataframe():
  """
  Creates dummy dataframe
  :return: pd.dataframe
  """
  df = pd.DataFrame({"A": [0, 2, 9, 6], "B": [5, 2, 7, 6] , "C":["a", "b", "c", "d"]})
  return df

