# Übung 2.1-4: Mehrere Bedingungen mit and/or
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach seinem Alter fragt
# 2. Prüft, ob die Person zwischen 13 und 19 Jahre alt ist (inklusive)
# 3. Wenn ja, gibt es "Du bist ein Jugendlicher" aus
# 4. Wenn nein, gibt es "Du bist kein Jugendlicher" aus

# Lösung:
alter = int(input("Wie alt bist du? "))
if alter >= 13 and alter <= 19:
    print("Du bist ein Jugendlicher")
else:
    print("Du bist kein Jugendlicher")
