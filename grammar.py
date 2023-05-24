import io
import tokenize

grammar = {
  'and': 'und',
  'as': 'als',
  'assert': 'behaupte',
  'break': 'abbrechen',
  'class': 'klasse',
  'continue': 'weiter',
  'def': 'definiere',
  'del': 'entferne',
  'elif': 'wennsonst',
  'else': 'sonst',
  'except': 'außer',
  'exec': 'erledige',
  'False': 'Falsch',
  'finally': 'schließlich',
  'for': 'für',
  'from': 'von',
  'from': 'von',
  'global': 'global',
  'if': 'wenn',
  'import': 'importiere',
  'in': 'im',
  'is': 'ist',
  'None': 'Nichts',
  'nonlocal': 'nichtlokal',
  'not': 'nicht',
  'or': 'oder',
  'pass': 'pass',
  'print': 'drucken',
  'raise': 'behandle',
  'range': 'bereich',
  'return': 'zurück',
  'self': 'selbst',
  'sqrt': 'quadratwurzel',
  'True': 'Wahr',
  'try': 'versuche',
  'while': 'solange',
  'with': 'mit',
  'yield': 'ergibt',
  'ZeroDivisionError': 'NullTeilungsFehler',
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
