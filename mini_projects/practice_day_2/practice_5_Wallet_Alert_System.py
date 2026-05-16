"""
Übung 5 — Wallet Alert System
Aufgabe:

Frage:

Wallet Hitrate
Profit

Wenn:

Hitrate > 50
UND Profit > 1000

→ „Top Wallet erkannt“

Sonst:
→ „Wallet uninteressant“

Bonus:

Unterschiedliche Kategorien:

Elite Wallet
Gute Wallet
Riskante Wallet
"""

hitrate = int(input("Bitte gebe die Hitrate der Wallet in Prozent ein: "))
profit = int(input("Bitte gebe den Profit der Wallet ein: "))



if hitrate > 80 and profit > 1000:
    print("Elite Wallet erkannt")

elif hitrate > 60 and profit > 1000:
    print("Gute Wallet erkannt")

elif hitrate > 50 and profit > 1000:
    print("Top Wallet erkannt.")

elif hitrate > 45 and profit > 1000:
    print("Riskante Wallet")
else:
    print("Wallet uninteressant")