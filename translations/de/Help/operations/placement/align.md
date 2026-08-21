---
title: Ausrichten
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Ausrichten

Mit Ausrichten werden mehrere Objekte präzise relativ zu einem Ankerobjekt positioniert. Verwenden Sie diese Funktion, um Kanten bündig zu setzen, Teile zueinander zu zentrieren, ein Objekt auf einem anderen zu platzieren oder gleichmäßig verteilte Stapel zu erzeugen.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus.
2. Wenden Sie die Operation **Ausrichten** aus dem Menü **Platzierung** an.
3. Wählen Sie das **Anker**-Objekt. Der Anker bleibt an seiner Position, die übrigen Objekte werden bewegt.
4. Legen Sie die Ausrichtung für die X-, Y- und Z-Achse unabhängig voneinander fest.
5. Verwenden Sie **Übernehmen**, wenn Sie die ausgerichteten Positionen fest in den Objektbaum schreiben möchten.

## Parameter

### Anker

In der Liste **Anker** wählen Sie das untergeordnete Objekt aus, das als Referenz dient. Der Anker bewegt sich nicht. Jedes andere untergeordnete Objekt der Operation Ausrichten wird relativ zum Anker neu positioniert, sofern eine Achse nicht den Modus **Gestapelt** verwendet.

### Achsensteuerungen

Jede Achse besitzt eigene Steuerelemente. Sie können auf einer Achse, auf zwei Achsen oder auf allen drei Achsen ausrichten. Die minimalen und maximalen Kanten sind nach der jeweiligen Achse benannt:

- **X-Achse** – Min ist links, Max ist rechts.
- **Y-Achse** – Min ist vorne, Max ist hinten.
- **Z-Achse** – Min ist unten, Max ist oben.

Für jede Achse gilt:

- **Ausrichten** – Legt den Referenzpunkt des Ankers für diese Achse fest. Mit **Keine** bleiben die Positionen auf dieser Achse unverändert.
- **Modus** – Steuert, wie die gewählte Ausrichtung angewendet wird:
  - **Einfach** – Bringt die entsprechende Kante, Mitte oder den Ursprung jedes bewegten Objekts mit dem Anker zur Deckung. Es wird kein Versatz verwendet.
  - **Versatz** – Wählen Sie, welcher Teil des bewegten Objekts auf der Ankerreferenz landen soll, und ergänzen Sie den Abstand über **Versatz**.
  - **Gestapelt** – Platziert die Objekte entlang dieser Achse nacheinander und verwendet **Versatz** als Abstand zwischen ihnen.
- **Unterausrichtung** – Im Modus **Versatz** verfügbar. Legt den Teil des bewegten Objekts fest, der auf der Ankerreferenz platziert wird. Steht **Unterausrichtung** auf **Keine**, verwendet Ausrichten dieselbe Kante, Mitte oder denselben Ursprung, die bzw. der unter **Ausrichten** gewählt wurde.
- **Versatz** – In den Modi **Versatz** und **Gestapelt** verfügbar. Fügt entlang dieser Achse einen Abstand hinzu und unterstützt [Ausdrücke](../../workspace/expressions.md).

## Ausrichtungsmodi

### Einfach

Verwenden Sie **Einfach**, wenn gleichartige Positionen zur Deckung gebracht werden sollen. Beispiel: **X-Ausrichtung: Mitte** verschiebt jedes Objekt außer dem Anker so, dass seine X-Mitte mit der X-Mitte des Ankers übereinstimmt. **Z-Ausrichtung: Min** verschiebt jedes Objekt außer dem Anker so, dass seine Unterseite auf der Höhe der Unterseite des Ankers liegt.

### Versatz

Verwenden Sie **Versatz**, wenn sich der maßgebliche Teil des bewegten Objekts von der Ankerreferenz unterscheiden soll. Um beispielsweise ein Objekt auf dem Anker zu platzieren:

1. Setzen Sie **Z-Ausrichtung** auf **Max** (oben).
2. Setzen Sie **Z-Modus** auf **Versatz**.
3. Setzen Sie **Z-Unterausrichtung** auf **Unten**.
4. Setzen Sie **Z-Versatz** auf den gewünschten Abstand oder belassen Sie ihn bei `0` für direkten Kontakt.

Dadurch wird die Unterseite des bewegten Objekts an der Oberseite des Ankers platziert, wahlweise mit Abstand.

### Gestapelt

Verwenden Sie **Gestapelt**, um mehrere Objekte entlang einer Achse aneinanderzureihen. Die Objekte werden nach Namen und anschließend nach interner ID verarbeitet; eine klare Benennung sorgt daher für eine vorhersehbare Stapelreihenfolge.

Im Modus **Gestapelt** wird jedes bewegte Objekt an der vorherigen Referenz dieser Achse angesetzt:

- Die Ausrichtung **Min** stapelt in positive Richtung, etwa von links nach rechts auf X oder von unten nach oben auf Z.
- Die Ausrichtung **Max** stapelt in negative Richtung, etwa von rechts nach links auf X oder von oben nach unten auf Z.
- Die Ausrichtungen **Mitte** und **Ursprung** verwenden den Abstand zwischen der Mitte bzw. dem Ursprung der einzelnen Objekte.

Verwenden Sie **Versatz** im Modus **Gestapelt**, um den Abstand zwischen den Objekten festzulegen.

## Beispiele

- **Objekte auf der Druckbettfläche zentrieren** – Wählen Sie das Objekt, das fixiert bleiben soll, als **Anker** und setzen Sie **X-Ausrichtung** und **Y-Ausrichtung** auf **Mitte**.
- **Ein Objekt auf einem anderen platzieren** – Setzen Sie **Z-Ausrichtung** auf **Max** (oben), **Z-Modus** auf **Versatz** und **Z-Unterausrichtung** auf **Unten**.
- **Einen präzisen Abstand zu einer Kante hinzufügen** – Verwenden Sie den Modus **Versatz**, wählen Sie mit **Unterausrichtung** die Kante des bewegten Objekts und setzen Sie **Versatz** auf den benötigten Abstand.
- **Mehrere Objekte hintereinander aufreihen** – Setzen Sie **X-Ausrichtung** auf **Min** (links), **X-Modus** auf **Gestapelt** und verwenden Sie **X-Versatz** für den Abstand.
- **Einen vertikalen Stapel aufbauen** – Setzen Sie **Z-Ausrichtung** auf **Min** (unten), **Z-Modus** auf **Gestapelt** und verwenden Sie **Z-Versatz** für den Abstand zwischen den Objekten.

## Tipps

- Das Ankerobjekt bleibt an seiner Position; die anderen Objekte bewegen sich, um sich daran auszurichten.
- Sie können auf verschiedenen Achsen unterschiedliche Modi verwenden, etwa **Gestapelt** auf X und gleichzeitig **Mitte** mit **Einfach** auf Y.
- Nutzen Sie Objektnamen, um die Reihenfolge bei **Gestapelt** zu steuern, wenn mehrere Objekte gleichzeitig ausgerichtet werden.
- Ausrichten ist bis zum Übernehmen nicht destruktiv. Sie können die Einstellungen jederzeit ändern, um die untergeordneten Objekte neu auszurichten.
- Verwenden Sie **Ursprung**, wenn Sie Modellierungsursprünge statt Begrenzungsrahmenkanten aufeinander ausrichten möchten.

## Verwandte Themen

- [An Grenzen anpassen](fit-to-bounds.md) – Ein Objekt auf bestimmte Abmessungen skalieren
- [Verschieben](../transform/translate.md) – Um eine bestimmte Distanz bewegen
- [Gruppieren](../../workspace/grouping.md) – Ausgerichtete Objekte gruppieren, damit sie zusammenbleiben
