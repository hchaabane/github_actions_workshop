"""
this module for testing
"""
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from main import calculate_x_squared


def test_squared():
    """
    testing squared
    :return:
    """
    assert calculate_x_squared(2) == 4
