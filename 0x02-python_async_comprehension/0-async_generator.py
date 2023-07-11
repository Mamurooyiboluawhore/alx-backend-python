#!/usr/bin/env python3
''' Async Generator '''
import asyncio
import random


async def async_generator():
    ''' a function that genrate random float'''
    for i in range(10):
        await asyncio.sleep(1)
        i = random.uniform(1, 10)
        yield i
