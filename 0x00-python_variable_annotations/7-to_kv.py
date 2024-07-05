#!/usr/bin/env python3
"""input a string and an int/float to return a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv: takes a string k and an int/float v as arguments
    and returns a tuple"""
    return (k, v ** 2)
