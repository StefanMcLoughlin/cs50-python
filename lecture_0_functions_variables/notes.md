Functions and Variables

- Funktionen (Function) führen Aufgaben aus
z.B. Print → Text auf dem Bildschirm anzeigen.
- Ein String ist ein Text, Strings sind Textdaten
- Python Interpretiert, es liest den Code Zeile für Zeile und führt ihn aus. 
- Ein Argument ist eine Information, die man einer Funktion gibt.
- Manche Funktionen erzeugen Nebenwirkungen diese nennt man Side Effects 
- Debugging ist das beheben von Fehlern

Mit # kann man Kommentare schreiben. 
Diese sind für Menschen und werden vom Computer ignoriert. 

Damit das Programm mit dem Nutzer interagieren kann nutzt man
Input()
Beispiel: Input(“What’s your name? “)
Erklärung: Das Programm zeigt die Frage an und wartet auf Antwort. 

Variablen:
Variablen sind Speicherplätze für Daten (Ist wie eine beschriftete Box: Container)
name = input("What’s your name? “)

name ist eine variable. 

Strings können manipuliert werden. 

Spaces können entfernt werden mit folgendem code:
name = name.strip()

Namen können dazu gezwungen werden, Gross geschrieben zu werden 
name = name.title()

Es kann auch zusammengefasst werden: 
name = name.strip().title()

Method Chaining: Der Code kann noch weiter zusammengefasst werden (Mehrere Funktionen hintereinander:
name = input("What's your name? ").strip().title()

Um z.B. Vornamen und Nachnamen zu separieren, kann man die Funktion split() verwenden.
Split users name into first name and last name: 
First, last = name.split(" ")
print(f"hello, {first}")





Thema	Bedeutung
input()	Benutzereingaben
Variablen	Daten speichern
Strings	Textdaten
Datentypen	Arten von Daten
Rückgabewerte	Funktionen liefern Werte
Kommentare	Notizen
Methoden	Daten verändern
Chaining	Funktionen kombinieren

Integer int()
Integer sind ganze Zahlen, von negativ unendlich bis positiv unendlich. (Keine Kommazahlen!)
Diese Funktion wandelt einen Wert (Text) in eine Zahl um. 
Python kann nicht mit Text rechnen, daher ist es wichtig das die Strings in Zahlen (Integer) umgewandelt werden. 

X = input("Was ist x? ")
Y = input("Was ist y? ")
Z = int(x) + int(y)
Print(z)

Die Variable Z ist nicht notwendig. Sie kann ersetzt werden:

X = int(input("Was ist x? "))
Y = int(input("Was ist y? "))
Print(x + y)

Wie in Mathe, werden die Klammern von innen nach außen gelesen.

Für Kommazahlen wird float() verwendet.
X = float(input("Was ist x? "))
Y = float(input("Was ist y? "))
Print(x + y)

Formatieren von Strings: 
Mithilfe des F-Strings können die Tausender-Trennstellen angegeben werden (1.000 anstatt 1000)

x = float(input("Was ist x? "))
y = float(input("Was ist y? "))
z = x + y
print(f"{z:,}")
999 + 1 = 1,000 


Def = Define 
Eigene Funktionen definieren. Der Grund für eigene Funktionen ist, dass man sich nicht ständig wiederholen muss.
Funktionen müssen definiert werden, bevor sie im Code ausgeführt werden, da das Programm Zeile für Zeile liest. Allerdings kann das schnell die Logik des Codes zerstören. Um das zu umgehen gibt es folgende Methode: def main (): (Am Start vom Code, um den Main Code zu bestimmen)

Main() (Am Ende des Codes) 

Funktionen in Python
def = define
Mit def erstellt man eigene Funktionen.
Funktionen helfen dabei:
	• Code zu strukturieren 
	• Wiederholungen zu vermeiden 
	• Programme übersichtlicher zu machen 
	• denselben Code mehrfach zu verwenden 

Beispiel

def hallo():
    print("Hallo")
Hier wurde eine eigene Funktion namens hallo() definiert.

Funktionen ausführen
Eine Funktion wird erst ausgeführt, wenn sie aufgerufen wird:

hallo()

Wichtig zu verstehen
Python liest den Code:
von oben nach unten
Deshalb muss eine Funktion:
zuerst definiert werden,
bevor sie verwendet werden kann.

Problem bei großen Programmen
Wenn der gesamte Hauptcode oben steht, kann das Programm:
	• unübersichtlich werden 
	• schwer lesbar sein 
	• chaotisch wirken 

Lösung: main()
Deshalb verwenden Entwickler oft eine Hauptfunktion:

def main():
    print("Hallo Welt")

Warum main()?
main() enthält:
den Hauptablauf des Programms
Dadurch:
	• bleibt der Code sauber 
	• Funktionen können oben definiert werden 
	• die Programmlogik bleibt übersichtlich 

Typischer Aufbau

def hallo():
    print("Hallo")


def main():
    hallo()


main()

Ablauf des Programms
	1. Python liest die Funktionen 
	2. Funktionen werden gespeichert 
	3. main() wird aufgerufen 
	4. Das eigentliche Programm startet 

Wichtig
main() ist keine besondere Python-Funktion.
Es ist einfach:
eine Entwickler-Konvention
Fast alle größeren Programme nutzen dieses Prinzip.

Return: Return ist ein wichtiger Bestandteil im Code, denn es wird ein Wert zurück gegeben.

print()
zeigt etwas an
return
gibt einen Wert zurück, damit du ihn weiterverwenden kannst.


Komplette Zusammenfassung durch Chat GPT:

CS50P – Lecture 0: Functions & Variables

Komplette Zusammenfassung auf Deutsch
Die erste CS50 Python Vorlesung behandelt die absoluten Grundlagen von Python und Programmierung allgemein.
Die Lecture ist extrem wichtig, weil dort fast alle Grundlagen erklärt werden, auf denen später alles aufbaut. 

1. Was ist Programmierung?
Programmieren bedeutet:
einem Computer Anweisungen geben.
Der Computer versteht eigentlich nur:
	• 0 
	• 1 
Python übersetzt unseren geschriebenen Code in Maschinensprache. 

2. Das erste Programm
Das klassische erste Programm:

print("hello, world")

3. Funktionen (Functions)
Eine Funktion ist:
eine Aktion oder Fähigkeit.
Beispiele:

print()
input()
round()
int()
float()

print()
Gibt etwas im Terminal aus.

print("Hallo")

input()
Fragt den Benutzer nach einer Eingabe.

name = input("Wie heißt du? ")

4. Argumente und Parameter
Funktionen können Informationen bekommen.
Beispiel:

print("Hallo")
"Hallo" ist das Argument.

5. Variablen
Variablen speichern Werte.

name = "Stefan"
Das = bedeutet:
Weise den rechten Wert der linken Variable zu.

Beispiel:

name = input("Wie heißt du? ")
print("Hallo,", name)

6. Bugs und Fehlermeldungen
Fehler gehören zum Programmieren.
CS50 erklärt:
Fehler sind normal.
Typische Fehler:
	• Klammern vergessen 
	• Doppelpunkte vergessen 
	• Einrückung falsch 
	• Variable falsch geschrieben 
Python zeigt Fehlermeldungen an, damit man den Fehler findet. 

7. VS Code und Terminal
VS Code ist:
dein Arbeitsplatz.
Dort:
	• schreibst du Code 
	• öffnest Dateien 
	• nutzt das Terminal 
	• startest Programme 

Terminal
Das Terminal ist:
die Kommandozeile.
Dort startest du Programme:

python hello.py

8. Strings
Strings sind:
Textwerte
Beispiele:

"Hallo"
"Stefan"
"Python"

9. String-Methoden
Strings besitzen Funktionen.

.strip()
Entfernt Leerzeichen.

name = name.strip()

.title()
Macht Anfangsbuchstaben groß.

name = name.title()

.capitalize()
Nur erster Buchstabe groß.

city.capitalize()

10. f-Strings
Moderne Methode Texte und Variablen zu kombinieren.

Alte Methode

print("Hallo,", name)

f-String

print(f"Hallo, {name}")
Das ist:
	• moderner 
	• lesbarer 
	• professioneller 

11. Escape Characters
Wenn man Anführungszeichen im String braucht:

print("Er sagte \"Hallo\"")
\ nennt man:
Escape Character

12. Kommentare
Kommentare sind Notizen im Code.

# Das ist ein Kommentar
Kommentare helfen:
	• beim Lernen 
	• beim Verstehen 
	• bei großen Projekten 

13. Pseudocode
Pseudocode bedeutet:
Logik vorher aufschreiben.
Beispiel:

# Benutzer nach Namen fragen
# Namen speichern
# Namen ausgeben
Das hilft beim Planen.

14. int()
Konvertiert Text in Ganzzahlen.

x = int(input("x: "))
Warum wichtig?
input() liefert immer Strings zurück.

15. float()
Für Kommazahlen.

x = float(input("x: "))

16. Mathematische Operatoren

+   Addition
-   Subtraktion
*   Multiplikation
/   Division

Quadrat

x * x
oder:

x ** 2

17. Rundung

round(x)
oder:

round(x, 2)

18. Tausendertrennzeichen
Mit f-Strings:

print(f"{x:,}")
Beispiel:

1000000
wird:

1,000,000

19. Eigene Funktionen mit def
Das ist einer der wichtigsten Teile der Lecture.

Funktion definieren

def hello():
    print("Hallo")

Funktion aufrufen

hello()

20. Parameter
Funktionen können Werte bekommen.

def hello(to):
    print("Hallo,", to)

21. main()
Große Programme nutzen oft:

def main():
Das ist:
der Hauptteil des Programms.

Warum?
Damit:
	• der Code sauber bleibt 
	• die Logik besser lesbar ist 
	• große Programme strukturierter werden 

22. return
Sehr wichtiger Punkt.

print()
zeigt etwas nur an.

return
gibt einen Wert zurück.
Beispiel:

def square(n):
    return n * n

Verwendung

x = square(5)
Jetzt enthält x:

25

23. Scope
Variablen existieren nur in bestimmten Bereichen.
Beispiel:

def hello():
    name = "Stefan"
name existiert nur innerhalb der Funktion.

24. Der wichtigste Gedanke der Lecture
CS50 erklärt immer wieder:
Programmieren lernt man durch Fehler.
Nicht durch Auswendiglernen.
Sondern durch:
	• ausprobieren 
	• Fehler machen 
	• Debugging 
	• Wiederholen 
	• Üben 

Was du nach Lecture 0 gelernt hast
Du kannst jetzt bereits:
✅ Python installieren
✅ VS Code nutzen
✅ Terminal verwenden
✅ Programme starten
✅ Git & GitHub nutzen
✅ Variablen verwenden
✅ Input verarbeiten
✅ Strings bearbeiten
✅ int und float nutzen
✅ Rechnen in Python
✅ Eigene Funktionen schreiben
✅ return verstehen
✅ Fehler lesen und beheben
✅ Commits erstellen
✅ Projekte versionieren

