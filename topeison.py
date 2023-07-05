import sys

from grammar import swap, grammar
from util import read_file_into_string

# Lese den Dateinamen aus den Kommandozeilenargumenten
filename = sys.argv[1]
# Lese den Inhalt der Datei in einen String
input_string = read_file_into_string(filename)

# Wende die Grammatikregeln auf den String an
output = swap(input_string, grammar)

# Schreibe das Ergebnis in eine Datei mit der gleichen Bezeichnung, aber mit der Erweiterung .pei
with open(filename[:-3] + '.pei', 'w') as dest:
  dest.write(output)