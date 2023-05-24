import sys

from grammar import swap, grammar
from util import read_file_into_string

filename = sys.argv[1]
input_string = read_file_into_string(filename)

output = swap(input_string, grammar)

# write to file of the same name, but with .pei extension
with open(filename[:-3] + '.pei', 'w') as dest:
  dest.write(output)
