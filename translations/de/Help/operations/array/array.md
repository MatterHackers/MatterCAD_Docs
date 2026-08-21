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

Array erzeugt mehrere Kopien eines Objekts, die in einem Muster angeordnet werden. Wählen Sie oben über die Schaltflächen einen Modus – **Linear**, **Radial** oder **Transformation** –, um zwischen den Mustertypen zu wechseln.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Array** aus dem Menü „Duplizieren“ an
3. Wählen Sie einen Modus (Linear, Radial oder Transformation)
4. Passen Sie die Parameter des gewählten Modus an

## Modus: Linear

Im Modus „Linear“ werden Kopien entlang einer Richtung platziert, wahlweise mit fortschreitender Drehung und Skalierung.

**Anzahl** – Anzahl der Kopien (ganze Zahl oder Ausdruck). Das Ausgangsobjekt ist die erste Kopie; weitere Kopien werden dazu versetzt.

**Versatzmethode** – Wie der Abstand berechnet wird:
- **Relativ** – Der Versatz wird mit der Größe des Begrenzungsrahmens des Objekts multipliziert. Ein relativer Versatz von (1, 0, 0) setzt die Kopien entlang X genau eine Objektbreite auseinander.
- **Versatz** – Fester Abstand im Weltkoordinatensystem in mm pro Kopie.
- **Endpunkt** – Legt die Position der letzten Kopie fest; der Abstand wird gleichmäßig auf die Kopien verteilt.

**Relativer Versatz** / **Versatz** / **Endpunkt** – Der Abstandsvektor, abhängig von der gewählten Versatzmethode.

**Rotationsmodus** – Wie sich die Drehung über die Kopien hinweg aufsummiert:
- **Lokal** – Jede Kopie dreht sich an Ort und Stelle um ihren eigenen Mittelpunkt; die Versatzrichtung bleibt an den Weltachsen ausgerichtet.
- **Kumulativ** – Die Drehung summiert sich auf und lenkt den Versatz mit, wodurch Spiralen, Fächer und Helices entstehen.

**Drehung** – Drehung pro Kopie in Grad je Achse.

**Skalierung** – Kumulative Skalierung pro Kopie je Achse. Werte kleiner als 1 verkleinern die Kopien, Werte größer als 1 vergrößern sie.

**Skalierung wirkt auf Versatz** – Wenn aktiviert, skaliert auch der Abstand zwischen den Kopien mit jedem Schritt. Verwenden Sie dies für enger werdende Spiralen und geometrische Progressionen (Nautilusschalen, gestapelte Schneckenkurven).

## Modus: Radial

Im Modus „Radial“ werden Kopien gleichmäßig um eine zentrale Achse in einem festen Radius verteilt.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Anzahlmethode** – Wie die Anzahl der Kopien bestimmt wird:
- **Anzahl** – Explizite Anzahl der Kopien.
- **Abstand** – Winkelabstand zwischen den Kopien in Grad; die Anzahl wird so berechnet, dass der Bereich gefüllt wird.

**Anzahl** / **Winkelabstand** – Anzahl der Kopien (Modus „Anzahl“) oder Winkelabstand in Grad (Modus „Abstand“). Unterstützt Ausdrücke.

**Zentrale Achse** – Die Achse, um die gedreht wird (Standard: Z).

**Kreissegment** – Ob die Kopien einen vollen 360°-Kreis (**Voll**) oder einen Teilbogen (**Bogen**) umspannen.

**Radius** – Abstand von der zentralen Achse zu jeder Kopie.

**Überstrichener Winkel** – Zu füllender Bogen in Grad (wird angezeigt, wenn Kreissegment auf „Bogen“ steht). Unterstützt Ausdrücke.

**Drehung ausrichten** – Dreht jede Kopie so, dass ihre Vorwärtsachse vom Mittelpunkt nach außen zeigt.

**Vorwärtsachse** – Welche Achse der Kopie für die Ausrichtung als „vorwärts“ gilt (wird angezeigt, wenn „Drehung ausrichten“ aktiviert ist).

## Modus: Transformation

Im Modus „Transformation“ werden die Kopien über eine manuelle Transformation oder anhand der Transformation eines anderen Objekts schrittweise versetzt.

**Anzahl** – Anzahl der Kopien (ganze Zahl oder Ausdruck).

**Transformationsreferenz** – Woher die Transformation pro Schritt stammt:
- **Eingabe** – Sie geben Verschiebung, Drehung und Skalierung direkt an.
- **Objekt** – Die Transformation wird von einem benannten gleichgeordneten Objekt übernommen.

**Verschiebung** – Versatz pro Schritt im Weltkoordinatensystem in mm (wird angezeigt, wenn die Referenz „Eingabe“ ist).

**Drehung** – Drehung pro Schritt in Grad je Achse (wird angezeigt, wenn die Referenz „Eingabe“ ist).

**Skalierung** / **Skalierungsachsen** – Gleichmäßige und achsenweise Skalierung, die bei jedem Schritt angewendet wird (wird angezeigt, wenn die Referenz „Eingabe“ ist).

**Transformationsname** – Name des gleichgeordneten Objekts, dessen Transformation als Schrittinkrement verwendet wird (wird angezeigt, wenn die Referenz „Objekt“ ist).

**Relativer Raum** – Wenn aktiviert, summiert sich die Transformation jeder Kopie im lokalen Koordinatensystem der vorherigen Kopie; wenn deaktiviert, wird jeder Schritt im Weltkoordinatensystem angewendet (wird angezeigt, wenn die Referenz „Objekt“ ist).

## Zufällige Variation

Aktivieren Sie **Zufällige Variation**, um allen Kopien Abweichungen hinzuzufügen.

- **Zufälliger Versatz** – Maximaler zufälliger Positionsversatz je Achse in mm.
- **Zufällige Drehung** – Maximale zufällige Drehung je Achse in Grad.
- **Zufällige Skalierungsachsen** – Maximale zufällige Skalierungsabweichung je Achse.
- **Erste ausschließen** – Belässt die erste Kopie an ihrer exakt berechneten Position (Standard: aktiviert).
- **Letzte ausschließen** – Belässt die letzte Kopie an ihrer exakt berechneten Position.
- **Zufallswert (Seed)** – Ändern Sie diesen Wert, um eine andere zufällige Anordnung zu erhalten. Unterstützt Ausdrücke.

## Zusammenführen

- **Einzelnes Netz erstellen** – Fasst alle Kopien zu einem zusammengeführten Netzobjekt zusammen.
- **Scheitelpunkte zusammenführen** – Verschweißt Scheitelpunkte innerhalb des Schwellenwerts für den Zusammenführungsabstand (wird angezeigt, wenn „Einzelnes Netz erstellen“ aktiviert ist).
- **Abstand** – Schwellenwert für das Zusammenführen in mm (wird angezeigt, wenn „Scheitelpunkte zusammenführen“ aktiviert ist).

## Tipps

- Verwenden Sie Ausdrücke für Anzahl, Drehung oder Endpunkt, um parametrische Muster zu erstellen
- Verwenden Sie für kreisförmige Muster den Modus „Radial“ – legen Sie mit dem Radius die Kreisgröße fest und aktivieren Sie „Drehung ausrichten“, wenn die Kopien nach außen zeigen sollen
- Kumulative Drehung im Modus „Linear“ erzeugt Spiralen und Fächer, ohne dass Winkelversätze manuell berechnet werden müssen
- „Skalierung wirkt auf Versatz“ erzeugt ganz natürlich Layouts nach Art von Nautilusschalen und geometrischen Progressionen
- Kombinieren Sie Array mit [Untergeordnetes Objekt auswählen](select-child.md), um Muster zu erstellen, in denen jede Kopie eine andere Variante zeigt

## Verwandte Themen

- [Ausrichten](../placement/align.md) – Objekte relativ zueinander positionieren
- [Untergeordnetes Objekt auswählen](select-child.md) – Eine bestimmte Kopie aus einem Array nach Index oder Name auswählen
