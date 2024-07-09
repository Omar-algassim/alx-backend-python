#!/usr/bin/env python3
"""async yeild a randim number"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator:
    """yeild a random number after wait 1 second"""
    for _ in range(10):
        radn_num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield radn_num
