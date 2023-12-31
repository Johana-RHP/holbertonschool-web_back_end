#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of the list of floats"""
    suma: float = 0.0

    for item in input_list:
        suma += item
    return suma
