import io
import tokenize

grammar = {
  '__debug__': '__fehlerfindung__',
  '__doc__': '__dok__',
  '__import__': '__import__',
  '__name__': '__name__',
  'abs': 'bauchmuskeln',
  'and': 'und',
  'apply': 'verwende',
  'ArithmeticError': 'ArithmetischerFehler',
  'as': 'als',
  'assert': 'behaupte',
  'AssertionError': 'AnnahmeFehler',
  'AttributeError': 'AttributFehler',
  'basestring': 'basiszeichenkette',
  'bool': 'wahrfalsch',
  'break': 'abbrechen',
  'buffer': 'puffer',
  'callable': 'aufrufbar',
  'chr': 'chr',
  'class': 'klasse',
  'classmethod': 'klassenmethode',
  'cmp': 'vgl',
  'coerce': 'zwingen',
  'compile': 'kompiliere',
  'complex': 'komplex',
  'continue': 'weiter',
  'copyright': 'urheberrecht',
  'credits': 'würdigung',
  'def': 'definiere',
  'del': 'entferne',
  'delattr': 'entfattr',
  'DeprecationWarning': 'VeraltetWarnung',
  'dict': 'lexikon',
  'dir': 'verz',
  'divmod': 'divmod',
  'elif': 'wennsonst',
  'Ellipsis': 'Ellipse',
  'else': 'sonst',
  'enumerate': 'aufzählung',
  'EnvironmentError': 'UmgebungsFehler',
  'EOFError': 'EOFFehler',
  'eval': 'eval',
  'except': 'außer',
  'Exception': 'Ausnahme',
  'exec': 'erledige',
  'execfile': 'ausführedatei',
  'exit': 'raus',
  'False': 'Falsch',
  'file': 'datei',
  'filter': 'filter',
  'finally': 'schließlich',
  'float': 'fließkomma',
  'FloatingPointError': 'FließkommaFehler',
  'for': 'für',
  'from': 'von',
  'frozenset': 'gefroreneset',
  'FutureWarning': 'ZukunftsWarnung',
  'getattr': 'nimmattr',
  'global': 'global',
  'globals': 'globale',
  'hasattr': 'hatattr',
  'hash': 'hash',
  'help': 'hilfe',
  'hex': 'hex',
  'id': 'id',
  'if': 'wenn',
  'import': 'importiere',
  'ImportError': 'ImportFehler',
  'in': 'im',
  'IndentationError': 'EinruckungsFehler',
  'IndexError': 'IndexFehler',
  'input': 'eingabe',
  'int': 'ganzzahl',
  'intern': 'intern',
  'IOError': 'EAFehler',
  'is': 'ist',
  'isinstance': 'istinstanz',
  'issubclass': 'istunterklasse',
  'iter': 'iter',
  'KeyboardInterrupt': 'TastaturUnterbrechung',
  'KeyError': 'SchlüsselFehler',
  'len': 'länge',
  'license': 'lizenz',
  'list': 'liste',
  'locals': 'lokal',
  'long': 'lang',
  'LookupError': 'NachsehenFehler',
  'map': 'map',
  'max': 'max',
  'MemoryError': 'SpeicherFehler',
  'min': 'min',
  'NameError': 'NamensFehler',
  'None': 'Nichts',
  'nonlocal': 'nichtlokal',
  'not': 'nicht',
  'NotImplemented': 'NichtImplementiert',
  'NotImplementedError': 'NichtImplementiertFehler',
  'object': 'objekt',
  'oct': 'oct',
  'open': 'öffne',
  'or': 'oder',
  'ord': 'ord',
  'OSError': 'BetriebssystemFehler',
  'OverflowError': 'ÜberGrenzeFehler',
  'OverflowWarning': 'ÜberGrenzeWarnung',
  'pass': 'pass',
  'PendingDeprecationWarning': 'AusstehendeEinstellungWarnung',
  'pow': 'hoch',
  'print': 'drucken',
  'property': 'eigenschaft',
  'quit': 'schließe',
  'raise': 'behandle',
  'range': 'bereich',
  'raw_input': 'raw_input',
  'reduce': 'reduziere',
  'ReferenceError': 'ReferenzFehler',
  'reload': 'ladeneu',
  'repr': 'repr',
  'return': 'zurück',
  'reversed': 'umgekehrt',
  'round': 'runde',
  'RuntimeError': 'LaufzeitFehler',
  'RuntimeWarning': 'LaufzeitWarnung',
  'self': 'selbst',
  'set': 'menge',
  'setattr': 'setzeattr',
  'slice': 'schlitz',
  'sorted': 'sortiert',
  'sqrt': 'quadratwurzel',
  'StandardError': 'StandardFehler',
  'staticmethod': 'statischemethode',
  'StopIteration': 'StopIteration',
  'str': 'zeichenkette',
  'sum': 'summe',
  'super': 'ober',
  'SyntaxError': 'SyntaxFehler',
  'SyntaxWarning': 'SyntaxWarnung',
  'SystemError': 'SystemFehler',
  'SystemExit': 'SystemAusgang',
  'TabError': 'TabFehler',
  'True': 'Wahr',
  'try': 'versuche',
  'tuple': 'tupel',
  'type': 'typ',
  'TypeError': 'TypFehler',
  'UnboundLocalError': 'UngebundenLokalFehler',
  'unichr': 'unichr',
  'unicode': 'unicode',
  'UnicodeDecodeError': 'UnicodeDecodierungsFehler',
  'UnicodeEncodeError': 'UnicodeCodierungsFehler',
  'UnicodeError': 'UnicodeFehler',
  'UnicodeTranslateError': 'UnicodeÜrbersetzungsFehler',
  'UserWarning': 'BenutzerWarnung',
  'ValueError': 'WertFehler',
  'vars': 'variablen',
  'Warning': 'Warnung',
  'while': 'solange',
  'WindowsError': 'FensterFehler',
  'with': 'mit',
  'xrange': 'xbereich',
  'yield': 'ergibt',
  'ZeroDivisionError': 'NullTeilungsFehler',
  'zip': 'zip',
}
grammar_reverse = {value: key for key, value in grammar.items()}


def swap(input_string, dict):
  # Erstelle ein BytesIO-Objekt aus dem Eingabestring
  src = io.BytesIO(input_string.encode())
  # Initialisiere eine leere Liste, um die modifizierten Tokens zu speichern
  tokens = []
  # Initialisiere ein Tupel, um die Endposition des vorherigen Tokens zu speichern
  prev_end = (0, 0)
  # Schleife durch jedes Token im Eingabestring
  for token in tokenize.tokenize(src.readline):
    # Wenn das Token ein NAME-Token ist und sein String-Wert im Wörterbuch enthalten ist
    if token.type == tokenize.NAME and token.string in dict:
      # Überprüfe, ob Leerzeichen vor dem Token vorhanden sind
      spaces = token.start[1] - prev_end[1]
      if token.start[0] > prev_end[0]:
        spaces = token.start[1]
      # Füge die erforderlichen Leerzeichen und den entsprechenden Wert aus dem Wörterbuch zur Liste der Tokens hinzu
      tokens.append(' ' * spaces)
      tokens.append(dict[token.string])
    # Wenn das Token ein NEWLINE-Token ist, füge es einfach zur Liste der Tokens hinzu
    elif token.type == tokenize.NEWLINE:
      tokens.append(token.string)
    # Wenn das Token kein ENCODING- oder ENDMARKER-Token ist
    elif token.type not in (tokenize.ENCODING, tokenize.ENDMARKER):
      # Überprüfe, ob Leerzeichen vor dem Token vorhanden sind
      spaces = token.start[1] - prev_end[1]
      if token.start[0] > prev_end[0]:
        spaces = token.start[1]
      # Füge die erforderlichen Leerzeichen und das Token selbst zur Liste der Tokens hinzu
      tokens.append(' ' * spaces)
      tokens.append(token.string)
    # Aktualisiere die Endposition des vorherigen Tokens
    prev_end = token.end

  # Füge die Liste der Tokens zu einem einzelnen String zusammen und gib ihn zurück
  return ''.join(tokens)
