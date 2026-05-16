"""
Übung 3 — Trading Journal Mini-Version
Aufgabe:

Frage:

Anzahl Gewinntrades
Anzahl Verlusttrades

Berechne:

Gesamtanzahl
Gewinnquote in %
Beispiel:
Gewinntrades: 7
Verlusttrades: 3

Gewinnquote: 70%
Bonus:

Wenn Gewinnquote > 60:
→ „Starke Strategie“
"""

gewinntrades = int(input("Anzahl Gewinntrades: "))
verlusttrades = int(input("Anzahl Verlusttrades: "))

gesamtanzahl = gewinntrades + verlusttrades
print(f"Gesamtanzahl Trades: {gesamtanzahl}")

gewinnquote = gewinntrades / gesamtanzahl * 100
print(f"Gewinnquote: {gewinnquote:.2f} % ")

if gewinnquote >60:
    print("Starke Strategie")