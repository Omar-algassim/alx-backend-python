#!/usr/bin/env python3
from typing import Sequence, Tuple, List, Iterable

 
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
