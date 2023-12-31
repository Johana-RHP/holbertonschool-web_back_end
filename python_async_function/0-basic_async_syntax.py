#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return a random float number"""
    num: float = random.uniform(0, max_delay)
    await asyncio.sleep(num)

    return num
