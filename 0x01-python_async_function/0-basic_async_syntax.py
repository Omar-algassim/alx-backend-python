#!/usr/bin/env python3
"""async function"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """wait random second and return it"""
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
