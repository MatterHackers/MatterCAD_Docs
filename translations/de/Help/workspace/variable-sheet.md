---
title: Variablenblatt
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Variablenblatt

Das Variablenblatt speichert gemeinsam genutzte Werte für einen Entwurf. Verwenden Sie es, wenn mehrere Objekte dieselben Abmessungen, Anzahlen, Bezeichnungen oder Formeln referenzieren sollen. Wird ein Wert im Blatt geändert, werden die abhängigen Objekte neu berechnet, sodass parametrische Entwürfe konsistent bleiben, ohne dass jedes Objekt einzeln bearbeitet werden muss.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## So fügen Sie ein Variablenblatt hinzu

1. Öffnen Sie die Bibliothek und fügen Sie **Variable Sheet** zur Szene hinzu.
2. Wählen Sie das Variablenblatt-Objekt aus, um den Blatteditor anzuzeigen.
3. Wählen Sie eine Zelle aus und geben Sie dann einen **Namen** sowie einen Wert oder eine Formel ein.
4. Verwenden Sie den Zellennamen in anderen ausdrucksfähigen Feldern des Entwurfs.

## Zellen bearbeiten

Jede Zelle hat zwei bearbeitbare Teile:

- **Name** – Ein optionaler Variablenname für die Zelle. Bei Namen wird die Groß- und Kleinschreibung nicht beachtet, Leerzeichen werden in Unterstriche umgewandelt und doppelte Namen werden automatisch angepasst.
- **Ausdruck** – Der Zellenwert. Reiner Text oder Zahlen werden direkt gespeichert. Formeln beginnen mit `=`.

Zellen können auch über ihre Adresse referenziert werden, etwa `A1` oder `B2`. Benannte Zellen sind für Entwurfsparameter meist verständlicher, weil sie die Absicht beschreiben, zum Beispiel `wall_thickness`, `outer_diameter` oder `hole_count`.

## Formeln

Beginnen Sie eine Formel mit `=`, damit sie im Blatt ausgewertet wird:

- `=20 + 5` ergibt `25`
- `=pi * 10` ergibt `31.41592653589793`
- `=A1 * 2` referenziert eine andere Zelle über ihre Adresse
- `=wall_thickness + 4` referenziert eine benannte Zelle

Das Blatt unterstützt Arithmetik, Klammern, Vergleichsoperatoren, gängige `Math`-Funktionen wie `sin`, `cos`, `sqrt` und `round` sowie Konstanten einschließlich `pi`, `tau` und `e`.

## Blattwerte in Objekten verwenden

Die meisten numerischen Felder in MatterCAD unterstützen Ausdrücke. Um einen Blattwert in einem Objektparameter zu verwenden, stellen Sie der Referenz `=` voran:

- Setzen Sie die **Breite** eines Würfels auf `=case_width`.
- Setzen Sie die **Anzahl** eines Arrays auf `=hole_count`.
- Setzen Sie einen **Versatz**-Wert einer Verschiebung auf `=wall_thickness * 2`.

Wenn sich das Blatt ändert, berechnet MatterCAD die davon abhängigen Objekte neu.

## Text- und Hilfsfunktionen

Zellen des Variablenblatts können sowohl Text als auch Zahlen enthalten. Textwerte sind nützlich für generierte Bezeichnungen, Teilenummern, importierte Daten und benutzerdefinierte Design-Apps.

Nützliche Hilfsfunktionen sind unter anderem:

- `concat()` oder `strcat()` – Text oder Werte zusammenfügen.
- `substring()` – Einen Teil eines Textwerts extrahieren.
- `split()` – Text aufteilen und ein Element zurückgeben.
- `count()` – Durch Trennzeichen getrennte Elemente in einem Text zählen.
- `substitute()` – Text ersetzen.
- `rand(seed)` – Einen deterministischen Zufallswert erzeugen, wenn ein Startwert angegeben wird.
- `importdata()` – Einen Wert von einer URL oder einem lokalen Dateipfad lesen.

## Tipps

- Bevorzugen Sie beschreibende Namen gegenüber Zellenadressen für Werte, die von anderen Objekten verwendet werden.
- Halten Sie zentrale Abmessungen nahe der linken oberen Ecke des Blatts, damit sie leicht zu finden sind.
- Verwenden Sie Formeln für abgeleitete Werte, zum Beispiel `inner_diameter = outer_diameter - wall_thickness * 2`.
- Vermeiden Sie reservierte Wörter wie `pi`, `e`, `true`, `false` oder Funktionsnamen als Zellennamen.
- Wenn eine Formel nicht ausgewertet werden kann, behält MatterCAD die ursprüngliche Eingabe als Text bei.

## Verwandte Themen

- [Ausdrücke](expressions.md) – Ausdrücke in Objektparametern verwenden
- [Komponenten](components.md) – Wiederverwendbare parametrisierte Entwürfe erstellen
- [Array](../operations/array/array.md) – Wiederholte Muster erstellen, die durch Blattwerte gesteuert werden
