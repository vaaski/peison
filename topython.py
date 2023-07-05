import sys

from grammar import swap, grammar_reverse
from util import read_file_into_string

# Lese den Dateinamen aus den Kommandozeilenargumenten
filename = sys.argv[1]
# Lese den Inhalt der Datei in einen String
input_string = read_file_into_string(filename)

# Wende die umgekehrten Grammatikregeln auf den String an
output = swap(input_string, grammar_reverse)

# Schreibe das Ergebnis in eine Datei mit der gleichen Bezeichnung, aber mit der Erweiterung .py
with open(filename[:-4] + '.py', 'w') as dest:
  dest.write(output)