# Übung 2.2-5: Benutzereingabe in Schleife
#
# Schreibe ein Programm, das:
# 1. Den Benutzer so lange nach Zahlen fragt, bis er "Stopp" eingibt
# 2. Alle eingegebenen Zahlen in einer Liste speichert
# 3. Am Ende alle Zahlen ausgibt

# Lösung:
zahlen = []
while True:
    eingabe = input("Gib eine Zahl ein (oder 'Stopp' zum Beenden): ")
    if eingabe == "Stopp":
        break
    zahlen.append(int(eingabe))
print("Eingegebene Zahlen:", zahlen)
