# Übung 2.3-2: Einfaches OR
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach einer Zahl fragt
# 2. Prüft, ob die Zahl 1, 2 oder 3 ist
# 3. "Gewonnen!" ausgibt, wenn die Zahl 1, 2 oder 3 ist
# 4. "Verloren!" ausgibt, wenn die Zahl etwas anderes ist

# Lösung:
zahl = int(input("Wähle eine Zahl: "))
if zahl == 1 or zahl == 2 or zahl == 3:
    print("Gewonnen!")
else:
    print("Verloren!")
