# Design-Entscheidungen für das Python-Lehrbuch

Dieses Dokument hält alle strukturellen und inhaltlichen Entscheidungen für das Python-Lehrbuch fest, um Konsistenz und Klarheit für Autoren, Leser und Tools zu gewährleisten.

---

## 1. Zielgruppe

- **Primäre Zielgruppe:** Absolute Anfänger (keine Programmiererfahrung).
- **Didaktischer Ansatz:** Linearer Aufbau (Kapitel bauen aufeinander auf).
- **Besonderheit:** Es gibt sehr viele Übungen.

---

## 2. Struktur des Buches

### 2.1 Dateisystem

- Das Buch besteht **ausschließlich aus Markdown- und Python-Dateien**.
- **Verzeichnisstruktur:**

```text
  Python-Lehrbuch/
  ├── AGENTS.md               # Diese Datei
  ├── Buch/
  |   ├── Glossar.md              # Fachbegriffe
  |   ├── Inhalt.md               # Inhaltsverzeichnis
  |   ├── 1.1 Ein- und Ausgabe.md
  |   ├── 1.2 Variablen und Datentypen.md
  |   ├── 1.3 Grundlegende Operatoren.md
  |   ├── 2.1 Bedingungen.md
  |   ├── 2.2 Schleifen.md
  |   ├── 2.3 Logische Operatoren und Verschachtelung.md
  |   ├── 3.1 Listen.md
  |   ├── 3.2 Tupel.md
  |   ├── 3.3 Dictionaries.md
  |   ├── 3.4 Sets.md
  |   ├── 4.1 Funktionen definieren.md
  |   ├── 4.2 Parameter und Rückgabewerte.md
  |   ├── 4.3 Module und Importe.md
  |   ├── ...
  ├── Übungen/                # Alle Übungen aller Kapitel
  │   ├── Übung 1.1-1.py      # Aufgabenstellung als Kommentar am Anfang
  │   ├── Übung 1.1-2.py
  │   └── ...
  └── Lösungen/               # Alle Lösungen aller Kapitel
      ├── Lösung 1.1-1.py
      ├── Lösung 1.1-2.py
      └── ...
  ```

### 2.2 Benennungskonventionen

- **Verzeichnisse und Dateien:** Leerzeichen statt Unterstriche (z. B. `1.1 Variablen und Datentypen.md`).
- **Übungen:** Als Python-Dateien im Format `Übung K.M-N.py` (z. B. `Übung 1.1-1.py`, `Übung 1.1-2.py`) in einem gemeinsamen `Übungen`-Ordner im Toplevel.
  - Die **Aufgabenstellung** steht als **Kommentar am Anfang der Datei**.
- **Lösungen:** Als Python-Dateien im Format `Lösung K.M-N.py` (z. B. `Lösung 1.1-1.py`) in einem gemeinsamen `Lösungen`-Ordner im Toplevel.

---

## 3. Aufbau der Kapitel

- **Jedes Unterkapitel** folgt dem Schema:
  **Problem → Theorie → Zusammenfassung → Lösung → Übungen**.
  - **Problem:** Ein praktisches Problem wird gestellt.
  - **Theorie:** Erklärung der zugrundeliegenden Konzepte.
  - **Zusammenfassung:** Kurze, prägnante Übersicht der wichtigsten Syntax/Regeln
  - **Lösung:** Code-Beispiel zur Lösung des Problems.
  - **Übungen:** Verweis auf separate Python-Dateien im `Übungen`-Ordner.

---

## 4. Inhaltsverzeichnis

- Das Inhaltsverzeichnis wird in `/Inhalt.md` gepflegt.
- Es listet alle Kapitel und Unterkapitel auf.

---

## 5. Extras

- **Glossar:** Erklärung von Fachbegriffen in `Glossar.md`.
- **Lösungen:** Separates Verzeichnis `Lösungen` (nicht Teil des Hauptbuches).
- **Ausblick:** Kurze Erwähnung fortgeschrittener Themen (keine Vertiefung).

---

## 6. Richtlinien für Autoren

- **Sprache:** Einfach und verständlich, für absolute Anfänger.
- **Code-Beispiele:** Sollten **praktisch und alltagsnah** sein.
- **Übungen:** Viele Übungen, d.h. mindestens fünf, pro Unterkapitel, um das Gelernte zu festigen.
- **Markdown:**
  - Eine Leerzeile nach jeder Überschrift
  - Eine Leerzeile vor jeder Aufzählung sowie vor jedem Code-Block
  - Reiner Text mit Codeblock Sprache "text" markieren
  - Tabellen so formattieren, dass alle "|" einer Spalte untereinander stehen.
  - Alle Dateien sollen mit einem Newline enden

---

## 7. Versionierung

- Dieses Dokument wird bei **strukturellen Änderungen** aktualisiert.
- Inhaltliche Änderungen an Kapiteln werden **nicht** hier dokumentiert
