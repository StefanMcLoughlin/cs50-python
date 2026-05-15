Conditionals - Bedingungen

Mithilfe von Bedingungen wird Code intelligent!

Symbole in Python

> greater then
>= greater then or equal to
< less then
<= less then or equal to
== equality / one = means assignment from the right to the left
!= not equal to

If Funktionen.


x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")




Das ist die Logik hinter der Funktion

Das Ergebnis ist zwar richtig aber der Code ist nicht gut designed weil das Programm immer wieder if Fragen muss. Das Programm fragt jedes Mal alle drei if Fragen ab.

Das heißt der Code sollte so angepasst werden, sobald die richtige Antwort erscheint, frag nicht mehr weiter.

Das erreichen wir mit else if Funktionen (elif)


x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print("x is less than y")
elif x > y:

    print("x is greater than y")
elif x == y:
    print("x is equal to y")

Das ist die Logik hinter dieser Funktion

Bei kleinen Programmen wie diesem, merkt man in der Ausführung keinen Unterschied. 
Wenn man jedoch riesige Codes hat, dann sind solche Verbesserungen sehr wichtig, damit 
Der Code schneller und besser läuft und weniger Energie verbraucht.

In diesem Szenario fragen wir ist x größer als y oder ist x kleiner als y. Logischerweise brauchen wir am Ende nicht mehr Fragen, ob x = y ist, denn wenn es nicht größer oder kleiner ist, dann kann es nur gleich sein.

Dafür können wir else nutzen. 

Das macht den Code nochmal smoother.



x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

Das ist die Logik hinter dieser Funktion

If und or Funktion 


x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")


Das ist die Logik hinter dieser Funktion

Wichtig sind die Schritte kurz, logisch und einfach zu gestalten. 
Diese komplette Vorgehensweise kann noch weiter verkürzt und verbessert werden. 


x = int(input("What's x? "))
y = int(input("What's y? "))
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


Das ist die Logik hinter dieser Funktion

Boolean expressions / Boolean Werte
Mithilfe von boolean Werten kann man Bedigungen erzeugen.

Bool can only be True or False
Bool ist eine weitere Vokabel die wichtig fuer Funktionen ist. 
Denn den Wert, den bool ausgeben kann ist nur wahr oder falsch. 


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()

Pythonic ist ein Begriff, der von Python Programmierern benutzt wird, um einen Code simpler in Python darzustellen. 

Ergebnis: 

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
main()


Es geht nicht nur darum richtigen Code zu schreiben, sondern immer besseren Code zu schreiben.
Wenn die Antwort der boolian expression, nur True oder False sein kann, wieso sollte man dann überhaupt fragen?
Man braucht nicht if oder else Fragen, einfach nur return.

Man kann den Code also noch besser gestalten:

Ergebnis: 


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return (n % 2 == 0)
main()






Match: 

name = input("What's your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")

Abfrage, ob die Namen passen anstatt alle mit if, elif und else abzufragen.

Auch hier kann man den Code nochmal verfeinern und zusammenfassen mit | , was als or Befehl gilt. 

Ergebnis: 


name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")




Zusammenfassung von Chat GPT:

CS50P – Lecture 1: Conditionals

Komplette Zusammenfassung auf Deutsch
Jetzt lernt man, wie Programme Entscheidungen treffen.

Das Thema heißt:
Conditionals (Bedingungen)
Damit wird Code „intelligent“. 

1. Was sind Conditionals?
Conditionals erlauben Programmen:

Wenn etwas passiert → mache A
Sonst → mache B
Ohne Conditionals wären Programme:
nur starre Befehlslisten.
Mit Conditionals können Programme:
    • reagieren 
    • vergleichen 
    • Entscheidungen treffen 
    • Logik ausführen 
Das ist die Grundlage fast aller Software. 

2. Vergleichsoperatoren
Python besitzt Operatoren zum Vergleichen.

Gleich

==
Beispiel:

x == y

Ungleich

!=

Größer / Kleiner

>
<
>=
<=

Wichtig:
= ist NICHT ==

=
weist einen Wert zu.

x = 5

==
vergleicht Werte.

x == 5
Das ist extrem wichtig. 

3. if
Die erste echte Bedingung.

if x < y:
    print("x is less than y")

Was passiert?
Python prüft:

x < y
Wenn TRUE:
→ Code wird ausgeführt.
Wenn FALSE:
→ wird übersprungen.

4. Boolean Werte
Bedingungen erzeugen:

True
False
Das nennt man:
Boolean / bool
Beispiele:

5 > 3
Ergebnis:

True


5 < 3
Ergebnis:

False

5. Einrückungen (Indentation)
Sehr wichtig in Python.

Richtig

if x < y:
    print("Hallo")

Falsch

if x < y:
print("Hallo")
Dann kommt:

IndentationError
Python benutzt Einrückungen,
um Codeblöcke zu erkennen.

6. Mehrere if Statements

if x < y:
    print("x kleiner")

if x > y:
    print("x größer")

if x == y:
    print("gleich")
Python prüft:
jede Bedingung einzeln.
Das nennt man:
Control Flow


7. elif
elif bedeutet:
else if
sonst wenn

Beispiel

if x < y:
    print("kleiner")

elif x > y:
    print("größer")

else:
    print("gleich")

Vorteil
Python stoppt,
sobald eine Bedingung TRUE ist.
Das macht Code:
    • effizienter 
    • lesbarer 
    • schneller 


8. else
else ist:
der Standardfall.
Wenn nichts anderes zutrifft:

else:

9. or
or bedeutet:
mindestens eine Bedingung muss wahr sein.

Beispiel

if x < y or x > y:
Das ist TRUE wenn:
    • x kleiner ist
ODER 
    • x größer ist 

10. and
and bedeutet:
beide Bedingungen müssen wahr sein.

Beispiel

if score >= 90 and score <= 100:

Pythonische Schreibweise
Python erlaubt kürzere Schreibweise:

if 90 <= score <= 100:
Das nennt man:
Pythonic Code
also:
saubere Python-Schreibweise.


11. Vereinfachung von Code
CS50 zeigt oft:
Guter Code stellt möglichst wenige Fragen.

Schlechter

if x < y or x > y:

Besser

if x != y:
Denn:
eine Bedingung reicht.

12. Grade System
CS50 baut ein Notensystem.

Beispiel

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

else:
    print("F")

Wichtiges Prinzip
Python prüft:
von oben nach unten.
Darum ist Reihenfolge extrem wichtig.

13. Modulo %
Sehr wichtiges neues Konzept.

%
gibt den:
Rest einer Division
zurück.

Beispiele

4 % 2
Ergebnis:

0


5 % 2
Ergebnis:

1

14. Gerade / Ungerade prüfen

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

Warum funktioniert das?
Gerade Zahlen:

Rest = 0
Ungerade:

Rest = 1

15. Eigene Funktionen mit Boolean
Sehr wichtiger Teil der Lecture.

Beispiel

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

Noch bessere Version

def is_even(n):
    return n % 2 == 0
Denn:

n % 2 == 0
ist bereits:
    • True
ODER 
    • False 


16. match
Eine modernere Alternative zu vielen if Statements.

Beispiel

match name:
    case "Harry":
        print("Gryffindor")

    case "Draco":
        print("Slytherin")

    case _:
        print("Who?")

_
bedeutet:
alles andere
ähnlich wie:

else

17. Mehrere Werte mit |

case "Harry" | "Hermione" | "Ron":
Das bedeutet:
oder

18. Der wichtigste Gedanke der Lecture
Lecture 1 zeigt:
Guter Code ist einfacher Code.
Nicht:
    • kompliziert 
    • unnötig lang 
    • doppelt 
Sondern:
    • lesbar 
    • logisch 
    • effizient 

Was du nach Lecture 1 gelernt hast
Du kannst jetzt:
✅ Bedingungen schreiben
✅ Vergleiche durchführen
✅ if / elif / else nutzen
✅ Boolean Werte verstehen
✅ or / and / not verwenden
✅ Modulo % verstehen
✅ gerade und ungerade Zahlen prüfen
✅ eigene bool Funktionen bauen
✅ Pythonic Code schreiben
✅ match/case verwenden
✅ Kontrollfluss verstehen

