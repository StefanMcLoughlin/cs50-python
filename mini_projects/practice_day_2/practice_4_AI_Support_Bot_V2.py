"""
Übung 4 — AI Support Bot V2
Aufgabe:

Der Bot soll mehrere Keywords erkennen.

Beispiele:

"api"
"json"
"python"
"error"
"login"

Wenn mehrere Keywords vorkommen:
→ passende Antwort geben

Beispiel:

Input:

my api has json error

Output:

Prüfe die JSON Response
Bonus:

Baue:

while True:

damit der Bot dauerhaft läuft.

Und:

exit

beendet den Bot.
"""


def main():
    support_bot()

def support_bot():
    while True:
        task = input("Wie kann ich dir weiterhelfen? ").lower()

        if task == "exit":
            print("Bot beendet")
            break

        elif "api" in task :
           print("Pruefe die JSON response")
        elif "json" in task :
            print("Prüfe, ob die JSON-Daten gültig sind und ob die gesuchten Keys existieren")
        elif "python" in task :
            print("Ueberpruefe die einrueckung")
        elif "error" in task :
            print("Aktuell liegt leider ein Systemfehler vor, probiere es spaeter noch einmal")
        elif "login" in task :
            print("Bitte Benutzernamen und Passwort kontrollieren")
        else:
            print("Diese Fehlermeldung ist mir leider nicht bekannt")

main()