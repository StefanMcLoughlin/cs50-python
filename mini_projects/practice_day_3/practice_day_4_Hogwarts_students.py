"""
Übung 1 — Anfänger bis Mittel
Hogwarts Studenten-System

Baue ein kleines System mit:

einer Liste
mehreren Dictionaries
Ziel

Speichere mehrere Schüler.

Jeder Schüler soll haben:

Name
Haus
Patronus
Beispiel-Struktur

(NICHT komplett kopieren — nur Orientierung)

students = [
    {"name": "...", "house": "...", "patronus": "..."},
]
Deine Aufgabe
1.

Erstelle mindestens:

3 Schüler
2.

Nutze eine Schleife:

for student in students:
3.

Gib schön formatiert aus:

Beispiel:

Name: Harry | House: Gryffindor | Patronus: Stag
Zusatzaufgabe (wichtiger Teil)

Falls Patronus None ist:

statt:

Patronus: None

soll stehen:

Patronus: Unknown
Was du dabei trainierst

Du kombinierst jetzt:

Listen
Dictionaries
Schleifen
Bedingungen
Key-Zugriffe
Datenstrukturen

Das ist ein großer Schritt.

Bonus-Challenge (wenn du fertig bist)

Lass den Benutzer neue Schüler hinzufügen mit:

input()

und speichere sie in der Liste.
"""

students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "stud"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "Unknown"},
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" | ")
