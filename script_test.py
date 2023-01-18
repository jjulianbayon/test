
#!/usr/bin/env python

import sys
from subprocess import call

BYTES_PER_KB = 1000
UNITS = ['B', 'KB', 'MB', 'GB']

if len(sys.argv) < 4:
    print 'Usage: %s [size] [unit] [path]' % sys.argv[0]
    exit(1)

size = float(sys.argv[1])
unit = sys.argv[2].upper()
filepath = sys.argv[3]

try:
    multiplier = UNITS.index(unit)
except ValueError:
    print """'%s' is an invalid unit. Accepted units: %s""" % (unit, str(UNITS))
    exit(1)

num_bytes = size * pow(BYTES_PER_KB, multiplier)

call(['dd', 'if=/dev/zero', 'of=%s' % filepath, 'bs=%d' % num_bytes, 'count=1'])