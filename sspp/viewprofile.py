#!/usr/bin/env python

import sys
import pstats

filename = sys.argv[1]

try:
    pstats.Stats(filename).strip_dirs().sort_stats('cumtime').print_stats()
except BrokenPipeError:
    pass
