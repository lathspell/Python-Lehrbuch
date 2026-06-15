# Übung 2.3-4: Kombinierte Bedingungen
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach seinem Alter und seinem Namen fragt
# 2. Prüft, ob die Person "Max" heißt UND zwischen 18 und 30 Jahre alt ist
# 3. "Willkommen, Max!" ausgibt, wenn beide Bedingungen wahr sind
# 4. "Zutritt verweigert" ausgibt, wenn nicht beide Bedingungen wahr sind

# Lösung:
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
if name == "Max" and alter >= 18 and alter <= 30:
    print("Willkommen, Max!")
else:
    print("Zutritt verweigert")
