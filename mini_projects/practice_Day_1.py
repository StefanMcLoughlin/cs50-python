# Uebung 5 - AI Assistent Simulation
# Fragestellung: Frage den Benutzer: Welches Problem hast Du? Wenn "API"-> "Pruefe JSON response", wenn "Python" -> "Ueberpruefe einrueckung", wenn "Login" -> "Pruefe Benutzernamen und Passwort", sonst -> "Unbekannter Fehler"

problem = input("Welches Problem hast Du? ").lower()
if "api" in problem:
    print("Prüfe die JSON response")
elif "python" in problem :
    print("Überprüfe die Einrückung")
elif "login" in problem:
    print("Prüfe Benutzernamen und Passwort")
else:
    print("Unbekannter Fehler")