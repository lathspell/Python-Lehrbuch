# Übung 2.3-5: Verschachtelte Bedingungen
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach seinem Alter fragt
# 2. Wenn das Alter >= 18 ist:
#    - Den Benutzer fragt, ob er einen Führerschein hat (ja/nein)
#    - Wenn ja: "Du darfst Auto fahren" ausgeben
#    - Wenn nein: "Du brauchst einen Führerschein" ausgeben
# 3. Wenn das Alter < 18 ist:
#    - "Du bist zu jung zum Autofahren" ausgeben

# Lösung:
alter = int(input("Wie alt bist du? "))
if alter >= 18:
    fuehrerschein = input("Hast du einen Führerschein? (ja/nein): ")
    if fuehrerschein == "ja":
        print("Du darfst Auto fahren")
    else:
        print("Du brauchst einen Führerschein")
else:
    print("Du bist zu jung zum Autofahren")
