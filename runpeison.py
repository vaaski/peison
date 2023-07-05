import sys

from grammar import swap, grammar_reverse
from util import read_file_into_string

filename = sys.argv[1]
input_string = read_file_into_string(filename)

output = swap(input_string, grammar_reverse)

exec(output)
