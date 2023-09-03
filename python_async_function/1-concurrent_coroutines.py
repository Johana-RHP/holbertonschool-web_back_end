#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """float time random"""
    list_of_the_delays = []
    for x in range(n):
        list_of_the_delays.append(wait_random(max_delay))
    sort = await asyncio.gather(*list_of_the_delays)
    return sorted(sort)
