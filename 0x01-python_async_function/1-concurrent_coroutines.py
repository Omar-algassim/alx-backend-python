#!/usr/bin/env python3
"""concurrent module"""
import asyncio
from typing import List
wait = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """run wait_random n times and return waits time list"""
    wait_list = [await wait(max_delay) for _ in range(n)]
    return sorted(wait_list)
