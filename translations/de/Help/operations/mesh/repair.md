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

Reparieren behebt häufige Probleme in der Netzgeometrie, darunter nicht-mannigfaltige Kanten, Löcher, inkonsistente Flächenorientierung und nahezu deckungsgleiche Eckpunkte. Das ist besonders nützlich für importierte STL- und OBJ-Dateien, die Fehler enthalten können.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Verwendung

1. Wählen Sie ein Objekt mit Netzproblemen aus
2. Wenden Sie die Operation **Reparieren** aus dem Menü **Netz** an
3. Prüfen Sie die Statistik vor und nach der Reparatur, um zu sehen, was behoben wurde

## Statistik (schreibgeschützt)

- **Anfangs-Eckpunkte / Endpunkte** - Anzahl der Eckpunkte vor und nach der Reparatur
- **Anfangsflächen / Endflächen** - Anzahl der Flächen vor und nach der Reparatur
- **Anfängliche nicht-mannigfaltige Kanten / Finale nicht-mannigfaltige Kanten** - Anzahl der problematischen Kanten vorher und nachher

### Erweiterte Optionen

Aktivieren Sie den Modus **Erweitert** für eine feinstufige Kontrolle:

- **Punkte verschweißen** - Nahezu deckungsgleiche Eckpunkte zusammenführen (Standard: ein)
- **Verschweißtoleranz** - Wie nah Eckpunkte beieinander liegen müssen, um zusammengeführt zu werden
- **Flächenorientierung** - Dreht nach innen gestülpte Hüllen richtig herum, sodass jeder Körper als Volumenkörper gelesen wird. Jede Hülle wird für sich beurteilt, sodass ein hohles Modell seine Hohlräume behält, statt dass diese gefüllt werden. Hüllen, deren eigene Flächen sich widersprechen, werden unangetastet gelassen, statt darüber zu spekulieren, und Modelle, die nicht wasserdicht sind, greifen auf eine toleranter Reparatur zurück - führen Sie zuerst **Löcher füllen** aus, wenn die Orientierung allein sie nicht behebt.
- **Kanten verschweißen** - Kleine Risse und schlechte Nähte reparieren
- **Löcher füllen** - Lücken in der Netzoberfläche schließen
- **Entfernen-Modus** - Interne oder verdeckte Geometrie entfernen:
  - **Keine** - Gesamte Geometrie beibehalten
  - **Innenbereich** - Innenliegende Körper entfernen, die in der Hauptform verborgen sind
  - **Verdeckt** - Flächen entfernen, die von außen nicht sichtbar sind

## Tipps

- Probieren Sie zuerst Reparieren, wenn boolesche Operationen (Vereinen, Subtrahieren) bei importierten Modellen unerwartete Ergebnisse liefern
- Die Standardeinstellungen (Punkte verschweißen ein, alles andere aus) beheben die häufigsten Probleme
- Aktivieren Sie Löcher füllen, wenn Sie durch Lücken im Modell hindurchsehen können
- Verwenden Sie den Entfernen-Modus Innenbereich, um Modelle zu bereinigen, die verborgene Geometrie im Inneren haben

## Verwandte Themen

- [Dezimieren](decimate.md) - Polygonanzahl reduzieren
- [Vorhandene Objekte hinzufügen](../../getting-started/adding-existing-objects.md) - Modelle importieren, die möglicherweise repariert werden müssen
