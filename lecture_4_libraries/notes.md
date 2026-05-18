Was sind Libraries?
Libraries sind fertige Code-Sammlungen.
Sie enthalten:
	• Funktionen 
	• Klassen 
	• Werkzeuge 
	• vorgefertigte Lösungen 
Dadurch muss man viele Dinge nicht selbst programmieren.

Warum sind Libraries wichtig?
Libraries:
	• sparen Zeit 
	• machen Programme leistungsfähiger 
	• lösen komplexe Probleme einfacher 
Fast alle professionellen Python-Projekte benutzen Libraries.

Importieren von Libraries
Ganze Library importieren

import random
Dann benutzt man:

random.randint(1, 10)

Bestimmte Funktion importieren

from random import randint
Dann braucht man nicht mehr:

random.randint()
sondern nur:

randint(1, 10)

Eigene Erklärung

import lädt eine externe Datei oder Library,
damit man deren Funktionen benutzen kann.

Das random Modul
Das random Modul erzeugt Zufallswerte.

randint()

from random import randint

print(randint(1, 10))
Erzeugt eine Zufallszahl zwischen:
	• 1 
	• und 10 
inklusive beider Zahlen.

choice()

from random import choice

coin = choice(["Kopf", "Zahl"])
print(coin)
Wählt zufällig ein Element aus einer Liste.

shuffle()

from random import shuffle

cards = ["Ass", "König", "Dame"]

shuffle(cards)

print(cards)
Mischt eine Liste zufällig.

statistics Library
Mit statistics kann man mathematische Berechnungen machen.

average / mean

from statistics import mean

print(mean([100, 90, 80]))
Berechnet den Durchschnitt.

sys Library
Die sys Library gibt Zugriff auf:
	• das Betriebssystem 
	• Python-Systemfunktionen 
	• Command-Line Arguments 

sys.argv

import sys

print(sys.argv)
sys.argv ist eine Liste aller Argumente,
die beim Start des Programms eingegeben wurden.

Beispiel

python hello.py Stefan
Dann enthält:

sys.argv
Folgendes:

['hello.py', 'Stefan']

Wichtig verstehen
sys.argv[0]
Dateiname
sys.argv[1]
erstes echtes Argument

len(sys.argv)

if len(sys.argv) != 2:
    sys.exit()
Prüft:
	• wie viele Argumente eingegeben wurden 

sys.exit()

sys.exit()
Beendet das Programm sofort.

APIs
API bedeutet:

Application Programming Interface
Eine API erlaubt Programmen,
mit anderen Systemen zu kommunizieren.

requests Library
Mit requests kann Python:
	• Webseiten anfragen 
	• APIs nutzen 
	• Daten aus dem Internet holen 

Installation mit pip

pip install requests
pip installiert externe Python-Packages.

HTTP GET Anfrage

import requests

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=eminem")
Python sendet eine Anfrage an die iTunes API.

JSON
Viele APIs schicken Daten als JSON zurück.
JSON sieht ähnlich aus wie Dictionaries.

response.json()

response.json()
wandelt JSON Daten in Python Daten um.

json.dumps()

import json

print(json.dumps(response.json(), indent=2))
Macht JSON schön lesbar.

indent=2
Fügt:
	• Einrückungen 
	• Zeilenumbrüche 
	• Struktur 
hinzu.

pycache
Python erstellt automatisch:

__pycache__
Darin speichert Python:
	• kompilierten Bytecode 
	• .pyc Dateien 
Dadurch starten Programme schneller.

Eigene Modules / Libraries
Man kann eigene Python-Dateien importieren.

Beispiel
sayings.py

def hello(name):
    print("hello,", name)

main.py

from sayings import hello

hello("Stefan")

Sehr wichtig verstehen
Jede .py Datei kann:
	• ein Programm 
	• ODER ein Modul sein 

Eigene Erklärung

Python Dateien können wie Libraries benutzt werden.
Mit import kann man Funktionen aus anderen Dateien laden.

Vorteile von Libraries
Libraries machen Code:
	• sauberer 
	• kürzer 
	• professioneller 
	• wiederverwendbar 

Wichtige Begriffe aus Lecture 4
Begriff	Bedeutung
Library	Fertige Codesammlung
import	Library laden
module	Einzelne Python-Datei
pip	Package Installer
API	Verbindung zwischen Programmen
JSON	Datenformat
sys.argv	Terminal Argumente
requests	HTTP Anfragen senden
pycache	Python Bytecode Speicher

Sehr wichtige Erkenntnis aus Lecture 4

Man muss nicht alles selbst programmieren.
Professionelle Entwickler benutzen ständig Libraries,
APIs und externe Module.

Eigene Gesamtzusammenfassung

Lecture 4 erklärt, wie Python externe Libraries,
APIs und eigene Module benutzt.

Mit import können fertige Funktionen geladen werden.
Mit pip installiert man neue Libraries.
Mit requests kann Python Daten aus dem Internet holen.
Mit sys.argv können Argumente über das Terminal übergeben werden.
Python kann außerdem eigene Dateien als Module importieren.
