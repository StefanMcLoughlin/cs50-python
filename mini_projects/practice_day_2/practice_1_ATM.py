"""
Aufgabe 1 - ATM - Bankautomat

Aufgabe:

Frage den Benutzer:

Kontostand
gewünschte Auszahlung

Wenn:

Auszahlung größer als Kontostand
→ „Nicht genügend Guthaben“

Sonst:

neuen Kontostand ausgeben
Bonus:

Wenn Kontostand genau 0:
→ „Konto leer“
"""

def main():

    kontostand = int(input("Aktueller Kontostand? "))
    auszahlung = int(input("Wie hoch ist der gewuenschte Auszahlungbetrag? "))

    if kontostand < auszahlung:
        print("Nicht genuegend Guthaben! ")

    else:
        neuer_kontostand = kontostand_neu(kontostand, auszahlung)
        if neuer_kontostand == 0:
            print("Konto leer")

        else:
            print(f"Neuer Kontostand: {neuer_kontostand}")


def kontostand_neu(kontostand, auszahlung):
    n = kontostand - auszahlung
    return n

main()
