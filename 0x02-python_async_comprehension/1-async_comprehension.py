#!/usr/bin/env python3
""""async comperhensen"""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """implement async_generator and return list of float"""
    list_rand = [x async for x in async_generator()]
    return list_rand
