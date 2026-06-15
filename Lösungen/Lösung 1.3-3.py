# Übung 1.3-3: Durchschnitt berechnen
# 
# Schreibe ein Programm, das:
# 1. Den Benutzer nach drei Noten fragt
# 2. Den Durchschnitt der drei Noten berechnet
# 3. Das Ergebnis ausgibt

# Lösung:
note1 = int(input("Note 1: "))
note2 = int(input("Note 2: "))
note3 = int(input("Note 3: "))
durchschnitt = (note1 + note2 + note3) / 3
print("Der Durchschnitt ist: " + str(durchschnitt))