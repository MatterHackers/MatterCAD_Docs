---
title: Ausdrücke
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Ausdrücke

Viele Parameter in MatterCAD akzeptieren mathematische Ausdrücke anstelle einfacher Zahlen. Das ermöglicht parametrisches Konstruieren, bei dem die Änderung eines Werts zugehörige Maße automatisch aktualisiert.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Verwendung

Anstatt eine einfache Zahl in ein Parameterfeld einzugeben, können Sie einen mathematischen Ausdruck eingeben. Zum Beispiel:

- `20 + 5` ergibt 25
- `pi * 10` ergibt 31,416
- `width * 2` verweist auf einen anderen Parameter mit dem Namen „width“

## Verfügbare Konstanten

- **pi** – 3,14159… (das Verhältnis von Umfang zu Durchmesser)
- **tau** – 6,28318… (2 * pi, eine volle Umdrehung im Bogenmaß)

## Unterstützte Operationen

- Addition: `+`
- Subtraktion: `-`
- Multiplikation: `*`
- Division: `/`
- Klammern: `(` und `)` zur Gruppierung

## Tipps

- Ausdrücke werden in jedem Feld unterstützt, das `DoubleOrExpression`, `IntOrExpression` oder `StringOrExpression` im Code anzeigt – in der Praxis akzeptieren die meisten numerischen Felder in Konstruktionswerkzeugen sie
- Verwenden Sie Ausdrücke, um Beziehungen zwischen Parametern herzustellen – setzen Sie zum Beispiel den Durchmesser einer Bohrung auf `outer_diameter - 4`, damit sie immer 2 mm starke Wände hat
- Ausdrücke werden automatisch aktualisiert, wenn sich die referenzierten Werte ändern
- Verwenden Sie ein [Variablenblatt](variable-sheet.md), wenn mehrere Objekte dieselben benannten Werte oder Formeln nutzen sollen
- Sie können Ausdrücke in [Array](../operations/array/index.md)-Operationen verwenden, um parametrische Muster zu erzeugen

## Verwandte Themen

- [Komponenten](components.md) – Wiederverwendbare parametrisierte Designs erstellen
- [Variablenblatt](variable-sheet.md) – Gemeinsam genutzte Werte und Formeln für ein Design speichern
- [Objekte bearbeiten](../getting-started/editing-objects.md) – Arbeiten mit Objektparametern
