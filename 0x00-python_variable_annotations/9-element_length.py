#!/usr/bin/env python3
''' duck type'''
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' duck type '''
    return [(i, len(i)) for i in lst]
