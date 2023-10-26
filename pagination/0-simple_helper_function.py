#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function that takes 2 integers"""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
