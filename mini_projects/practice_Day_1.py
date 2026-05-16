# Uebung 5 - AI Assistent Simulation
# Fragestellung: Frage den Benutzer: Welches Problem hast Du? Wenn "API"-> "Pruefe JSON response", wenn "Python" -> "Ueberpruefe einrueckung", wenn "Login" -> "Pruefe Benutzernamen und Passwort", sonst -> "Unbekannter Fehler"

problem = input("Welches Problem hast Du? ").lower()
if problem == "api":
    print("Prüfe die JSON response")
elif problem == "python":
    print("Überprüfe die Einrückung")
elif problem == "login":
    print("Prüfe Benutzernamen und Passwort")
else:
    print("Unbekannter Fehler")