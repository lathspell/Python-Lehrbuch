# Übung 2.1-3: if-elif-else
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach einer Zahl fragt
# 2. Prüft, ob die Zahl positiv, negativ oder null ist
# 3. Gibt den entsprechenden Text aus

# Lösung:
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv")
elif zahl < 0:
    print("Die Zahl ist negativ")
else:
    print("Die Zahl ist null")
