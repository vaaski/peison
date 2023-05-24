import sys
from tokenize import tokenize, untokenize

from grammar import grammar

filename = sys.argv[1] # error checking

with open(filename, 'rb') as src:
  tokens = []
  for token in tokenize(src.readline):
    if token.type == 1 and token.string in grammar:
      # new_token = (token.type, grammar[token.string])
      # print(new_token)
      tokens.append((token.type, grammar[token.string]))
    else:
      tokens.append((token.type, token.string))

# rebuild code from our "modified" tokens
code = untokenize(tokens).decode('utf-8')

# write to file of the same name, but with .pei extension
with open(filename[:-3] + '.pei', 'w') as dest:
  dest.write(code)
