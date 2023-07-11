#!/usr/bin/env python3
''' execute multiple coroutines at the same time with async '''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' an async function that runs multiple coroutine'''
    delays = [wait_random(max_delay) for i in range(n)]
    output = await asyncio.gather(*delays)
    return output
