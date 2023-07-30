#!/usr/bin/env python3
""" annotate value in a function """
from typing import Tuple, List


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
