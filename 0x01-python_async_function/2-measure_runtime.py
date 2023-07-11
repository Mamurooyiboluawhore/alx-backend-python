#!/usr/bin/env python3
''' Measure the runtime '''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' a function that measures runtime'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_time = elapsed_time / n
    return average_time
