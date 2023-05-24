# Python-Schlüsselwörter
import keyword

# Gib alle Python-Schlüsselwörter aus
print(keyword.kwlist)

# Beispielhafte Verwendung jedes Schlüsselworts


def und_func():
  x = True
  y = False
  if x and y:
    print("Sowohl x als auch y sind wahr")


def als_func():
  x = "Hallo, Welt!"
  y = x[2:5]  # Slicing
  print(y)  # Ausgabe: llo


def behaupte_func():
  x = 5
  assert x == 5, "x ist nicht gleich 5"


def abbruch_func():
  for i in range(10):
    if i == 5:
      break
    print(i)


def klasse_func():
  class MeineKlasse:
    def __init__(self):
      self.name = "John"

    def begrüßen(self):
      print("Hallo,", self.name)

  obj = MeineKlasse()
  obj.begrüßen()


def fortsetzen_func():
  for i in range(10):
    if i == 5:
      continue
    print(i)


def def_func():
  def addiere(x, y):
    return x + y

  ergebnis = addiere(3, 5)
  print(ergebnis)


def lösche_func():
  x = 5
  del x


def sonstwenn_func():
  x = 5
  if x == 1:
    print("x ist 1")
  elif x == 2:
    print("x ist 2")
  else:
    print("x ist weder 1 noch 2")


def sonst_func():
  x = 5
  if x > 10:
    print("x ist größer als 10")
  else:
    print("x ist kleiner oder gleich 10")


def außer_func():
  try:
    x = 5 / 0
  except ZeroDivisionError:
    print("Fehler: Division durch Null")


def schließlich_func():
  try:
    x = 5 / 0
  except ZeroDivisionError:
    print("Fehler: Division durch Null")
  finally:
    print("Finally-Block ausgeführt")


def für_func():
  fruechte = ["Apfel", "Banane", "Kirsche"]
  for frucht in fruechte:
    print(frucht)


def von_func():
  from math import sqrt
  print(sqrt(16))


def global_func():
  x = 5

  def func():
    global x
    x = 10

  func()
  print(x)


def wenn_func():
  x = 5
  if x > 0:
    print("x ist positiv")


def import_func():
  import math
  print(math.sqrt(16))


def in_func():
  x = 5
  y = [1, 2, 3, 4, 5]
  if x in y:
    print("x ist in der Liste enthalten")


def ist_func():
  x = 5
  y = 10
  if x is y:
    print("x und y verweisen auf dasselbe Objekt")


def lambda_func():
  def addiere(x, y): return x + y
  ergebnis = addiere(3, 5)
  print(ergebnis)


def nichtlokal_func():
  def äußere():
    x = "lokal"

    def innere():
      nonlocal x
      x = "nichtlokal"
      print("inner:", x)

    innere()
    print("äußere:", x)

  äußere()


def nicht_func():
  x = False
  if not x:
    print("x ist Falsch")


def oder_func():
  x = True
  y = False
  if x or y:
    print("Entweder x oder y ist wahr")


def überspringen_func():
  pass


def auslöse_func():
  x = 5
  if x > 0:
    raise ValueError("x muss negativ sein")


def rückgabe_func():
  def addiere(x, y):
    return x + y

  ergebnis = addiere(3, 5)
  return ergebnis


def versuche_func():
  try:
    x = 5 / 0
  except ZeroDivisionError:
    print("Fehler: Division durch Null")


def während_func():
  i = 0
  while i < 5:
    print(i)
    i += 1


def mit_func():
  with open("datei.txt", "r") as f:
    daten = f.read()
    print(daten)


def erzeugen_func():
  def generator():
    for i in range(5):
      yield i

  g = generator()
  for x in g:
    print(x)


# Rufe alle Funktionen auf
und_func()
als_func()
behaupte_func()
abbruch_func()
klasse_func()
fortsetzen_func()
def_func()
lösche_func()
sonstwenn_func()
sonst_func()
außer_func()
schließlich_func()
für_func()
von_func()
global_func()
wenn_func()
import_func()
in_func()
ist_func()
lambda_func()
nichtlokal_func()
nicht_func()
oder_func()
überspringen_func()
# raise_func()
rückgabe_func()
versuche_func()
während_func()
# with_func()
erzeugen_func()
