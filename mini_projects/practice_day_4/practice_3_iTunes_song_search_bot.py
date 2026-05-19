"""
Übung 3 — iTunes Song Search Bot
Schwierigkeitsgrad: Mittel
Ziel

Wiederhole:

requests
APIs
JSON
Loops
Dictionaries
Aufgabe

Nutze die iTunes API.

Der User soll einen Künstler eingeben:

Künstler:

Dann soll das Programm:

mehrere Songs laden
Songnamen ausgeben
Anforderungen
Nutze:
requests.get()
Nutze:
response.json()
Die Ausgabe soll ungefähr so aussehen:
1. Lose Yourself
2. Mockingbird
3. Without Me
Bonus Challenge

Lass den User auswählen:

Wie viele Songs anzeigen?
Sehr wichtig

Versuche:

selbst herauszufinden
wo die Songnamen im JSON liegen

Das ist EXTREM gutes Training.
"""


import requests
import json

def main():
    song_request()

   
        

def song_request():

    term = input("Künstler: ").strip().title()
    limit = input("Anzahl der songs: ")
    link = f"https://itunes.apple.com/search?entity=song&limit={limit}&term={term}"
    
    response = requests.get(link)

    o = response.json()
    for result in o["results"]:
        print(result["trackName"])

    

main()