# Übung 1.2-3: Mehrere Variablen kombinieren
# 
# Schreibe ein Programm, das:
# 1. Den Benutzer nach seinem Vornamen fragt
# 2. Den Benutzer nach seinem Nachnamen fragt
# 3. Den Benutzer nach seinem Alter fragt
# 4. Alle Informationen in einem Satz ausgibt

# Lösung:
vorname = input("Vorname? ")
nachname = input("Nachname? ")
alter = int(input("Alter? "))
print(vorname + " " + nachname + " ist " + str(alter) + " Jahre alt.")