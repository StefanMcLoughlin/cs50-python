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
    artist = get_term()
    amount = get_limit()
    link = build_url(artist, amount)
    data = get_data(link)
    print_songs(data)
    
def get_term():
    artist = input("Künstler: ").strip().title()
    return artist 

def get_limit():
    amount = int(input("Anzahl der songs: "))
    return amount

def build_url(artist, amount):
    link = f"https://itunes.apple.com/search?entity=song&limit={amount}&term={artist}"
    return link

def get_data(link):
    response = requests.get(link)
    data = response.json()
    return data

def print_songs(data):
    for result in data["results"]:
        print(result["trackName"])


main()