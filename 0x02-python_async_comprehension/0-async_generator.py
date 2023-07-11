#!/usr/bin/env python3
''' Async Generator'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float]:
    ''' a function that genrate random float'''
    for i in range(10):
        await asyncio.sleep(1)
        i = random.uniform(1, 10)
        yield i
