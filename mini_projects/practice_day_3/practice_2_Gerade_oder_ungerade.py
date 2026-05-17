"""
Übung 2 — Gerade oder Ungerade
Schwierigkeitsgrad: Mittel
Ziel

Nutze:

def
return
if
else
%
while
try/except
Aufgabe

Baue ein Programm:

Der User gibt eine Zahl ein.
Das Programm prüft:
x % 2
Gib aus:
"Gerade Zahl"
"Ungerade Zahl"
Falls keine Zahl eingegeben wird:
Ungültige Eingabe
Das Programm soll sich danach erneut starten.
Extra Challenge

Frage zusätzlich:

Nochmal prüfen? (ja/nein)
Beispiel
Zahl: 4
Gerade Zahl

Nochmal prüfen? ja

Zahl: 7
Ungerade Zahl
Ziel dieser Übung

Du kombinierst:

Loops
Bedingungen
Fehlerbehandlung
eigene Funktionen

zu einem echten kleinen Programm.
"""

def main():

    while True:
        x = get_number("Bitte eine Zahl eingeben: ")

        if is_even(x):
            print("Gerade Zahl")
        else:
            print("Ungerade Zahl")
    
        i = input("Nochmal prüfen? ")
        if i == "nein":
            break

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Bitte eine gültige Zahl eingeben! ")

def is_even(n):
    return (n % 2 == 0)


main()