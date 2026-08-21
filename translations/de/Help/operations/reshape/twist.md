---
title: Verdrehen
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Verdrehen

Verdrehen dreht die Oberseite eines Objekts relativ zur Unterseite und erzeugt so einen spiralförmigen bzw. verdrehten Effekt über die Höhe. Standardmäßig verläuft die Drehung gleichmäßig von unten nach oben; unter „Erweitert“ können Sie zeichnen, an welcher Stelle der Höhe die Drehung tatsächlich stattfindet.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Verdrehen** aus dem Menü Umformen an
3. Legen Sie den Verdrehwinkel fest und passen Sie die Unterteilungen für ein gleichmäßiges Ergebnis an
4. Aktivieren Sie **Erweitert**, wenn Sie zeichnen möchten, wie die Verdrehung über die Höhe des Bauteils verteilt wird

## Das Verdrehungsprofil

Unter „Erweitert“ bestimmt die Kurve **Verdrehungsprofil**, wo die Verdrehung stattfindet. Der Gesamtbetrag der Verdrehung wird weiterhin über die Einstellung Winkel (bzw. Rotationsdistanz) festgelegt – die Kurve verteilt ihn lediglich:

- **Entlang der Kurve nach oben** ist die Höhe am Bauteil in Prozent – 0 unten, 100 oben. Eine Hilfslinie quer durch den Editor markiert 100 Prozent und ist mit der tatsächlichen Höhe des Bauteils in mm beschriftet.
- **Quer zur Kurve** ist der Prozentsatz der gesamten Verdrehung, der bei dieser Höhe erreicht ist – 0 für gar keine, 100 für die vollständige.

Ein neues Verdrehen beginnt mit einer geraden Diagonalen von 0 bis 100 – das ist genau die gleichmäßige Verdrehung, die Sie auch ganz ohne „Erweitert“ erhalten.

Ein waagerechter Abschnitt in der Kurve ist ein Bereich des Bauteils, der nicht verdreht wird. Wo die Kurve nicht die gesamte Höhe abdeckt, wird ihr jeweils nächstgelegenes Ende gehalten; eine Kurve, die nur zwischen 40 und 60 Prozent gezeichnet ist, lässt das Bauteil darunter und darüber also starr – so beginnen und beenden Sie eine Verdrehung auf halber Höhe.

Ein Abschnitt, der nach oben hin wieder abfällt, dreht zurück: Dieser Bereich des Bauteils dreht sich in die andere Richtung, zurück in Richtung Ausgangslage. Indem Sie das Profil über 100 hinaus und anschließend wieder nach unten zeichnen, überschreiten Sie den Gesamtwert und kehren zu ihm zurück.

## Parameter

- **Rotationstyp** – Auswahl zwischen:
  - **Winkel** – Gesamten Verdrehwinkel in Grad angeben (3–360)
  - **Distanz** – Verdrehung als Distanz entlang des Umfangs angeben
- **Unterteilungen** – Anzahl der horizontalen Schnitte, die für eine gleichmäßige Verdrehung hinzugefügt werden, gleichmäßig über die Höhe verteilt. Mehr Unterteilungen = gleichmäßigere Verdrehung
- **Mindestanzahl Seiten** – Die kleinste Anzahl an Seiten, die das Bauteil um die Verdrehachse herum haben soll. Eine grobe Form wie ein Würfel besitzt entlang ihres Umfangs keine Geometrie, die die Drehung mitträgt, sodass ihre ebenen Flächen facettiert wirken, statt sich zu krümmen; dies fügt vertikale Schnitte durch die Verdrehachse hinzu, damit diese Flächen der Verdrehung folgen können. 0 (der Standardwert) lässt das Bauteil unverändert
- **Nach rechts verdrehen** – Richtung der Verdrehung: rechts (im Uhrzeigersinn) oder links (gegen den Uhrzeigersinn)
- **Bevorzugter Radius** – Schreibgeschützt: der Radius, den das Bauteil selbst meldet, oder der sich aus seiner Form ergibt – um diesen Radius wird eine Verdrehdistanz gemessen (nur im Modus Distanz)
- **Radius bearbeiten** – Den gemeldeten Radius deaktivieren, damit Sie einen eigenen festlegen können (nur im Modus Distanz und nur, wenn das Bauteil einen Radius meldet)
- **Radius überschreiben** – Benutzerdefinierter Radius für die Verdrehungsberechnung (nur im Modus Distanz)

### Erweiterte Parameter

- **Verdrehungsprofil** – Der oben beschriebene Kurveneditor: der Prozentsatz der gesamten Verdrehung, der auf jeder Höhe (in Prozent) erreicht wird
- **Rotationsversatz** – Verschiebt das Zentrum, um das das Bauteil gedreht wird, aus der Mitte des Bauteils heraus

## Tipps

- Höhere Werte für Unterteilungen liefern gleichmäßigere Ergebnisse, erzeugen aber mehr Geometrie
- Wirkt ein verdrehter Würfel oder eine andere Form mit ebenen Seiten facettiert statt gekrümmt, erhöhen Sie die Mindestanzahl Seiten
- Zeichnen Sie das Profil unten flach und erst danach ansteigend, um unter einer verdrehten Säule einen geraden Sockel zu erhalten
- Eine Verdrehung um 90 Grad an einer quadratischen Säule erzeugt einen eleganten architektonischen Effekt
- Zeichnen Sie zwei flache Abschnitte, die durch einen kurzen Anstieg verbunden sind, um die Mitte des Bauteils zu verdrehen und beide Enden starr zu lassen

## Verwandte Themen

- [Krümmen](curve.md) – Ein Objekt zu einem Bogen biegen
- [Einschnüren](pinch.md) – Zur Mitte hin zusammendrücken
- [Radiales Einschnüren](radial-pinch.md) – Das Profil auf dieselbe Weise mit einer Kurve formen
