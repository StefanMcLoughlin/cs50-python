# Uebung 4 - Einfache Trading Logik
# Fragestellung: Gewinn? Verlust? - Wenn Gewinn groesser als Verlust -> Strategie profitabel, sonst -> Strategie nicht profitabel

gewinn = int(input("Bitte trage die Summe der Gewinntrades ein: "))
verlust = int(input("Bitte trage die Summe der Verlusttrades ein: "))

if gewinn > verlust:
    print("Strategie profitabel")
elif gewinn == verlust:
    print("Breakeven")
else:
    print("Strategie nicht profitabel")

differenz = gewinn - verlust
print (f"Gewinnüberschuss: {differenz}")