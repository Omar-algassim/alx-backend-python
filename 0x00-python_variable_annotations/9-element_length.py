#!/usr/bin/env python3
"""get iterable and return list of tuples
with each element and its length"""
from typing import Sequence, Tuple, List, Iterable

 
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that takes a list of strings and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
