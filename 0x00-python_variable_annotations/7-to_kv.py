#!/usr/bin/env python3
"""input a string and an int/float to return a tuple"""


def to_kv(k: str, v: [int | float]) -> tuple:
    """to_kv: takes a string k and an int/float v as arguments
    and returns a tuple"""
    return (k, v ** 2)