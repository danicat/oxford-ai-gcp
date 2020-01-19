#!/usr/bin/env python
from functools import reduce
from itertools import groupby
from operator import itemgetter

with open("hamlet.txt","r") as f: 
    words = f.read().split()
    ones = map(lambda x: (x, 1), words)
    print([reduce(lambda x, y: (x[0], x[1] + y[1]), group)
        for _, group in groupby(sorted(ones), key=itemgetter(0))])