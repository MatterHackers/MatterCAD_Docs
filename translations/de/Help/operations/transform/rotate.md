---
title: Drehen
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Drehen

Drehen dreht ein Objekt um eine angegebene Achse um einen bestimmten Winkel. Sie können um jede beliebige Achsenrichtung drehen und den Mittelpunkt der Drehung wählen.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Anwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Drehen** aus dem Menü Transformieren an
3. Legen Sie den Drehwinkel und die Achse im Eigenschaften-Panel fest

Sie können Objekte auch direkt im Ansichtsfenster drehen, indem Sie auf die Drehsteuerelemente an den Ecken eines ausgewählten Objekts klicken. Wenn Sie die Maus über die Winkelanzeigen bewegen, rastet die Drehung in 45-Grad-Schritten ein.

## Parameter

- **Winkel** – Der Drehwinkel in Grad (Bereich: 3–360). Unterstützt [Ausdrücke](../../workspace/expressions.md).
- **Drehen um** – Legt die Drehachse und den Ursprungspunkt fest. Sie können um die X-, Y- oder Z-Achse drehen oder eine benutzerdefinierte Richtung angeben.

## Tipps

- Die Drehung erfolgt standardmäßig um den Mittelpunkt des Begrenzungsrahmens des Objekts
- Bei 90-Grad-Drehungen erleichtern die Einrastanzeigen das Erreichen exakter Werte
- Verwenden Sie die Operation Drehen (statt der Steuerelemente im Ansichtsfenster), wenn Sie einen präzisen Winkel benötigen, der kein Vielfaches von 45 Grad ist
- Sie können die Drehachse nach dem Anwenden der Operation ändern, indem Sie die Eigenschaft Drehen um bearbeiten

## Verwandte Themen

- [Verschieben](translate.md) – Ein Objekt um eine bestimmte Distanz verschieben
- [Skalieren](scale.md) – Die Größe eines Objekts ändern
- [Spiegeln](mirror.md) – Eine gespiegelte Kopie erstellen
