# Übung 2.3-1: Einfaches AND
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach seinem Alter fragt
# 2. Prüft, ob die Person zwischen 18 und 65 Jahre alt ist (inklusive)
# 3. "Zugang gewährt" ausgibt, wenn die Bedingung wahr ist
# 4. "Zugang verweigert" ausgibt, wenn die Bedingung falsch ist

# Lösung:
alter = int(input("Wie alt bist du? "))
if alter >= 18 and alter <= 65:
    print("Zugang gewährt")
else:
    print("Zugang verweigert")
