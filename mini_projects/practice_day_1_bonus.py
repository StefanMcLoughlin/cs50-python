# Bonus Aufgabe: Schreibe eine kleine Funktion
# Die Funktion soll den Namen fragen, den Namen ausgeben und "Willkommen" schreiben.
def main():
    begruessung()

def begruessung():
    name = input("Wie heisst Du? ").strip().title()
    print(f"Willkommen {name}")

main()