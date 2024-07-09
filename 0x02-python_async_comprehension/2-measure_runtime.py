#!/usr/bin/env python3
"""mesure the time"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """clculate the time async_comprehension spend"""
    comprhension = [(async_comprehension()) for i in range(4)]
    start = time.perf_counter()
    await asyncio.gather(*comprhension)
    end = time.perf_counter()
    return end - start
