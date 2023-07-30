#!/usr/bin/env python3
""" Complex type- list and float """
from typing import List

def sum_list(input_list: List[float]) -> float:
    """ takes a list and returns the sum as a float """
    return float(sum(input_list))
