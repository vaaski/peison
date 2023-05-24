import sys
from tokenize import tokenize, untokenize

from grammar import grammar
reversed_grammar = {value: key for key, value in grammar.items()}

filename = sys.argv[1]  # error checking

with open(filename, 'rb') as src:
  tokens = []
  for token in tokenize(src.readline):
    if token.type == 1 and token.string in reversed_grammar:
      tokens.append((token.type, reversed_grammar[token.string]))
    else:
      tokens.append((token.type, token.string))

# rebuild code from our "modified" tokens
code = untokenize(tokens).decode('utf-8')

# execute the code
exec(code)
