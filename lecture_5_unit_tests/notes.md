Was ist Unit Testing?

Unit Testing bedeutet:

Kleine Teile eines Programms automatisch testen.

Meistens testet man:

Funktionen
Berechnungen
Rückgabewerte
Warum sind Tests wichtig?

Tests helfen:

Fehler früh zu erkennen
sicheren Code zu schreiben
Änderungen zu überprüfen
Bugs zu vermeiden

Professionelle Entwickler testen ihren Code ständig.

Das Problem ohne Tests

Ohne Tests müsste man:

jede Funktion manuell starten
alles selbst überprüfen
ständig Inputs eingeben

Das kostet Zeit und führt zu Fehlern.

Beispiel ohne Tests
def square(n):
    return n * n

Man müsste jedes Mal selbst testen:

print(square(2))
print(square(3))
Unit Tests automatisieren das

Stattdessen schreibt man:

def test_square():
    assert square(2) == 4

Dann überprüft Python automatisch:

ob die Funktion korrekt arbeitet
assert
assert square(2) == 4

Bedeutet:

Überprüfe, ob square(2) wirklich 4 ergibt.
Wenn der Test erfolgreich ist

→ keine Fehlermeldung

Wenn der Test fehlschlägt

Python zeigt:

AssertionError
Fehlerdetails
Mehrere Tests
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0

Sehr wichtig:

auch Grenzfälle testen
negative Zahlen testen
0 testen
pytest

pytest ist ein Test-Framework für Python.

Es findet automatisch:

Testdateien
Testfunktionen
asserts
Installation
pip install pytest
Tests starten

Unter Windows oft:

py -m pytest

Oder:

python -m pytest
Warum nicht einfach pytest?

Auf Windows ist PATH oft nicht gesetzt.

Darum benutzt man besser:

py -m pytest
Dateinamen für Tests

pytest sucht automatisch nach:

test_...

oder:

..._test.py
Beispiel Struktur
calculator.py
def square(n):
    return n * n
test_calculator.py
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
Wichtige Erkenntnis

Tests werden getrennt vom eigentlichen Programm geschrieben.

Das ist professioneller:

sauberer
strukturierter
leichter wartbar
Fehler finden mit Tests

Beispiel Fehler:

def square(n):
    return n + n

Dann schlägt der Test fehl:

assert 4 == 9

Dadurch erkennt man sofort:

die Funktion ist falsch
Testbare Funktionen schreiben

Funktionen sollten:

klein sein
klar sein
Werte zurückgeben

Das macht Testing einfacher.

return ist wichtig

Tests funktionieren meistens mit:

return

nicht mit:

print()
Warum?
print()

zeigt nur etwas an.

return

gibt einen echten Wert zurück,
den Tests vergleichen können.

Eigene Erklärung
Unit Tests prüfen automatisch,
ob Funktionen die richtigen Ergebnisse liefern.
Gute Testfälle

Man sollte testen:

normale Werte
große Werte
kleine Werte
negative Werte
0
falsche Inputs
pytest Ausgabe
Erfolgreich
1 passed
Fehler
1 failed
Wichtige Begriffe
Begriff	Bedeutung
Unit Test	Test für kleine Codeeinheit
assert	Erwartung überprüfen
pytest	Python Test Framework
passed	Test erfolgreich
failed	Test fehlgeschlagen
return	Wert zurückgeben
bug	Fehler im Code
Sehr wichtige Erkenntnis aus Lecture 5
Professionelle Entwickler testen ihren Code automatisch,
anstatt alles manuell auszuprobieren.
Eigene Gesamtzusammenfassung
Lecture 5 erklärt Unit Testing mit pytest.

Mit assert überprüft man automatisch,
ob Funktionen korrekt arbeiten.
Tests werden in separaten Dateien geschrieben.
pytest findet und startet diese Tests automatisch.

Tests helfen dabei:
- Bugs früh zu finden
- sicheren Code zu schreiben
- Änderungen zu überprüfen
- professioneller zu programmieren