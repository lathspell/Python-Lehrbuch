# Übung 2.1-5: Alterskategorien
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach seinem Alter fragt
# 2. Das Alter in eine der folgenden Kategorien einteilt:
#    - Baby: 0-2 Jahre
#    - Kind: 3-12 Jahre
#    - Jugendlicher: 13-19 Jahre
#    - Erwachsener: 20-64 Jahre
#    - Senior: 65+ Jahre
# 3. Gibt die entsprechende Kategorie aus

# Lösung:
alter = int(input("Wie alt bist du? "))
if alter <= 2:
    print("Baby")
elif alter <= 12:
    print("Kind")
elif alter <= 19:
    print("Jugendlicher")
elif alter <= 64:
    print("Erwachsener")
else:
    print("Senior")
