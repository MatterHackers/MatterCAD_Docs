---
title: Variablenblatt
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Variablenblatt

Das Variablenblatt speichert gemeinsam genutzte Werte für einen Entwurf. Verwenden Sie es, wenn mehrere Objekte auf dieselben Maße, Anzahlen, Beschriftungen oder Formeln verweisen sollen. Beim Ändern eines Werts im Blatt werden die abhängigen Objekte neu berechnet, sodass parametrische Entwürfe konsistent bleiben, ohne dass Sie jedes Objekt einzeln bearbeiten müssen.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## So fügen Sie ein Variablenblatt hinzu

1. Öffnen Sie die Bibliothek und fügen Sie **Variablenblatt** zur Szene hinzu.
2. Wählen Sie das Objekt Variablenblatt aus, um den Blatteditor anzuzeigen.
3. Wählen Sie eine Zelle aus und geben Sie dann einen **Name** und einen Wert oder eine Formel ein.
4. Verwenden Sie den Zellennamen in anderen ausdrucksfähigen Feldern des Entwurfs.

## Zellen bearbeiten

Jede Zelle besteht aus zwei bearbeitbaren Teilen:

- **Name** – Ein optionaler Variablenname für die Zelle. Namen unterscheiden nicht zwischen Groß- und Kleinschreibung, Leerzeichen werden in Unterstriche umgewandelt und doppelte Namen werden automatisch angepasst.
- **Ausdruck** – Der Zellenwert. Reiner Text oder Zahlen werden direkt gespeichert. Formeln beginnen mit `=`.

Zellen können auch über ihre Adresse referenziert werden, etwa `A1` oder `B2`. Benannte Zellen sind für Entwurfsparameter meist verständlicher, weil sie die Absicht beschreiben, zum Beispiel `wall_thickness`, `outer_diameter` oder `hole_count`.

## Formeln

Beginnen Sie eine Formel mit `=`, damit sie im Blatt ausgewertet wird:

- `=20 + 5` ergibt `25`
- `=pi * 10` ergibt `31.41592653589793`
- `=A1 * 2` verweist über die Adresse auf eine andere Zelle
- `=wall_thickness + 4` verweist auf eine benannte Zelle

Das Blatt unterstützt Arithmetik, Klammern, Vergleichsoperatoren, gängige `Math`-Funktionen wie `sin`, `cos`, `sqrt` und `round` sowie Konstanten wie `pi`, `tau` und `e`.

## Blattwerte in Objekten verwenden

Die meisten numerischen Felder in MatterCAD unterstützen Ausdrücke. Um einen Blattwert in einem Objektparameter zu verwenden, stellen Sie der Referenz `=` voran:

- Setzen Sie die **Breite** eines Würfels auf `=case_width`.
- Setzen Sie die **Anzahl** eines Arrays auf `=hole_count`.
- Setzen Sie einen **Versatz**-Wert von Verschieben auf `=wall_thickness * 2`.

Wenn sich das Blatt ändert, berechnet MatterCAD die davon abhängigen Objekte neu.

## Text- und Hilfsfunktionen

Zellen des Variablenblatts können nicht nur Zahlen, sondern auch Text enthalten. Textwerte sind nützlich für erzeugte Beschriftungen, Teilenummern, importierte Daten und eigene Konstruktions-Apps.

Nützliche Hilfsfunktionen sind:

- `concat()` oder `strcat()` – Verbindet Text oder Werte miteinander.
- `substring()` – Extrahiert einen Teil eines Textwerts.
- `split()` – Teilt Text und gibt ein Element zurück.
- `count()` – Zählt die durch Trennzeichen getrennten Elemente in einem Text.
- `substitute()` – Ersetzt Text.
- `rand(seed)` – Erzeugt einen deterministischen Zufallswert, wenn ein Startwert angegeben wird.
- `importdata()` – Liest einen Wert aus einer URL oder einem lokalen Dateipfad.

## Tipps

- Bevorzugen Sie für Werte, die von anderen Objekten verwendet werden, aussagekräftige Namen gegenüber Zellenadressen.
- Halten Sie zentrale Maße nahe der linken oberen Ecke des Blatts, damit sie leicht zu finden sind.
- Verwenden Sie Formeln für abgeleitete Werte, zum Beispiel `inner_diameter = outer_diameter - wall_thickness * 2`.
- Vermeiden Sie reservierte Wörter wie `pi`, `e`, `true`, `false` oder Funktionsnamen als Zellennamen.
- Wenn eine Formel nicht ausgewertet werden kann, behält MatterCAD die ursprüngliche Eingabe als Text bei.

## Verwandte Themen

- [Ausdrücke](expressions.md) – Ausdrücke in Objektparametern verwenden
- [Komponenten](components.md) – Wiederverwendbare parametrische Entwürfe erstellen
- [Array](../operations/array/array.md) – Wiederholte Muster erstellen, die von Blattwerten gesteuert werden
