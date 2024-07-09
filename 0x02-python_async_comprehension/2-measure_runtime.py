#!/usr/bin/env python3
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """clculate the time async_comprehension spend"""
    comprhension = asyncio.create_task(async_comprehension())
    start = time.perf_counter()
    for i in range(4):
        await asyncio.gather(comprhension)
    end = time.perf_counter()
    return end - start
