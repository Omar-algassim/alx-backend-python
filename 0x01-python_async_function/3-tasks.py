#!/usr/bin/env python3
"""task object"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return a task object of a wait random function"""
    return asyncio.Task(wait_random(max_delay))