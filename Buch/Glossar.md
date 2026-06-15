# Glossar

Dieses Glossar erklärt die wichtigsten Begriffe aus der Programmierung mit Python.

---

## A

### and

Ein **logischer Operator**, der zwei Bedingungen verbindet.
Das Ergebnis ist nur dann `True` (wahr), wenn **beide** Bedingungen wahr sind.

```python
if alter >= 18 and alter <= 65:
    print("Zugang gewährt")
```

---

## B

### break

Ein Schlüsselwort, das eine **Schleife sofort beendet**.

```python
while True:
    eingabe = input("Gib eine Zahl ein (oder 'Stopp'): ")
    if eingabe == "Stopp":
        break  # Beendet die while-Schleife
```

---

## C

### continue

Ein Schlüsselwort, das den **aktuellen Durchlauf einer Schleife überspringt** und mit dem nächsten Durchlauf weitermacht.

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print(i)  # Gibt nur ungerade Zahlen aus
```

---

## D

### Datentyp

Der **Typ eines Wertes** in Python.
Beispiele: `str` (Text), `int` (Ganzzahl), `float` (Dezimalzahl).

---

## E

### elif

Kurz für "**else if**".
Wird in Kombination mit `if` verwendet, um **mehrere Bedingungen** zu prüfen.

```python
note = 2
if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
```

---

### else

Der **Standardfall** in einer `if`-Anweisung.
Wird ausgeführt, wenn **keine** der vorherigen Bedingungen (`if`, `elif`) wahr war.

```python
if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

---

## F

### Float

Ein **Datentyp** für Dezimalzahlen (Zahlen mit Nachkommastellen).

```python
3.14
0.5
-2.718
```

---

### for-Schleife

Eine **Schleife**, die Code für jedes Element in einer **Sequenz** (z.B. Liste, range) ausführt.

```python
for i in range(1, 6):
    print(i)  # Gibt die Zahlen 1 bis 5 aus
```

---

## I

### if

Eine **Bedingung**, die Code nur ausführt, wenn eine Prüfung wahr ist.

```python
if alter >= 18:
    print("Du bist volljährig")
```

---

### input()

Eine **Funktion**, die auf eine **Benutzereingabe wartet** und diese als Text (String) zurückgibt.

```python
name = input("Wie heißt du? ")
```

**Wichtig:** `input()` gibt immer einen String zurück! Für Zahlen musst du `int()` oder `float()` verwenden.

---

### Integer

Ein **Datentyp** für **ganze Zahlen** (ohne Nachkommastellen).

```python
42
-3
0
```

---

## K

### Kommentar

Text in deinem Code, der **nicht ausgeführt wird**, sondern nur für Menschen lesbar ist.
Beginnt mit `#`.

```python
# Dies ist ein Kommentar
name = "Anna"  # Dies ist ein inline-Kommentar
```

---

## L

### Logische Operatoren

Operatoren, die **Bedingungen kombinieren**: `and`, `or`, `not`.

| Operator | Name  | Wirkung                                  |
|----------|-------|------------------------------------------|
| `and`    | UND   | Beide Bedingungen müssen wahr sein       |
| `or`     | ODER  | Mindestens eine Bedingung muss wahr sein |
| `not`    | NICHT | Kehrt den Wahrheitswert um               |

---

## M

### Modulo (Operator %)

Ein **Operator**, der den **Rest einer Division** zurückgibt.

```python
10 % 3  # Ergebnis: 1 (denn 10 ÷ 3 = 3 Rest 1)
```

Nützlich, um zu prüfen, ob eine Zahl gerade ist:

```python
if zahl % 2 == 0:
    print("Die Zahl ist gerade")
```

---

## N

### not

Ein **logischer Operator**, der den Wahrheitswert **umkehrt**.

```python
if not (passwort == "geheim"):
    print("Passwort ist nicht 'geheim'")
```

---

## O

### Operatoren

Symbole, die **Operationen** auf Werten durchführen.

**Arithmetische Operatoren:**

| Operator | Name              | Beispiel  | Ergebnis |
|----------|-------------------|-----------|----------|
| `+`      | Addition          | `5 + 3`   | `8`      |
| `-`      | Subtraktion       | `10 - 4`  | `6`      |
| `*`      | Multiplikation    | `3 * 7`   | `21`     |
| `/`      | Division          | `10 / 2`  | `5.0`    |
| `//`     | Ganzzahl-Division | `10 // 3` | `3`      |
| `%`      | Modulo            | `10 % 3`  | `1`      |
| `**`     | Potenz            | `2 ** 3`  | `8`      |

**Vergleichsoperatoren:**

| Operator | Bedeutung           | Beispiel           |
|----------|---------------------|--------------------|
| `==`     | gleich              | `alter == 18`      |
| `!=`     | ungleich            | `name != "Anna"`   |
| `<`      | kleiner als         | `zahl < 10`        |
| `>`      | größer als          | `zahl > 5`         |
| `<=`     | kleiner oder gleich | `alter <= 18`      |
| `>=`     | größer oder gleich  | `temperatur >= 20` |

---

### or

Ein **logischer Operator**, der zwei Bedingungen verbindet.
Das Ergebnis ist `True` (wahr), wenn **mindestens eine** der Bedingungen wahr ist.

**Beispiel:**

```python
if note == 1 or note == 2:
    print("Sehr gut oder gut")
```

---

## P

### Potenz (Operator **)

Ein **Operator**, der eine Zahl mit einer anderen potenziert.

---

### print()

Eine **Funktion**, die Text oder Werte auf dem **Bildschirm ausgibt**.

---

## R

### range()

Eine **Funktion**, die eine **Sequenz von Zahlen** erzeugt.
Wird oft in `for`-Schleifen verwendet.

**Beispiele:**

| Aufruf            | Ergebnis                       |
|-------------------|--------------------------------|
| `range(5)`        | 0, 1, 2, 3, 4                  |
| `range(1, 5)`     | 1, 2, 3, 4                     |
| `range(1, 10, 2)` | 1, 3, 5, 7, 9 (Schrittweite 2) |

```python
for i in range(1, 6):
    print(i)  # Gibt 1, 2, 3, 4, 5 aus
```

---

## S

### Schleife

Eine **Code-Struktur**, die einen Code-Block **mehrmals ausführt**.

**Arten von Schleifen:**

- **`while`-Schleife:** Führt Code aus, **solange** eine Bedingung wahr ist
- **`for`-Schleife:** Führt Code für jedes Element in einer Sequenz aus

---

### String

Ein **Datentyp** für **Text**.
Steht immer in **Anführungszeichen** (einfach oder doppelt).

```python
"Hallo Welt"
'Python'
"123"  # Dies ist ein String, keine Zahl!
```

---

## V

### Variable

Ein **benannter Behälter** für einen Wert.
Du kannst dir eine Variable wie eine **beschriftete Schachtel** vorstellen.

```python
name = "Anna"  # Speichert "Anna" in der Variablen name
alter = 15     # Speichert 15 in der Variablen alter
```

**Regeln für Variablennamen:**

- Keine Leerzeichen (nutz stattdessen `_`)
- Keine Sonderzeichen (außer `_`)
- Keine Python-Schlüsselwörter (z.B. `if`, `for`, `while`)
- Sollten **beschreibend** sein (z.B. `alter` statt `x`)

---

### Verschachtelung

Das **Schachteln von Code-Blöcken** ineinander.
Beispiel: Eine `if`-Anweisung innerhalb einer anderen `if`-Anweisung.

```python
if alter >= 18:
    if fuehrerschein:
        print("Du darfst Auto fahren")
    else:
        print("Du brauchst einen Führerschein")
else:
    print("Du bist zu jung")
```

---

## W

### while-Schleife

Eine **Schleife**, die Code **solange ausführt**, wie eine **Bedingung wahr ist**.

```python
zahl = 1
while zahl <= 5:
    print(zahl)
    zahl = zahl + 1
```

**Achtung:** Wenn die Bedingung nie falsch wird, läuft die Schleife **unendlich**!

---

## Z

### Zuweisung (Operator =)

Der **Operator `=`** speichert einen Wert in einer Variablen.

```python
name = "Anna"    # Speichert "Anna" in name
alter = 15 + 3   # Berechnet 18 und speichert es in alter
x = y           # Speichert den Wert von y in x
```

**Wichtig:** Nicht verwechseln mit dem Vergleichsoperator `==`!

- `=` ist eine **Zuweisung** (speichert einen Wert)
- `==` ist ein **Vergleich** (prüft auf Gleichheit)
