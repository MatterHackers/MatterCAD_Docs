---
title: Versionshinweise
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13. August 2026)
[Windows-Download](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Neue Funktionen

* **Unterobjekte bearbeiten**
  * Doppelklicken Sie auf ein Objekt auf dem Druckbett oder im Szenenbaum, um in es hineinzuwechseln und die Teile zu bearbeiten, aus denen es aufgebaut ist – ohne separates Fenster und ohne zusätzlichen Tab
  * Bei Operationen wie Subtrahieren bearbeiten Sie die Ausgangsteile, und das Ergebnis wird neu aufgebaut, sobald Sie die Ebene wieder verlassen
  * Ein Brotkrumenpfad oben im Szenenbaum zeigt den vollständigen Pfad an; ein Klick auf eine Ebene fasst Ihre Änderungen zu einem einzigen rückgängig machbaren Schritt zusammen, und jede Ebene behält ihren eigenen Undo-Verlauf
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Ein einziges boolesches Werkzeug**
  * Vereinigen, Subtrahieren, Schnittmenge sowie Subtrahieren und Ersetzen sind jetzt eine einzige Operation mit einer Symbolreihe oben im Bedienfeld – wechseln Sie den Modus per Klick, statt zu löschen und neu anzuwenden
  * Dieselbe Operation verarbeitet sowohl 3D-Meshes als auch 2D-Pfade und zeigt den Fortschritt an, während eine aufwendige boolesche Berechnung läuft
  * Designs, die mit den früheren separaten booleschen Objekten gespeichert wurden, lassen sich weiterhin normal öffnen
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Boolesche Operationen, die einfach funktionieren**
  * Boolesche Operationen laufen auf einer neuen nativen Engine, die schneller ist und auch bei Meshes gelingt, die zuvor fehlgeschlagen sind
  * Vereinigen repariert Teile mit Löchern automatisch: saubere Reparaturen gehen in die Vereinigung ein, Teile, die sich nicht sicher zusammenführen lassen, bleiben daneben erhalten und werden für Sie benannt, und ein Teil, das nicht repariert werden konnte, behält Ihre ursprüngliche Geometrie
  * Ebenenschnitt ist jetzt eine echte Volumenverschneidung, sodass das Ergebnis wasserdicht und druckbar ist statt einer offenen Hülle
  * Neue Optionen „Umgestülpte Geometrie beibehalten“ und „Umlaufrichtung reparieren“ für problematische importierte Meshes


## Verbesserungen

* **2D-Pfad-Editor**
  * Vier Punktmodi – Scharf, Symmetrisch, Ausgerichtet und Frei – mit einem Klick angewendet, sowohl im 2D-Editor als auch in der 3D-Ansicht
  * Spiegeln ist jetzt ein Live-Symmetriemodus: Änderungen werden während der Bearbeitung an der Mitte gespiegelt, und wenn Sie ein gespiegeltes Punktpaar auf die Achse ziehen, wird es zu einem einzigen Punkt verschmolzen
  * Punkte per Auswahlrahmen markieren, als Gruppe verschieben, am Raster einrasten und mit Esc ein Ziehen abbrechen
  * Glätten legt in einem Schritt eine Kurve durch Ihre gesetzten Punkte
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Ansicht und Navigation**
  * Drücken Sie Z bei ausgewähltem flachem Pfad, um animiert in eine senkrechte Bearbeitungsansicht zu wechseln, die auf den Pfad eingepasst ist
  * Die Subpixel-Textdarstellung wird jetzt automatisch aktiviert, wenn Ihr Display sie unterstützt, und lässt sich weiterhin unter den erweiterten Einstellungen ein- oder ausschalten

* **Modellierung**
  * Linear extrudieren kann die untere Kante mit eigenem Stil, Radius und eigener Segmentanzahl abschrägen
  * Nur im Editor sichtbare Objekte (3D-Kurve, Messwerkzeug, Beschreibung, Tabelle) werden weiterhin angezeigt, aber vom Export ausgeschlossen

## Wichtigste Fehlerbehebungen

  * Ein Speichervorgang, der auf halbem Weg fehlschlug, konnte die zu ersetzende Datei abschneiden und trotzdem Erfolg melden. Speichervorgänge werden jetzt vollständig abgeschlossen und ersetzen das Ziel anschließend atomar – derselbe Schutz gilt für Bibliotheks-Speicherungen und Exporte
  * Ein fehlgeschlagener Speichervorgang lässt das Design als ungespeichert markiert, sodass das Schließen der Anwendung Ihre Arbeit nicht stillschweigend verwerfen kann
  * Beim Speichern eines Cloud-Elements auf die Festplatte blieb der alte Tab-Name erhalten und der Tab ging beim Neustart verloren
  * Behoben: 3MF-Teilmodelle wurden beim Laden stillschweigend verworfen, und gleichzeitig geladene 3MF-Dateien haben sich gegenseitig beeinflusst
  * Behoben: Abstürze, ein fehlerhafter Histogrammfilter und Kopien eines Bildteils, die nicht mit dem Original synchron blieben
  * Behoben: ein Absturz beim Löschen eines Kurvenpunkts sowie Punkte an der Naht eines geschlossenen Pfads, die den von Ihnen gewählten Modus zurücksetzten
  * Die Schaltfläche „Stopp“ bei einer laufenden Aufgabe ist jetzt anklickbar und bricht den Vorgang tatsächlich ab

---

# MatterCAD 2.2026.5 (8. Mai 2026)
[Windows-Download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Neue Funktionen

* **Neu gestaltetes Array-Werkzeug**
  * Eine einzige vereinheitlichte Array-Operation ersetzt das bisherige lineare Array, radiale Array und erweiterte Array
  * Modus **Linear**: Kopien entlang einer Richtung mit optionaler Rotation und fortschreitender Skalierung
  * Modus **Radial**: Kopien um eine zentrale Achse mit konfigurierbarem Radius, Öffnungswinkel sowie Bogen- oder Vollkreismustern
  * Modus **Transformation**: schrittweise Kopien über eine manuelle Transformation oder die Transformation eines benannten Geschwisterobjekts
  * Der kumulative Rotationsmodus im linearen Modus erzeugt ganz natürlich Spiralen, Fächer und Helices
  * Option „Skalierung beeinflusst Versatz“ für Layouts nach Art von Nautilusmuscheln und geometrischen Progressionen
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Bibliotheks-Favoriten**
  * Markieren Sie ein beliebiges Bibliothekselement mit einem Stern, um es einem dauerhaften Favoriten-Ordner hinzuzufügen
  * Greifen Sie schnell von einer Stelle aus auf Ihre meistgenutzten Grundkörper, Generatoren und gespeicherten Teile zu
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Verbesserungen

* **Ausrichten**
  * Die gestapelte Ausrichtung ist jetzt eine direkte Modus-Schaltfläche statt einer Dropdown-Option
  * Klarere Modi Einfach, Versatz und Gestapelt für das Ausrichten von Kanten, das Einfügen präziser Abstände und das Erstellen geordneter Stapel
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Dateiunterstützung**
  * Unterstützung für das Bildformat WEBP in bildbasierten Operationen hinzugefügt
  * Verbesserte Auswertung von SVG-Dateien für zuverlässigere Importe

* **Zuverlässigkeit**
  * Schnelleres und zuverlässigeres Laden von 3MF-Dateien
  * Bessere Wiederherstellung von Tabs zwischen Sitzungen

## Wichtigste Fehlerbehebungen

* **Anmeldung und Zugriff auf die Cloud-Bibliothek**
  * Anmeldung und Zugriff auf die Cloud-Bibliothek funktionieren wieder, nachdem ein Backend-Server-Upgrade die Anmeldung unterbrochen hatte.
  * MatterCAD fordert Sie jetzt zur erneuten Anmeldung auf, wenn beim Cloud-Zugriff abgelaufene oder ungültige Anmeldedaten festgestellt werden.

* **Auswahl im Szenenbaum**
  * Behoben: uneinheitliches Auswahlverhalten beim Auswählen von Objekten im Szenenbaum.

* **Navigation in der Hilfe**
  * Behoben: Navigationsprobleme in der mitgelieferten Hilfe und in der Versionsdokumentation.

* **Rechtsklick in der Bibliothek**
  * Behoben: Rechtsklick-Verhalten in der Baumansicht der Bibliothek.

* **Tabellen**
  * Behoben: ein Absturz, der beim Arbeiten mit Tabellen auftreten konnte.

---

# MatterCAD 2.2026.3 (12. März 2026)
[Windows-Download](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Neue Funktionen

* **Völlig neue Direct3D-11-Rendering-Engine**
  * Vollständige Umstellung von OpenGL auf Direct3D 11 für deutlich bessere Leistung
  * FXAA-Kantenglättung für scharfe, saubere Kanten
  * Duales Depth Peeling für korrekte reihenfolgeunabhängige Transparenz
  * Hardwarebeschleunigte Schatten auf dem Druckbett
  * Verbesserte Objektumrisse und Auswahldarstellung
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Objekttransparenz**
  * Alpha/Transparenz für jedes einzelne Objekt in der Szene einstellen
  * Meshes mit flächenweisen Farben unterstützen Alpha ohne Farbverfälschung
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Objekte sperren und ausblenden**
  * Objekte sperren, um versehentliches Auswählen oder Bearbeiten zu verhindern
  * Objekte ausblenden, um die Ansicht beim Arbeiten an bestimmten Teilen übersichtlich zu halten
  * Befehle „Alle einblenden“ und „Alle entsperren“ zum schnellen Wiederherstellen der Sichtbarkeit
  * Gesperrte und ausgeblendete Objekte werden korrekt von der strahlenbasierten Auswahl ausgeschlossen
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Verbessertes boolesches Subtrahieren**
  * Mehrfach-Subtraktionen sind deutlich zuverlässiger und genauer

## Verbesserungen

* **Dateiverarbeitung**
  * Projekte werden jetzt standardmäßig als 3MF statt als STL gespeichert und behalten dabei Farben, Materialien und den Design-Verlauf bei
  * Verbesserte Drag-and-drop-Unterstützung für Dateien und Ordner in die 3D-Ansicht

* **Arbeitsablauf**
  * Die Dialoge „Speichern unter“ und „Verschieben“ merken sich den zuletzt verwendeten Ordner
  * Ausdrucksfelder unterstützen jetzt `pi`, `tau`, `e` und `count`
  * Die Esc-Taste macht Aktionen in Design-Bearbeitungskontexten rückgängig
  * Die 3D-Steuerelemente bleiben sichtbar, wenn die Maus die Szene verlässt

* **Leistung & Stabilität**
  * Behoben: Abstürze beim Start und Probleme mit rekursivem Laden
  * Behoben: Rendering-Fehler bei Beleuchtung und Mipmapping
  * Verbesserte Aktualisierung der Baumansicht der Bibliothek
  * Dynamische Berechnung der Nah- und Fernebene für besseres Zoomverhalten
  * Aktualisierung auf .NET 10

---

# MatterCAD 2.2025.6 (20. Juni 2025)
[Windows-Download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Neue Funktionen

* **Unterstützung für SVG-Dateien**  
  * Vollständige Drag-and-drop-Unterstützung für SVG-Dateien
  * Direkte Umwandlung von SVG-Grafiken in 3D-Objekte
  * Nahtlose Integration in bestehende CAD-Arbeitsabläufe

* **Erweiterte Verarbeitung von OBJ-Dateien**  
  * Unterstützung für das Laden von Materialien aus ZIP-Archiven
  * Verbesserte Auswertung von OBJ-Dateien und Materialverarbeitung
  * Bessere Unterstützung komplexer 3D-Modelle mit mehreren Materialien

* **Verbessertes Tab-Verwaltungssystem**
  * Tabs der Cloud-Bibliothek bleiben jetzt korrekt erhalten – Ihre Arbeit bleibt genau dort, wo Sie sie verlassen haben
  * Verbesserte Organisation und Navigation der Tabs
  * Automatische Wiederherstellung geöffneter Tabs zwischen Sitzungen

## Verbesserungen der Benutzerfreundlichkeit

* **Optimierte Oberfläche**
  * Neu organisiertes Menü „Zuletzt verwendet“ für schnelleren Zugriff
  * Besseres visuelles Feedback bei langen Vorgängen
  * Verbesserte Startzeit und Reaktionsfähigkeit der Anwendung

* **Zuverlässigkeit**
  * Behoben: kritische Abstürze bei Interaktionen in der 3D-Szene
  * Behoben: Probleme bei der Speicherverwaltung
  * Verbesserte Stabilität der Anwendung auf allen Plattformen

---

# MatterCAD 2.21.5 (13. Feb. 2025)

[Windows-Download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Bestehende Funktionen

*Die folgenden Funktionen bilden die Grundlage, auf der MatterCAD aus dem Erbe von MatterControl aufbaut:*

* Funktion „Aushöhlen“ hinzugefügt  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Polygonreduzierung hinzugefügt  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Mesh-Reparatur hinzugefügt  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Vollautomatische Stützstrukturen (alte Stützstrukturen) zusätzlich zur neuen Option für manuelle Stützstrukturen eingebaut
* Unterstützung für gsSlicer hinzugefügt (experimentelle neue Slicing-Engine)
* Fehler behoben

## Änderungen

* Verbessertes Aufheben der Gruppierung von Meshes (Aufteilen in mehrere Meshes)
    * Entartete Flächen werden verworfen
    * Mikroskopisch kleine, einzelne Merkmale werden verworfen

## Änderungen

* Suchleiste für die Anwendung hinzugefügt
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Verbesserte Design-Werkzeugleiste
    * Gruppierung für einige Elemente hinzugefügt
    * Schaltfläche für duale Ausrichtung hinzugefügt
    * Schaltfläche „Alle anordnen“ hinzugefügt
* Objekte auf dem Druckbett mit den Pfeiltasten verschieben
* Der Downloads-Ordner ist nach Datum sortiert

## Änderungen

* Verbesserungen der Benutzeroberfläche
    * Schnellere Aktualisierungen in Ordnern der Cloud-Bibliothek
    * Wiederherstellung der Oberfläche beim erneuten Öffnen
    * Bessere Unterstützung der Tastaturnavigation
* Neues System zur Fehlererkennung und Warnung
    * Mehr Hardwarefehler werden behandelt
* Verbesserungen und Optimierungen der Design-Werkzeuge
    * Neue Twist-Werkzeuge 
    * Verbessertes Kurven-Werkzeug
    * Verbessertes Ausrichten


## Änderungen

* Verbessertes Flatten
* Verbesserte Undo-Unterstützung
* Verbesserter Design-Verlauf

## Änderungen
* Versionierung: Umstellung auf eine Versionsnummer im Format (Version).(Jahr).(Monat). Leichter zu lesen und aussagekräftiger.
* Neues, hochmodernes Subtrahieren, Vereinigen und Schneiden (nur Windows)
* Wir starten jetzt mit einer „Funktionstour“, damit sich neue Benutzer schneller zurechtfinden

## Änderungen
* Design-Werkzeuge – die Möglichkeit, mit einem vollständigen Satz an Modellier-Grundkörpern in 3D zu modellieren
* Einen Grundkörper verwenden, um eigene angepasste Stützstrukturen zu erstellen
* Design-Apps – Design-Apps: anspruchsvolle, anpassbare Designs
* 64-Bit-Verarbeitung
