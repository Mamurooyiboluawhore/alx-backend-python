#!/usr/bin/env python3
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
''' Run time for four parallel comprehensions'''


async def measure_runtime():
    ''' a runtime function'''
    start_time = time.time()

    await asyncio.gather(*[async_comprehension() for m in range(4)])
    end_time = time.time()
    runtime = end_time - start_time
    return runtime
