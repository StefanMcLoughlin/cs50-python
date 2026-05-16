Exceptions

SyntaxError: 

SyntaxError müssen manuell vom Programmierer gefixt werden.

ValueError sind Fehlermeldungen, wenn der User etwas eingibt, was unser code nicht verarbeiten kann.
Beispielsweise, wenn wir ein Interger (int) abfragen aber der User z.B. cat schreibt. 
Ziel ist es den Code so aufzubauen, das er in der Defensive bereits diesen Fehlern vorbeugt.



Die Lösung für genau diese Defensive Code Schreibweise ist: 
Try: und except:

Beispiel:

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an interger")


Es wird nun versucht (try:) den Code laufen zu lassen, es sei denn es trifft die Ausnahme ein (except:),
dass es ein ValueError ist, dann bekommt der User den Hinweis.

Nun wird ein NameError ausgegeben, der besagt das x nicht definiert ist. Das liegt daran, dass der Code egal wie alle Zeilen durch geht. Um diesen Fehler zu umgehen, kann die else: Funktion genutzt werden, um die Zeile explizit zu machen.


try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an interger")
else:
    print(f"x is {x}")



Um den Code jetzt user freundlich zu machen, können wir einen Loop einbauen. 

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an interger")
    else:
        break
print(f"x is {x}")

While True: ist der infinite Loop, bis ein Integer eingegeben wurde.

Wir koennen den Code jetzt noch als eigene Funktion definieren: 

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an interger")
        else:
            return x    
main()


Jetzt ist get_int als eigene Funktion definiert und returned value x.

Pass
Damit wir nicht immer wieder die gleiche Fehlermeldung an den User ausspielen, können wir stattdessen auch einfach pass einsetzen. Der User wird dann einfach nur um erneute Eingabe gebeten, ohne Grund.

Beispiel:

def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
main()



Um das Thema abzuschließen können wir den Code noch dynamischer gestalten. 
Anstatt die variable in der selbst erstellten Funktion vorzugeben, können wir sie ersetzen und im Main Code die Frage stellen:

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()




Zusammenfassung von Chat GPT:

CS50P – Lecture 3: Exceptions
Vollständige Zusammenfassung & Übersetzung für OneNote

Hauptthema der Lecture
In Lecture 3 geht es um:
Exceptions (Fehlerbehandlung)
Python-Programme sollen:
    • nicht abstürzen 
    • Fehler erkennen 
    • sinnvoll reagieren 

Was sind Exceptions?
Eine Exception ist:
ein Fehler während der Programmausführung.

Beispiel

x = int(input("What's x? "))
print(x)
Wenn der User eingibt:

cat
entsteht ein Fehler.

Fehlermeldung

ValueError: invalid literal for int()

Bedeutung
Python kann:
"cat"
nicht in eine Zahl umwandeln.

Problem ohne Fehlerbehandlung
Das komplette Programm:
stoppt sofort.

Lösung:
try / except

Grundstruktur

try:
    ...
except:
    ...

Beispiel

try:
    x = int(input("What's x? "))
    print(x)
except ValueError:
    print("x is not an integer")

Erklärung

try
Python versucht:
diesen Code auszuführen.

except
Wenn ein Fehler entsteht:
springt Python hierhin.

Vorteil
Das Programm:
crasht nicht mehr.

ValueError
Ein sehr häufiger Fehler.

Entsteht wenn:
Datentypen nicht passen.

Beispiel

int("hello")
↓

ValueError

NameError

Beispiel

print(x)
ohne vorher:

x = ...

Ergebnis

NameError

ZeroDivisionError

Beispiel

10 / 0
↓

ZeroDivisionError

Mehrere Exceptions behandeln

Beispiel

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

Sehr wichtig
Python prüft:
except-Blöcke von oben nach unten.

Bare except

Beispiel

except:
Fängt:
ALLE Fehler ab.

Problem
Zu allgemein.
Man erkennt:
    • Ursache nicht mehr 
    • Debugging wird schwer 

Best Practice
Lieber:

except ValueError:
statt:

except:

else

Aufbau

try:
    ...
except:
    ...
else:
    ...

Bedeutung
else läuft:
nur wenn KEIN Fehler entstanden ist.

Beispiel

try:
    x = int(input("What's x? "))

except ValueError:
    print("x is not an integer")

else:
    print(f"x is {x}")

Vorteil
Sauberere Struktur.

while + try kombinieren
Sehr wichtiges Muster.

Beispiel

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

Erklärung
Das Programm fragt:
so lange erneut,
bis gültige Eingabe erfolgt.

break

break
↓
beendet die Schleife sofort.

Eigene Funktion für Validierung

Beispiel

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

Vorteil
Code wird:
    • wiederverwendbar 
    • sauber 
    • professioneller 

return in try
Sehr wichtig.

Beispiel

return int(input("What's x? "))
Wenn kein Fehler entsteht:
Funktion endet sofort.

pass

Beispiel

except ValueError:
    pass

Bedeutung

pass
↓
"Ignoriere den Fehler."

Beispiel komplett

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

Verhalten
Wenn Fehler:
    • nichts anzeigen 
    • einfach erneut fragen 

KeyboardInterrupt

Beispiel
User drückt:

CTRL + C

Ergebnis

KeyboardInterrupt

Python erkennt:
User möchte Programm abbrechen.

Runtime Errors
Lecture 3 unterscheidet:

Syntax Errors
Fehler im Code selbst.
Beispiel:

if x = 5

Runtime Errors
Fehler:
während das Programm läuft.
Beispiel:

int("hello")

Wichtiges Konzept
Programme sollen:
robust sein.

Gute Programme:
    • validieren Eingaben 
    • behandeln Fehler 
    • verhindern Abstürze 

Typische Fehlerquellen

Falscher Datentyp

int("cat")

Division durch 0

10 / 0

Nicht definierte Variablen

print(name)

Gute Programmstruktur
Lecture 3 zeigt erneut:

Kombination aus:
    • Funktionen 
    • Loops 
    • try 
    • except 
    • return 
    • break 

Das ist wichtig,
weil echte Programme:
ständig Fehler behandeln müssen.

Praktisches Muster aus Lecture 3

User-Input absichern

def get_number():
    while True:
        try:
            return int(input("Number: "))
        except ValueError:
            print("Invalid number")

Das ist professioneller Code.

Wichtigste Erkenntnisse aus Lecture 3

Exceptions
Fehler während der Laufzeit.

try
Versucht Code auszuführen.

except
Reagiert auf Fehler.

else
Läuft nur ohne Fehler.

pass
Ignoriert Fehler.

break
Beendet Schleifen.

while True
Endlosschleife für Input-Validierung.

return
Verlässt Funktion sofort.

Best Practices aus Lecture 3
✅ Fehler gezielt behandeln
✅ Keine unnötigen Abstürze
✅ Eingaben validieren
✅ Funktionen wiederverwenden
✅ while + try kombinieren
✅ spezifische Exceptions nutzen

Was du nach Lecture 3 jetzt kannst
✅ Runtime Errors verstehen
✅ try / except nutzen
✅ ValueError behandeln
✅ ZeroDivisionError behandeln
✅ NameError verstehen
✅ else verwenden
✅ pass verstehen
✅ User-Input absichern
✅ robuste Programme schreiben
✅ Fehlerfreie Eingaben erzwingen
✅ professionelle Input-Validierung bauen
