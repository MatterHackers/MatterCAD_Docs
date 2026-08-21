---
title: Reparieren
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Reparieren

Reparieren behebt häufige Probleme in der Mesh-Geometrie, darunter nicht-mannigfaltige Kanten, Löcher, uneinheitliche Flächenausrichtung und nahezu deckungsgleiche Vertices. Das ist besonders bei importierten STL- und OBJ-Dateien nützlich, die Fehler enthalten können.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Verwendung

1. Wählen Sie ein Objekt mit Mesh-Problemen aus
2. Wenden Sie die Operation **Reparieren** aus dem Menü Mesh an
3. Prüfen Sie die Statistiken vor und nach der Reparatur, um zu sehen, was behoben wurde

## Statistiken (schreibgeschützt)

- **Vertices vorher / Vertices nachher** - Anzahl der Vertices vor und nach der Reparatur
- **Flächen vorher / Flächen nachher** - Anzahl der Flächen vor und nach der Reparatur
- **Nicht-mannigfaltige Kanten vorher / Nicht-mannigfaltige Kanten nachher** - Anzahl der problematischen Kanten vor und nach der Reparatur

### Erweiterte Optionen

Aktivieren Sie den Modus **Erweitert** für eine feinere Steuerung:

- **Vertices verschweißen** - Nahezu deckungsgleiche Vertices zusammenführen (Standard: ein)
- **Schweißtoleranz** - Wie nah Vertices beieinander liegen müssen, um zusammengeführt zu werden
- **Flächenausrichtung** - Dreht nach innen gestülpte Hüllen richtig herum, sodass jeder Körper als solide erkannt wird. Jede Hülle wird für sich beurteilt, sodass ein hohles Modell seine Hohlräume behält, statt dass diese aufgefüllt werden. Hüllen, deren eigene Flächen sich widersprechen, bleiben unverändert, statt dass geraten wird, und bei Modellen, die nicht wasserdicht sind, wird auf eine tolerantere Reparatur zurückgegriffen - führen Sie zuerst **Löcher füllen** aus, wenn die Ausrichtung allein das Problem nicht behebt.
- **Kanten verschweißen** - Kleine Risse und fehlerhafte Nähte reparieren
- **Löcher füllen** - Lücken in der Mesh-Oberfläche schließen
- **Entfernungsmodus** - Innenliegende oder verdeckte Geometrie entfernen:
  - **Keine** - Gesamte Geometrie beibehalten
  - **Innenliegend** - Innere Körper entfernen, die in der Hauptform verborgen sind
  - **Verdeckt** - Flächen entfernen, die von außen nicht sichtbar sind

## Tipps

- Versuchen Sie es zuerst mit Reparieren, wenn boolesche Operationen (Vereinigen, Subtrahieren) bei importierten Modellen unerwartete Ergebnisse liefern
- Die Standardeinstellungen (Vertices verschweißen ein, alles andere aus) beheben die häufigsten Probleme
- Aktivieren Sie Löcher füllen, wenn Sie durch Lücken im Modell hindurchsehen können
- Verwenden Sie Innenliegend entfernen, um Modelle zu bereinigen, die verborgene Geometrie im Inneren enthalten

## Verwandte Themen

- [Dezimieren](decimate.md) - Polygonanzahl reduzieren
- [Vorhandene Objekte hinzufügen](../../getting-started/adding-existing-objects.md) - Modelle importieren, die möglicherweise repariert werden müssen
