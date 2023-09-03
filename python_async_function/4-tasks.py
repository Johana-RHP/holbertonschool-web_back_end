#!/usr/bin/env python3
"""Tasks"""
import asyncio
import typing
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This code is nearly identical to wait_n"""
    delays = []
    numbers = [task_wait_random(max_delay) for x in range(n)]
    done = asyncio.as_completed(numbers)
    for task in done:
        wait = await task
        delays.append(wait)

    return sorted(delays)
