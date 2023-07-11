#!/usr/bin/env python3
import asyncio

async_generator = __import__('0-async_generator').async_generator
'''  Async Comprehensions'''


async def async_comprehension():
    ''' a function that collects random numbers using comprehension'''
    comp = [number async for number in async_generator()]
    return comp
