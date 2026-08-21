---
title: Select Child
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Select Child

Select Child wählt ein untergeordnetes Objekt aus einer Gruppe von Objekten aus – entweder anhand einer Indexnummer oder anhand eines Namens. Das ist besonders nützlich bei skriptgesteuerten und parametrischen Konstruktionen, in denen dynamisch festgelegt werden soll, welches Objekt angezeigt wird.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Verwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Wenden Sie die Operation **Select Child** aus dem Menü „Duplication“ an
3. Wählen Sie **Nach Index** oder **Nach Name**, um festzulegen, wie das untergeordnete Objekt ausgewählt wird
4. Legen Sie die Indexnummer oder den zu suchenden Namen fest

## Parameter

- **Auswahlmethode** – Wählen Sie zwischen **Nach Index** (Auswahl nach Position) und **Nach Name** (Auswahl nach Objektname). Wird als Schaltflächen dargestellt.
- **Kindindex** – Der nullbasierte Index des auszuwählenden untergeordneten Objekts (wird bei Verwendung von „Nach Index“ angezeigt). Unterstützt [Ausdrücke](../../workspace/expressions.md).
- **Kindname** – Der Name des auszuwählenden untergeordneten Objekts (wird bei Verwendung von „Nach Name“ angezeigt). Unterstützt [Ausdrücke](../../workspace/expressions.md).

Liegt der Index außerhalb des gültigen Bereichs oder stimmt der Name mit keinem untergeordneten Objekt überein, wird als Rückfalloption das erste untergeordnete Objekt zurückgegeben. Sind keine untergeordneten Objekte vorhanden, wird nichts zurückgegeben.

## Verwendung in Skripten

Select Child ist darauf ausgelegt, mit Ausdrücken und der Funktion `rand()` zusammenzuarbeiten, um dynamische, datengesteuerte Konstruktionen zu erstellen. Sie können beispielsweise eine Szene mit mehreren Variantenobjekten als untergeordneten Objekten aufbauen und einen Ausdruck wie `rand(42)` als Index-Startwert verwenden, um zufällig eines davon auszuwählen.

**Beispiel: Zufällige Buch-Requisiten für eine Bühnenshow**

1. Importieren Sie 5 verschiedene Buch-Meshes als untergeordnete Objekte einer Select-Child-Operation
2. Setzen Sie die Auswahlmethode auf **Nach Index**
3. Verwenden Sie für den Kindindex einen Ausdruck wie `floor(rand(seed) * 5)`, wobei `seed` eine Tabellenvariable ist
4. Duplizieren Sie die Select-Child-Operation mehrfach, jeweils mit einem anderen Startwert
5. Jede Instanz wählt zufällig ein anderes Buch aus dem Satz aus

Dieses Muster funktioniert in jedem Szenario, in dem Sie aus einer Reihe von Varianten auswählen müssen: Möbel, Dekorationen, Architekturelemente oder jede Sammlung austauschbarer Teile.

## Tipps

- Kombinieren Sie die Operation mit [Array](array.md), um abwechslungsreiche Muster zu erzeugen, bei denen jede Kopie ein anderes untergeordnetes Objekt auswählt
- Verwenden Sie Tabellenvariablen für den Index oder den Namen, um die Auswahl über eine Tabelle zu steuern
- Durch den Rückfall auf das erste untergeordnete Objekt bleibt Ihre Konstruktion auch dann funktionsfähig, wenn der Index oder der Name falsch ist

## Verwandte Themen

- [Array](array.md) – Objekte in linearen, radialen, kurvenbasierten und Transformationsmustern duplizieren
