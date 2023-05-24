import io
import tokenize

grammar = {
  'and': 'und',
  'assert': 'behaupte',
  'break': 'abbrechen',
  'class': 'klasse',
  'continue': 'weiter',
  'def': 'definiere',
  'del': 'entferne',
  'elif': 'wennsonst',
  'else': 'sonst',
  'except': 'ausser',
  'exec': 'erledige',
  'finally': 'schliesslich',
  'for': 'fuer',
  'from': 'von',
  'if': 'wenn',
  'import': 'importiere',
  'in': 'im',
  'not': 'nicht',
  'or': 'oder',
  'pass': 'pass',
  'print': 'drucken',
  'raise': 'behandle',
  'return': 'zurueck',
  'try': 'versuche',
  'while': 'solange',
  'yield': 'ergibt',
}
grammar_reverse = {value: key for key, value in grammar.items()}


def swap(input_string, dict):
  src = io.BytesIO(input_string.encode())
  tokens = []
  prev_end = (0, 0)
  for token in tokenize.tokenize(src.readline):
    if token.type == tokenize.NAME and token.string in dict:
      # Check for spaces before the token
      spaces = token.start[1] - prev_end[1]
      if token.start[0] > prev_end[0]:
        spaces = token.start[1]
      tokens.append(' ' * spaces)
      tokens.append(dict[token.string])
    elif token.type == tokenize.NEWLINE:
      tokens.append(token.string)
    elif token.type not in (tokenize.ENCODING, tokenize.ENDMARKER):
      # Check for spaces before the token
      spaces = token.start[1] - prev_end[1]
      if token.start[0] > prev_end[0]:
        spaces = token.start[1]
      tokens.append(' ' * spaces)
      tokens.append(token.string)
    prev_end = token.end

  return ''.join(tokens)
