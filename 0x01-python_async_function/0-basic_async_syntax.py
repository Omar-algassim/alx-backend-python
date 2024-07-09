#!/usr/bin/env python3
"""async function"""
import asyncio
import random


async def wait_random(max_delay=10.0):
    """wait random second and return it"""
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num

