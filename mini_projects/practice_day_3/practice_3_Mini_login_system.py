"""
Übung 3 — Mini Login System
Schwierigkeitsgrad: Anspruchsvoll
Ziel

Fast alles kombinieren, was du bisher gelernt hast.

Aufgabe

Erstelle ein Login-System:

Anforderungen
1. Benutzername abfragen
Benutzername:
2. Passwort abfragen
Passwort:
3. Richtige Daten

Nutze feste Daten:

username = "stefan"
password = "python123"
4. Ausgabe

Wenn korrekt:

Login erfolgreich

Wenn falsch:

Falsche Zugangsdaten
5. Maximal 3 Versuche

Nach 3 falschen Eingaben:

Zu viele Fehlversuche
Extra Challenge

Nutze:

eine Funktion für den Login
einen Counter
while
break
Beispiel
Benutzername: stefan
Passwort: test

Falsche Zugangsdaten

Benutzername: stefan
Passwort: python123

Login erfolgreich
"""


i = 0

while i < 3:
    username = input("Bitte Benutzernamen eingeben: ")
    password = input("Bitte Passwort eingeben: ")
    if username == "stefan" and password == "python123":
        print("Login erfolgreich")
        break
    else:
        print("Falsche Zugangsdaten")
        i += 1

if i == 3:
    print("Zu viele Fehlversuche")