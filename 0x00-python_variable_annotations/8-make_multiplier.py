#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by the multiplier"""
    def multiplier_func(value: float) -> float:
        return float(value * multiplier)
    return multiplier_func
