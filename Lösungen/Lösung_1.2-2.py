# Übung 1.2-2: Alter speichern und verwenden
# 
# Schreibe ein Programm, das:
# 1. Den Benutzer nach seinem Alter fragt
# 2. Das Alter in einer Variablen speichert
# 3. Einen Satz ausgibt, der das Alter verwendet

# Lösung:
alter = int(input("Wie alt bist du? "))
print("Du bist " + str(alter) + " Jahre alt. In einem Jahr bist du " + str(alter + 1) + ".")