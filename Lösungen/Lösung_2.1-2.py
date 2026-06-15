# Übung 2.1-2: if-else
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach einer Zahl fragt
# 2. Prüft, ob die Zahl gerade oder ungerade ist
# 3. Gibt "Die Zahl ist gerade" oder "Die Zahl ist ungerade" aus

# Lösung:
zahl = int(input("Gib eine Zahl ein: "))
if zahl % 2 == 0:
    print("Die Zahl ist gerade")
else:
    print("Die Zahl ist ungerade")
