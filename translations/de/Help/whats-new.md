---
title: Neuerungen
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Neuerungen

* **Unterelemente bearbeiten**
  * Doppelklicken Sie auf ein beliebiges Objekt, um in es hineinzuwechseln und die Teile, aus denen es aufgebaut ist, direkt auf dem Druckbett zu bearbeiten
  * Eine Brotkrumennavigation zeigt an, wo Sie sich befinden — klicken Sie auf eine beliebige Ebene, um Ihre Bearbeitungen wieder zusammenzuführen
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Ein einziges boolesches Werkzeug**
  * Vereinen, Subtrahieren, Verschneiden sowie Subtrahieren und Ersetzen sind jetzt eine einzige Operation — wechseln Sie den Modus mit einem Klick, statt zu löschen und neu anzuwenden
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Boolesche Operationen, die einfach funktionieren**
  * Eine neue Engine ist schneller und kommt auch mit Netzen zurecht, die früher fehlgeschlagen sind
  * Vereinen repariert Teile mit Löchern automatisch und benennt alles, was nicht zusammengeführt werden konnte; Ebenenschnitt liefert jetzt einen wasserdichten, druckbaren Volumenkörper

* **Bessere 2D-Pfadbearbeitung**
  * Punktmodi, Live-Symmetrie mit Spiegeln, Rasterfang, Auswahl per Ziehrahmen und Esc zum Abbrechen einer Ziehbewegung
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Verbesserungen

* **Navigation** — Drücken Sie Z bei ausgewähltem 2D-Pfad für eine Bearbeitungsansicht von oben
* **Schärferer Text** — Subpixel-Textdarstellung ist jetzt automatisch aktiv, wenn Ihr Bildschirm sie unterstützt
* **Modellierung** — Linear extrudieren kann die untere Kante mit eigenem Stil, eigenem Radius und eigener Segmentanzahl abschrägen

## Wichtigste Fehlerbehebungen

* **Zuverlässigkeit beim Speichern** — Ein fehlgeschlagener Speichervorgang kann die zu ersetzende Datei nicht mehr beschädigen und meldet den Fehler
* **Cloud-Bibliothek** — Beim Speichern eines Cloud-Elements auf die Festplatte bleibt der Tab-Name erhalten, und der Tab übersteht einen Neustart
* **Laden von Dateien** — Behoben: 3MF-Teile wurden beim Laden stillschweigend verworfen
* **Pfadbearbeitung** — Behoben: Absturz beim Löschen eines Kurvenpunkts sowie Nahtpunkte, die den gewählten Modus zurücksetzten
* **Hintergrundaufgaben** — Die Schaltfläche Stopp einer laufenden Aufgabe ist jetzt anklickbar und bricht sie tatsächlich ab

## Die vollständigen Versionshinweise finden Sie [hier](release-notes.md).
