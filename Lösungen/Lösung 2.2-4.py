# Übung 2.2-4: Multiplikationstabelle
#
# Schreibe ein Programm, das die Multiplikationstabelle für eine gegebene Zahl ausgibt.
# Das Programm soll:
# 1. Den Benutzer nach einer Zahl fragen
# 2. Die Multiplikationstabelle von 1 bis 10 für diese Zahl ausgeben

# Lösung:
zahl = int(input("Wähle eine Zahl: "))
for i in range(1, 11):
    print(str(zahl) + " * " + str(i) + " = " + str(zahl * i))
