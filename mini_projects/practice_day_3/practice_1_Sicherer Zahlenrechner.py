"""
Übung 1 — Sicherer Zahlenrechner
Schwierigkeitsgrad: Einfach
Ziel

Du sollst:

try
except
while
int()
return
Funktionen

kombinieren.

Aufgabe

Erstelle ein Programm:

Frage den User nach zwei Zahlen.
Nutze eine eigene Funktion:
def get_number():
Falls der User keine Zahl eingibt:
Bitte eine gültige Zahl eingeben
Addiere beide Zahlen.
Gib das Ergebnis aus.
Beispiel
Was ist x? hello
Bitte eine gültige Zahl eingeben

Was ist x? 5
Was ist y? 3

Ergebnis: 8
Ziel dieser Übung

Du trainierst:

Fehlerbehandlung
Wiederverwendbare Funktionen
Input-Validierung
"""

def main():

    x = get_number("What's x? ")
    y = get_number("What's y? ")
    z = x + y

    print(f"Ergebnis: {z}")

def get_number(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
            print("Bitte eine gültige Zahl eingeben! ")
            
main()