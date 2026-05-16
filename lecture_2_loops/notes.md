Loops - Wiederholungen

Loops sind Wiederholungen, die es Programmen erlauben Dinge zu wiederholen.

Ohne Loop: 

print("meow")
print("meow")
print("meow")

Das würde funktionieren ist aber sehr begrenzt, da dieser Code nur 3x meow wiederholt. 
In der Theorie müsste man diesen Code immer wieder kopieren, wenn man z.B. 10x oder 50x meow wiederholt haben möchte. 
Oder wenn man den Befehl auf ein bellen "wuff" ändern möchte, müsste man jede Zeile einzeln ändern.

While-Loops:

Mithilfe der Funktion while, können loops erstellt werden. 
Im ersten Schritt wird eine variable erstellt, wie oft etwas wiederholt werden soll. Dieser Befehl muss eine TRUE oder FALSE Antwort sein.
TRUE = Schleife läuft weiter
FALSE = Schleife stoppt. 

Zum Beispiel: 
i = 3
while i != 0:
    print("meow")

ACHTUNG!! Das ist eine Endlosschleife, weil das Ergebnis immer TRUE ist!
Sollte man mal in einer Endlosschleife feststecken, kann man den Befehl mit CRTL + C abbrechen.

Um dem Loop ein einfaches Ende zu geben, kann man - jedes Mal um 1 reduzieren. 

Beispiel: 

i = 3
while i != 0:
    print("meow")
    i = i - 1

In diesem Beispiel wird im Code von 3 runtergezählt. Eine andere Methode ist von 0 aufwärts zu zählen.

Beispiel: 

i = 0
while i < 3:
    print("meow")
    i = i + 1

Das ganze kann wieder optimiert werden (Pythonic)

i = 0
while i < 3:
    print("meow")
    i += 1

 

For Loops:

Ein weiterer und besserer Ansatz für Loops sind die for loops, ergänzt durch eine Liste. 
Python geht diese Element für Element durch und stoppt die Schleife dann automatisch. 
Dies ist eine einfache Umstellung auf den for-loop, aber auch hier ist es begrenzt, da die Liste manuell weitergeführt werden muss.

for i in [0, 1, 2]:
    print("meow")

Um den Loop skalierbar zu machen, kann man die Liste einfach durch einen range() Befehl austauschen.

for i in range(3):
    print("meow")

Um den Code mehr Pythonic zu machen, kann man die variable austauschen


for _ in range(3):
    print("meow")


Ein weiterer Schritt, um den Code noch mehr zu optimieren ist der folgende: 

print("meow\n" * 3, end="")

Mit /n wird der Code manipuliert, dass am Ende ein Zeilenumbruch stattfindet und mit dem end Befehl wird das Ende manipuliert, dass kein extra Absatz am Ende eingefügt wird.

So ist der Code nur noch einzeilig aber weniger gut lesbar.

Loops erstellen für user input: 

Mit while True: kann direkt am Anfang ein "Infint Loop" erstellt werden, wichtig ist aber das dieser durch User input unterbrochen werden kann. 


while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")

Sobald der User ein Zahl größer als 0 eingibt, wird der Befehl print("meow") ausgeführt. 
Alles was kleiner als 0, also negative Zahlen eingegeben wird, wird die Fragestellung wiederholt.

Um das Ganze im Code nochmal besser darzustellen, kann das Ganze in selbst erstellte Funktionen untergebracht werden: 


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")
main()

Wir definieren mit number = get_number die Eingabe des Users.
In der Funktion wird der User gefragt "What's n?" Wenn n größer als 0 ist, wird n returned, ist es kleiner/gleich 0 wird der loop wiederholt. 

Dann wird die meow Funktion ausgeführt. 

Def main(): fragt alles ab und erst ab main() wird der Code erst ausgeführt. 


Loops and Lists: 

Mithilfe von Python können wir Listen angegeben und diese Abfragen oder auch ein Ranking erstellen lassen. 

students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])

Lenght (len) zaehlt Buchstaben, Leerzeichen oder auch den Inhalt von Listen []
Mit len (lenght) wird die Länge der Liste abgefragt.
Wir können in for-loops variablen einsetzen (i)
Wir wollen das über eine range von values einsetzen. 
Print(i + 1) bedeutet, dass die erste Zahl (Python startet beim Zählen immer bei 0) mit 1 addiert wird. 
Dann wird die Liste in der Reihenfolge ausgegeben, mit Nummerierung.



Dictonary (dict)
Dictonaries bestehen auf Key : Value
Man erstellt ein dictionary (dict) mit geschwungenen Klammern {}
{} ist ein leeres Wörterbuch. 
Man kann dieses Wörterbuch füllen
Zum Beispiel:
{"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}

Die Namen werden jetzt den Häusern zugewiesen. 

Um es übersichtlicher darzustellen, kann man die Auflistungen auch in einem Absatz darstellen: 


students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }

Im nächsten Schritt kombinieren wir Listen und dictionaries: 

Mit [] erstellen wir Listen
Mit {} erstellen wir dictionaries
Wenn wir also [{}] kombinieren, koennen wir dictionieries in Listen verwalten. 

Mit dictioniaries bekommen wir eine Sammlung aus Key und Value Paaren und können sie in Listen verwalten.

Beispiel: 

students = [
    {"name": "Hermione", "house": "Gryffinor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

So können wir Daten sammeln und verwalten.



Zusammenfassung von ChatGPT:

CS50P – Lecture 2: Loops
Vollständige Zusammenfassung & Übersetzung für OneNote

Hauptthema der Lecture
In Lecture 2 geht es um:
Schleifen (Loops)
Loops erlauben Programmen:
    • Wiederholungen 
    • Automatisierungen 
    • strukturierte Abläufe 
ohne denselben Code ständig erneut schreiben zu müssen.

Warum sind Loops wichtig?
Ohne Loops müsste man Dinge mehrfach schreiben:

print("meow")
print("meow")
print("meow")
Das funktioniert,
aber:
    • ist ineffizient 
    • schlecht lesbar 
    • nicht skalierbar 

Die Lösung:
Loops

while Loops
Erste Schleife:

while

Beispiel

i = 0

while i < 3:
    print("meow")
    i += 1

Erklärung

i = 0
Counter / Zählvariable

while i < 3
Python prüft:

Ist i kleiner als 3?
Wenn TRUE:
    • Schleife läuft weiter 
Wenn FALSE:
    • Schleife stoppt 

i += 1
Bedeutet:

i = i + 1
Die Variable wird erhöht.

Infinite Loops (Endlosschleifen)

Beispiel

while True:
    print("meow")
Das stoppt niemals.

Ursache vieler Endlosschleifen
Man vergisst:

i += 1
Dann verändert sich die Bedingung nie.

for Loops
Python besitzt elegantere Schleifen:

for

Beispiel

for i in [0, 1, 2]:
    print("meow")

Erklärung
Python geht:
Element für Element
durch die Liste.

range()
Sehr wichtige Python-Funktion.

Beispiel

for i in range(3):
    print("meow")

range(3)
liefert intern:

0
1
2

Wichtig
Python zählt:
ab 0
und stoppt:
vor der letzten Zahl.

_ statt i
Wenn die Variable nicht benötigt wird:

for _ in range(3):
    print("meow")

Bedeutung von _
Signalisiert:
„Variable wird ignoriert.“
Sehr häufig in Python.

Eingaben mit Schleifen validieren
Loops können Eingaben kontrollieren.

Beispiel

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

Erklärung
Die Schleife läuft:
solange weiter,
bis eine gültige Eingabe erfolgt.

break

break
bedeutet:
Schleife sofort beenden.

Funktion + Schleife kombinieren

Beispiel

def main():
    number = get_number()
    meow(number)

Eigene Funktion

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

Wichtige Erkenntnis
Loops und Funktionen werden:
kombiniert.
Das ist professionelle Programmstruktur.

return innerhalb von Loops

return
verlässt:
    • die Funktion 
    • UND die Schleife 
sofort.

Listen (Lists)
Neue Datenstruktur.

Beispiel

students = ["Hermione", "Harry", "Ron"]

Zugriff auf Elemente

students[0]
↓

Hermione

Wichtig
Python beginnt:
bei Index 0

Listen durchlaufen

for student in students:
    print(student)

Erklärung
Python nimmt:
jedes Element
und speichert es temporär in:

student

Dictionaries
Sehr wichtiges Thema.

Aufbau

{
    key : value
}

Beispiel

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Draco": "Slytherin"
}

Zugriff auf Values

students["Harry"]
↓

Gryffindor

Dictionary Loops

for student in students:
    print(student)

Wichtig
Beim Loopen über Dictionaries:
iteriert Python über die KEYS.

Values holen

students[student]
bedeutet:
„Hole den Value zum aktuellen Key.“

Beispiel
Wenn:

student = "Harry"
Dann:

students[student]
↓

students["Harry"]
↓

Gryffindor

Mehrere Werte ausgeben

print(student, students[student], sep=", ")

sep=", "
Bestimmt:
das Trennzeichen.

Dictionaries in Listen
Sehr wichtiges Konzept.

Beispiel

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
]

Bedeutung
    • Liste enthält mehrere Dictionaries 
    • jedes Dictionary repräsentiert ein Objekt 

Zugriff

student["name"]
oder:

student["house"]

Verschachtelte Loops
Loops in Loops.

Beispiel Quadrat

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

Erklärung

Äußerer Loop

for i in range(size):
bestimmt:
die Reihen

Innerer Loop

for j in range(size):
bestimmt:
die Zeichen pro Reihe

end=""
Verhindert:
automatischen Zeilenumbruch

print()
Ohne Inhalt:
erzeugt nur Zeilenumbruch.

Ergebnis

###
###
###

len()
Sehr wichtige Funktion.

Bedeutung

len()
↓
Länge zählen

Beispiel

name = input("Name: ")

print(len(name))

len zählt
    • Buchstaben 
    • Leerzeichen 
    • Elemente 

Beispiel

len("Stefan")
↓

6

Kombination mit if

if len(name) < 3:
    print("Too short")

Wichtige Konzepte aus Lecture 2

Schleifen
    • while 
    • for 
    • range 
    • break 

Datenstrukturen
    • Listen 
    • Dictionaries 
    • Listen mit Dictionaries 

Datenzugriff

dictionary[key]

Verschachtelte Schleifen
Loops innerhalb anderer Loops.

Wiederholung vermeiden
Programme strukturieren.

Funktionen kombinieren
    • Loops 
    • return 
    • if 
    • input 
zusammen nutzen.

Was du nach Lecture 2 jetzt kannst
✅ while Loops
✅ for Loops
✅ range()
✅ break
✅ input validieren
✅ Listen erstellen
✅ Listen loopen
✅ Dictionaries erstellen
✅ Keys & Values verstehen
✅ Dictionaries in Listen kombinieren
✅ verschachtelte Loops
✅ einfache Muster drucken
✅ len() verwenden
✅ strukturierte Daten speichern
