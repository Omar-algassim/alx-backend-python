#!/usr/bin/env python3
"""summation of a list of floats and integers"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list: takes a list of floats and integers
    as argument and returns their sum"""
    return sum(mxd_lst)
