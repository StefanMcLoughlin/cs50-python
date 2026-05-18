import sys

from practice_8_sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])