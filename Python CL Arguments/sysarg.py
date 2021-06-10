

import getopt
import sys

args = sys.argv[1:]

opts, otros = getopt.getopt(args, 'o:v', ['version=', 'auth='])

print('\nFile name:', sys.argv[0])

print('\nArgumentos:')
for op, arg in opts:
    print(op, arg)

print('\nOtros argumentos:', otros)

