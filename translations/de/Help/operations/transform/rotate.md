---
title: Rotieren
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Rotieren

Rotieren dreht ein Objekt um eine festgelegte Achse um einen bestimmten Winkel. Sie können um jede beliebige Achsrichtung rotieren und den Drehpunkt frei wählen.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Anwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Rotieren** aus dem Menü Transformieren an
3. Legen Sie Drehwinkel und Achse im Eigenschaften-Panel fest

Sie können Objekte auch direkt im Ansichtsfenster rotieren, indem Sie auf die Rotationsgriffe an den Ecken eines ausgewählten Objekts klicken. Wenn Sie die Maus über die Winkelanzeigen bewegen, wird auf 45-Grad-Schritte eingerastet.

## Parameter

- **Winkel** – Der Drehwinkel in Grad (Bereich: 3–360). Unterstützt [Ausdrücke](../../workspace/expressions.md).
- **Rotieren um** – Legt die Drehachse und den Ursprungspunkt fest. Sie können um die X-, Y- oder Z-Achse rotieren oder eine benutzerdefinierte Richtung angeben.

## Tipps

- Die Rotation erfolgt standardmäßig um den Mittelpunkt des Objekt-Begrenzungsrahmens
- Bei 90-Grad-Drehungen erleichtern die Einrastanzeigen das Erreichen exakter Werte
- Verwenden Sie die Operation Rotieren (anstelle der Steuerelemente im Ansichtsfenster), wenn Sie einen präzisen Winkel benötigen, der kein Vielfaches von 45 Grad ist
- Sie können die Drehachse nach dem Anwenden der Operation ändern, indem Sie die Eigenschaft „Rotieren um“ bearbeiten

## Verwandte Themen

- [Verschieben](translate.md) – Ein Objekt um eine bestimmte Distanz bewegen
- [Skalieren](scale.md) – Die Größe eines Objekts ändern
- [Spiegeln](mirror.md) – Eine gespiegelte Kopie erzeugen
