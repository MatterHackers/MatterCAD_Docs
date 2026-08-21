---
title: Rückgängig und Wiederherstellen
parent: "Workspace"
nav_order: 9
source_hash: a24c28c5640a8b59a836047f26dbbf0019de92c2
source_lang: en
---
# Rückgängig und Wiederherstellen

MatterCAD speichert einen vollständigen Verlauf Ihrer Änderungen, sodass Sie Fehler rückgängig machen und zurückgenommene Aktionen wiederherstellen können.

## Verwendung

- **Strg + Z** – Letzte Aktion rückgängig machen
- **Strg + Y** oder **Strg + Umschalt + Z** – Letzte rückgängig gemachte Aktion wiederherstellen
- Sie können auch die Schaltflächen **Undo** und **Redo** in der Symbolleiste verwenden

## Was rückgängig gemacht werden kann

Alle Konstruktionsvorgänge werden im Rückgängig-Verlauf erfasst, darunter:

- Hinzufügen oder Löschen von Objekten
- Verschieben, Drehen und Skalieren von Objekten
- Anwenden von Operationen (Boolesche Operationen, Transformationen, Umformungen usw.)
- Ändern von Objektparametern
- Gruppieren und Gruppierung aufheben

## Tipps

- Durch wiederholtes Drücken von Strg + Z können Sie mehrere Schritte rückgängig machen
- Der Rückgängig-Verlauf wird für die aktuelle Sitzung geführt. Beim Schließen und erneuten Öffnen einer Konstruktion beginnt ein neuer Verlauf.
- Wenn Sie mehrere Schritte rückgängig machen und anschließend eine neue Änderung vornehmen, wird der Wiederherstellungsverlauf ab diesem Punkt gelöscht

## Verwandte Themen

- [Tastenkombinationen](keyboard-shortcuts.md) – Alle verfügbaren Tastenkombinationen
- [Objekte bearbeiten](../getting-started/editing-objects.md) – Arbeiten mit Objekten im Ansichtsfenster
