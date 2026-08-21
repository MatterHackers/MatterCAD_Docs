---
title: Array
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Array

Array erstellt mehrere Kopien eines Objekts, die in einem Muster angeordnet werden. Wählen Sie oben über die Schaltflächen einen Modus — **Linear**, **Radial** oder **Transformieren** —, um zwischen den Mustertypen zu wechseln.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Array** aus dem Menü Duplizierung an
3. Wählen Sie einen Modus (Linear, Radial oder Transformieren)
4. Passen Sie die Parameter für den gewählten Modus an

## Modus: Linear

Im Modus Linear werden Kopien entlang einer Richtung platziert, wahlweise mit fortschreitender Drehung und Skalierung.

**Anzahl** — Anzahl der Kopien (Ganzzahl oder Ausdruck). Das Ausgangsobjekt ist die erste Kopie; weitere Kopien werden davon versetzt.

**Versatzmethode** — Wie der Abstand berechnet wird:
- **Relativ** — Der Versatz wird mit der Größe des Begrenzungsrahmens des Objekts multipliziert. Ein Relativer Offset von (1, 0, 0) setzt die Kopien entlang X genau eine Objektbreite auseinander.
- **Versatz** — Fester Abstand im Weltkoordinatensystem in mm pro Kopie.
- **Endpunkt** — Legt die Position der letzten Kopie fest; der Abstand wird gleichmäßig auf die Kopien verteilt.

**Relativer Offset** / **Versatz** / **Endpunkt** — Der Abstandsvektor, abhängig von der gewählten Versatzmethode.

**Drehmodus** — Wie sich die Drehung über die Kopien hinweg aufsummiert:
- **Lokal** — Jede Kopie dreht sich an Ort und Stelle um ihren eigenen Mittelpunkt; die Versatzrichtung bleibt an den Weltachsen ausgerichtet.
- **Verbund** — Die Drehung summiert sich auf und lenkt den Versatz mit, wodurch Spiralen, Fächer und Helices entstehen.

**Drehung** — Drehung pro Kopie in Grad um jede Achse.

**Skalieren** — Kumulative Skalierung pro Kopie auf jeder Achse. Werte kleiner als 1 verkleinern die Kopien, Werte größer als 1 vergrößern sie.

**Skalierung beeinflusst Versatz** — Wenn aktiviert, wird auch der Abstand zwischen den Kopien mit jedem Schritt skaliert. Verwenden Sie dies für enger werdende Spiralen und geometrische Progressionen (Nautilusschalen, gestapelte Nagelschalenkurven).

## Modus: Radial

Im Modus Radial werden Kopien gleichmäßig um eine Mittelachse in einem festen Radius verteilt.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Zählmethode** — Wie die Anzahl der Kopien bestimmt wird:
- **Anzahl** — Explizite Anzahl der Kopien.
- **Abstand** — Winkelabstand zwischen den Kopien in Grad; die Anzahl wird berechnet, um den Sweep zu füllen.

**Anzahl** / **Winkelabstand** — Anzahl der Kopien (Modus Anzahl) oder Winkelabstand in Grad (Modus Abstand). Unterstützt Ausdrücke.

**Mittelachse** — Die Achse, um die gedreht wird (Standard: Z).

**Kreissegment** — Ob die Kopien einen vollständigen 360°-Kreis (**Voll**) oder einen Teilbogen (**Bogen**) umspannen.

**Radius** — Abstand von der Mittelachse zu jeder Kopie.

**Sweep-Winkel** — Zu füllender Bogen in Grad (wird angezeigt, wenn Kreissegment auf Bogen steht). Unterstützt Ausdrücke.

**Rotation ausrichten** — Dreht jede Kopie so, dass ihre Vorwärtsachse vom Mittelpunkt nach außen zeigt.

**Vorwärtsachse** — Welche Achse der Kopie für die Ausrichtung als „vorwärts“ behandelt wird (wird angezeigt, wenn Rotation ausrichten aktiviert ist).

## Modus: Transformieren

Im Modus Transformieren werden die Kopien mit einer manuellen Transformation oder anhand der Transformation eines anderen Objekts schrittweise versetzt.

**Anzahl** — Anzahl der Kopien (Ganzzahl oder Ausdruck).

**Transformationsreferenz** — Woher die Transformation pro Schritt stammt:
- **Eingabe** — Sie geben Verschiebung, Drehung und Skalierung direkt an.
- **Objekt** — Die Transformation wird von einem benannten Geschwisterobjekt übernommen.

**Verschiebung** — Versatz pro Schritt im Weltkoordinatensystem in mm (wird angezeigt, wenn die Referenz Eingabe ist).

**Drehung** — Drehung pro Schritt in Grad je Achse (wird angezeigt, wenn die Referenz Eingabe ist).

**Skalieren** / **Achsen skalieren** — Gleichmäßige und achsenweise Skalierung, die bei jedem Schritt angewendet wird (wird angezeigt, wenn die Referenz Eingabe ist).

**Transformationsname** — Name des Geschwisterobjekts, dessen Transformation als Schrittinkrement verwendet wird (wird angezeigt, wenn die Referenz Objekt ist).

**Relativer Raum** — Wenn aktiviert, summiert sich die Transformation jeder Kopie im lokalen Bezugssystem der vorherigen Kopie; wenn deaktiviert, wird jeder Schritt im Weltkoordinatensystem angewendet (wird angezeigt, wenn die Referenz Objekt ist).

## Randomisieren

Aktivieren Sie **Randomisieren**, um allen Kopien Variation hinzuzufügen.

- **Zufälliger Versatz** — Maximaler zufälliger Positionsversatz pro Achse in mm.
- **Zufällige Drehung** — Maximale zufällige Drehung pro Achse in Grad.
- **Zufallsskalierungsachsen** — Maximale zufällige Skalierungsvariation pro Achse.
- **Erste ausschließen** — Behält die erste Kopie an ihrer exakt berechneten Position (Standard: aktiviert).
- **Letzte ausschließen** — Behält die letzte Kopie an ihrer exakt berechneten Position.
- **Zufallsstartwert** — Ändern Sie diesen Wert, um eine andere zufällige Anordnung zu erhalten. Unterstützt Ausdrücke.

## Zusammenführen

- **Einzelnes Mesh erstellen** — Vereint alle Kopien zu einem einzigen zusammengeführten Mesh-Objekt.
- **Vertices zusammenführen** — Verschweißt Vertices innerhalb des Schwellenwerts für den Zusammenführungsabstand (wird angezeigt, wenn Einzelnes Mesh erstellen aktiviert ist).
- **Abstand** — Schwellenwert für das Zusammenführen in mm (wird angezeigt, wenn Vertices zusammenführen aktiviert ist).

## Tipps

- Verwenden Sie Ausdrücke für Anzahl, Drehung oder Endpunkt, um parametrische Muster zu erzeugen
- Verwenden Sie für kreisförmige Muster den Modus Radial — legen Sie den Radius fest, um die Kreisgröße zu steuern, und aktivieren Sie Rotation ausrichten, wenn die Kopien nach außen zeigen sollen
- Die Verbund-Drehung im Modus Linear erzeugt Spiralen und Fächer, ohne dass Sie Winkelversätze manuell berechnen müssen
- Skalierung beeinflusst Versatz erzeugt ganz von selbst Layouts nach Art von Nautilusschalen und geometrischen Progressionen
- Kombinieren Sie Array mit [Unterobjekt auswählen](select-child.md), um Muster zu erstellen, bei denen jede Kopie eine andere Variante zeigt

## Verwandte Themen

- [Ausrichten](../placement/align.md) - Objekte relativ zueinander positionieren
- [Unterobjekt auswählen](select-child.md) - Eine bestimmte Kopie aus einem Array anhand von Index oder Name auswählen
