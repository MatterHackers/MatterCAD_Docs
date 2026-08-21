---
title: Unterobjekt auswählen
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Unterobjekt auswählen

Unterobjekt auswählen greift ein Unterelement aus einer Gruppe von Objekten heraus – entweder anhand einer Indexnummer oder eines Namens. Das ist besonders nützlich bei skriptgesteuerten und parametrischen Konstruktionen, in denen Sie dynamisch festlegen möchten, welches Objekt angezeigt wird.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Anwendung

1. Wählen Sie zwei oder mehr Objekte aus
2. Wenden Sie die Operation **Unterobjekt auswählen** aus dem Menü **Duplizierung** an
3. Wählen Sie **Nach Index** oder **Nach Name**, um zu steuern, wie das Unterelement ausgewählt wird
4. Legen Sie die Indexnummer oder den zu vergleichenden Namen fest

## Parameter

- **Auswahlmethode** – Wählen Sie zwischen **Nach Index** (Auswahl nach Position) und **Nach Name** (Auswahl nach Objektname). Wird als Schaltflächen dargestellt.
- **Unterelement-Index** – Der nullbasierte Index des auszuwählenden Unterelements (wird bei Verwendung von Nach Index angezeigt). Unterstützt [Ausdrücke](../../workspace/expressions.md).
- **Unterelement-Name** – Der Name des auszuwählenden Unterelements (wird bei Verwendung von Nach Name angezeigt). Unterstützt [Ausdrücke](../../workspace/expressions.md).

Liegt der Index außerhalb des gültigen Bereichs oder passt der Name zu keinem Unterelement, wird ersatzweise das erste Unterelement zurückgegeben. Sind keine Unterelemente vorhanden, wird nichts zurückgegeben.

## Verwendung im Skripting

Unterobjekt auswählen ist für die Zusammenarbeit mit Ausdrücken und der Funktion `rand()` ausgelegt, um dynamische, datengesteuerte Konstruktionen zu erstellen. Sie können beispielsweise eine Szene mit mehreren Varianten als Unterelemente aufbauen und einen Ausdruck wie `rand(42)` als Index-Startwert verwenden, um zufällig eine davon auszuwählen.

**Beispiel: Zufällige Buch-Requisiten für eine Bühnenshow**

1. Importieren Sie 5 verschiedene Buch-Meshes als Unterelemente einer Operation Unterobjekt auswählen
2. Setzen Sie die Auswahlmethode auf **Nach Index**
3. Verwenden Sie einen Ausdruck für den Unterelement-Index, etwa `floor(rand(seed) * 5)`, wobei `seed` eine Tabellenvariable ist
4. Duplizieren Sie die Operation Unterobjekt auswählen mehrfach, jeweils mit einem anderen Startwert
5. Jede Instanz wählt zufällig ein anderes Buch aus dem Satz aus

Dieses Muster funktioniert in jedem Szenario, in dem Sie aus einer Reihe von Varianten auswählen müssen: Möbel, Dekorationen, Architekturelemente oder jede Sammlung austauschbarer Teile.

## Tipps

- Kombinieren Sie die Operation mit [Array](array.md), um abwechslungsreiche Muster zu erzeugen, bei denen jede Kopie ein anderes Unterelement auswählt
- Verwenden Sie Tabellenvariablen für Index oder Name, um die Auswahl aus einer Tabelle heraus zu steuern
- Durch den Rückgriff auf das erste Unterelement bricht Ihre Konstruktion selbst dann nicht, wenn Index oder Name falsch sind

## Verwandte Themen

- [Array](array.md) – Objekte in linearen, radialen, kurvenbasierten und transformierten Mustern duplizieren
