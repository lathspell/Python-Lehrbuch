# Übung 2.2-3: Summe berechnen
#
# Schreibe ein Programm, das:
# 1. Die Summe aller Zahlen von 1 bis 10 berechnet
# 2. Das Ergebnis ausgibt

# Lösung:
summe = 0
for zahl in range(1, 11):
    summe = summe + zahl
print("Die Summe von 1 bis 10 ist:", summe)
