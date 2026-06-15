# Übung 2.3-3: NOT Operator
#
# Schreibe ein Programm, das:
# 1. Den Benutzer nach einem Passwort fragt
# 2. Prüft, ob das Passwort NICHT "geheim" ist
# 3. "Passwort akzeptiert" ausgibt, wenn das Passwort nicht "geheim" ist
# 4. "Passwort abgelehnt" ausgibt, wenn das Passwort "geheim" ist

# Lösung:
passwort = input("Gib dein Passwort ein: ")
if not (passwort == "geheim"):
    print("Passwort akzeptiert")
else:
    print("Passwort abgelehnt")
