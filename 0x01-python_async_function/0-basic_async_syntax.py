#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ A function that takes a random int and runs in asynchronously """
    delays = random.uniform(0, max_delay)
    await asyncio.sleep(delays)
    return delays
