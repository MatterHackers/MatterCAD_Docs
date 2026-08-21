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

Verdrehen dreht die Oberseite eines Objekts relativ zur Unterseite und erzeugt so einen spiralförmigen oder verdrehten Effekt über die Höhe. Standardmäßig nimmt die Drehung von unten nach oben gleichmäßig zu; unter Erweitert können Sie zeichnen, an welcher Stelle der Höhe die Drehung tatsächlich stattfindet.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Verdrehen** aus dem Menü Umformen an
3. Legen Sie den Verdrehwinkel fest und passen Sie die Schnitte für ein glatteres Ergebnis an
4. Aktivieren Sie **Erweitert**, wenn Sie zeichnen möchten, wie die Verdrehung über das Bauteil verteilt wird

## Das Verdrehungsprofil

Unter Erweitert bestimmt die Kurve **Verdrehungsprofil**, wo die Verdrehung stattfindet. Der Gesamtbetrag der Verdrehung wird weiterhin über das Steuerelement Winkel (bzw. Rotationsdistanz) festgelegt – die Kurve verteilt ihn lediglich:

- **Entlang der Kurve nach oben** ist die Höhe am Bauteil in Prozent – 0 unten, 100 oben. Eine Hilfslinie quer durch den Editor markiert 100 Prozent und ist mit der tatsächlichen Höhe des Bauteils in mm beschriftet.
- **Quer zur Kurve** ist der Prozentsatz der Gesamtverdrehung, der bei dieser Höhe erreicht ist – 0 für keinen Anteil, 100 für den vollen Anteil.

Ein neues Verdrehen beginnt mit einer geraden Diagonalen von 0 nach 100, was genau der gleichmäßigen Verdrehung entspricht, die Sie auch ganz ohne Erweitert erhalten.

Ein waagerechter Abschnitt der Kurve ist ein Band des Bauteils, das sich nicht verdreht. Wo die Kurve nicht die volle Höhe abdeckt, wird ihr jeweils nächstliegender Endwert gehalten; eine Kurve, die nur zwischen 40 und 60 Prozent gezeichnet ist, lässt das Bauteil darunter und darüber also unverdreht – so beginnen und beenden Sie eine Verdrehung auf halber Höhe.

Ein Abschnitt, der nach oben hin wieder abfällt, dreht zurück: Dieses Band des Bauteils dreht sich in die andere Richtung, zurück zu seiner Ausgangslage. Das Profil über 100 hinaus und dann wieder nach unten zu zeichnen, ist die Art und Weise, den Gesamtwert zu überschreiten und wieder zu ihm zurückzukehren.

## Parameter

- **Rotationstyp** – Wählen Sie zwischen:
  - **Winkel** – Geben Sie den gesamten Verdrehwinkel in Grad an (3–360)
  - **Abstand** – Geben Sie die Verdrehung als Strecke entlang des Umfangs an
- **Schnitte** – Anzahl der horizontalen Schnitte, die für eine gleichmäßige Verdrehung hinzugefügt und gleichmäßig über die Höhe des Bauteils verteilt werden. Mehr Schnitte = weichere Verdrehung
- **Minimale Seitenanzahl** – Die geringste Anzahl an Seiten, die das Bauteil um die Verdrehachse herum haben soll. Eine grobe Form wie ein Würfel besitzt entlang ihres Umfangs keine Geometrie, die die Drehung tragen könnte, sodass ihre ebenen Flächen facettieren statt sich zu krümmen; dies fügt vertikale Schnitte durch die Verdrehachse hinzu, damit diese Flächen der Verdrehung folgen können. 0 (der Standardwert) lässt das Bauteil unverändert
- **Nach rechts verdrehen** – Richtung der Verdrehung: rechts (im Uhrzeigersinn) oder links (gegen den Uhrzeigersinn)
- **Bevorzugter Radius** – Schreibgeschützt: der Radius, den das Bauteil selbst meldet, oder der aus seiner Form abgeleitete Radius, um den herum ein Verdrehabstand gemessen wird (nur im Modus Abstand)
- **Radius bearbeiten** – Schaltet den gemeldeten Radius aus, damit Sie einen eigenen festlegen können (nur im Modus Abstand und nur, wenn das Bauteil einen Radius meldet)
- **Radius überschreiben** – Benutzerdefinierter Radius für die Verdrehungsberechnung (nur im Modus Abstand)

### Erweiterte Parameter

- **Verdrehungsprofil** – Der oben beschriebene Kurveneditor: der Prozentsatz der Gesamtverdrehung, der bei jeder Höhe in Prozent erreicht ist
- **Drehversatz** – Verschiebt das Zentrum, um das das Bauteil gedreht wird, aus der Mitte des Bauteils heraus

## Tipps

- Höhere Werte für Schnitte liefern glattere Ergebnisse, erzeugen aber mehr Geometrie
- Wenn ein verdrehter Würfel oder eine andere flächige Form facettiert statt gekrümmt aussieht, erhöhen Sie die Minimale Seitenanzahl
- Zeichnen Sie das Profil unten waagerecht und danach ansteigend, um unter einer verdrehten Säule einen geraden Sockel zu erhalten
- Eine Verdrehung um 90 Grad an einer quadratischen Säule erzeugt einen eleganten architektonischen Effekt
- Zeichnen Sie zwei waagerechte Abschnitte, die durch einen kurzen Anstieg verbunden sind, um die Mitte des Bauteils zu verdrehen und beide Enden unverdreht zu lassen

## Verwandte Themen

- [Kurve](curve.md) – Ein Objekt zu einem Bogen biegen
- [Einschnüren](pinch.md) – Zur Mitte hin zusammendrücken
- [Radiale Einschnürung](radial-pinch.md) – Das Profil auf dieselbe Weise mit einer Kurve formen
