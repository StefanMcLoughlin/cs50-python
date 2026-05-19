"""
Übung 1 — Coinflip Generator
Schwierigkeitsgrad: Leicht
Ziel

Wiederhole:

import
random
Funktionen
choice()
Aufgabe

Erstelle ein Programm:

Kopf

oder

Zahl

zufällig ausgibt.

Anforderungen
Nutze:
from random import choice
Bonus

Lass das Programm:

5 Mal werfen
mit einem Loop
Ziel der Übung

Verstehen:

wie Libraries benutzt werden
wie import funktioniert
wie Funktionen aus Libraries genutzt werden
"""

from random import choice

def main():

    i = 0
    while i < 5:
        coinflip()
        i = i + 1

def coinflip():
    coin = choice(["Kopf", "Zahl"])
    print(coin)

main()