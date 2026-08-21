---
title: Versionshinweise
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13. August 2026)
[Windows-Download](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Neue Merkmale

* **Unterelemente bearbeiten**
  * Doppelklicken Sie auf ein Objekt auf dem Druckbett oder im Szenenbaum, um in das Objekt einzusteigen und die Teile zu bearbeiten, aus denen es aufgebaut ist – ohne separates Fenster oder separaten Tab
  * Bei Operationen wie Subtrahieren bearbeiten Sie die Ausgangsteile, und das Ergebnis wird neu aufgebaut, sobald Sie wieder heraustreten
  * Ein Brotkrumenpfad am oberen Rand des Szenenbaums zeigt den vollständigen Pfad an; ein Klick auf eine Ebene fügt Ihre Änderungen als einen einzigen widerrufbaren Schritt zusammen, und jede Ebene behält ihren eigenen Undo-Verlauf
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Ein einziges Boolesches Werkzeug**
  * Vereinen, Subtrahieren, Verschneiden sowie Subtrahieren und Ersetzen sind jetzt eine einzige Operation mit einer Symbolleiste am oberen Rand ihres Bedienfelds – wechseln Sie den Modus mit einem Klick, statt die Operation zu löschen und neu anzuwenden
  * Dieselbe Operation verarbeitet sowohl 3D-Netze als auch 2D-Pfade und zeigt den Fortschritt an, während eine aufwendige boolesche Berechnung läuft
  * Designs, die mit den früheren separaten booleschen Objekten gespeichert wurden, lassen sich weiterhin normal öffnen
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Boolesche Operationen, die einfach funktionieren**
  * Boolesche Operationen laufen auf einer neuen nativen Engine, die schneller ist und auch bei Netzen gelingt, die zuvor gescheitert sind
  * Vereinen repariert Teile mit Löchern automatisch: saubere Reparaturen gehen in die Vereinigung ein, Teile, die nicht sicher zusammengeführt werden können, werden daneben behalten und für Sie benannt, und ein Teil, das nicht repariert werden konnte, behält Ihre ursprüngliche Geometrie
  * Ebenenschnitt ist jetzt eine echte Volumenverschneidung, sodass das Ergebnis wasserdicht und druckbar ist statt einer offenen Schale
  * Neue Optionen Innen-nach-außen-Geometrie beibehalten und Windungsreihenfolge reparieren für problematische importierte Netze


## Verbesserungen

* **2D-Pfad-Editor**
  * Vier Punktmodi – Scharf, Symmetrisch, Ausgerichtet und Frei – mit einem Klick angewendet, sowohl im 2D-Editor als auch in der 3D-Ansicht
  * Spiegeln ist jetzt ein aktiver Symmetriemodus: Änderungen werden während der Bearbeitung an der Mitte gespiegelt, und wenn Sie ein gespiegeltes Punktepaar auf die Achse ziehen, verschmilzt es zu einem einzigen Punkt
  * Punkte per Gummiband auswählen, als Gruppe verschieben, am Raster einrasten und mit Esc einen Ziehvorgang abbrechen
  * Glätten legt in einem Schritt eine Kurve durch Ihre gesetzten Punkte
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Ansicht und Navigation**
  * Drücken Sie Z bei ausgewähltem flachem Pfad, um zu einer senkrechten Bearbeitungsansicht zu animieren, die auf den Pfad eingepasst ist
  * Subpixel-Textdarstellung ist jetzt automatisch aktiv, wenn Ihr Bildschirm sie unterstützt, und lässt sich weiterhin unter Erweitert ein- oder ausschalten

* **Modellieren**
  * Linear extrudieren kann die untere Kante mit eigenem Stil, eigenem Radius und eigener Segmentanzahl abschrägen
  * Reine Editor-Objekte (3D-Kurve, Messwerkzeug, Beschreibung, Blatt) werden weiterhin angezeigt, aber vom Export ausgeschlossen

## Wichtigste Fehlerbehebungen

  * Ein Speichervorgang, der auf halbem Weg fehlschlug, konnte die zu ersetzende Datei abschneiden und dennoch Erfolg melden. Speichervorgänge werden jetzt vollständig abgeschlossen und ersetzen das Ziel anschließend atomar – derselbe Schutz gilt für Speichervorgänge in der Bibliothek und für Exporte
  * Ein fehlgeschlagener Speichervorgang lässt das Design als ungespeichert markiert, sodass das Schließen der Anwendung Ihre Arbeit nicht stillschweigend verwerfen kann
  * Beim Speichern eines Cloud-Elements auf die Festplatte blieb der alte Tab-Name erhalten und der Tab ging beim Neustart verloren
  * Behoben: 3MF-Untermodelle wurden beim Laden stillschweigend verworfen, und gleichzeitig geladene 3MF-Dateien beeinflussten sich gegenseitig
  * Behoben: Abstürze, ein defekter Histogramm-Filter und Kopien eines Bildteils, die nicht mit dem Original synchron blieben
  * Behoben: ein Absturz beim Löschen eines Kurvenpunkts sowie Punkte an der Naht eines geschlossenen Pfades, die den von Ihnen gewählten Modus zurücksetzten
  * Die Stopp-Schaltfläche bei einer laufenden Aufgabe ist jetzt anklickbar und bricht den Vorgang tatsächlich ab

---

# MatterCAD 2.2026.5 (8. Mai 2026)
[Windows-Download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Neue Merkmale

* **Neu gestaltetes Array-Werkzeug**
  * Eine einzige, vereinheitlichte Array-Operation ersetzt das alte Lineares Array, Radiale Anordnung und Erweitertes Array
  * Modus **Linear**: Kopien entlang einer Richtung mit optionaler Rotation und progressiver Skalierung
  * Modus **Radial**: Kopien um eine zentrale Achse mit konfigurierbarem Radius, Öffnungswinkel sowie Bogen- oder Vollkreismustern
  * Modus **Transformieren**: schrittweise Kopien mithilfe einer manuellen Transformation oder der Transformation eines benannten Geschwisterobjekts
  * Der Rotationsmodus Verbund im Modus Linear erzeugt Spiralen, Fächer und Helices ganz natürlich
  * Option Skalierung beeinflusst Versatz für Anordnungen nach Nautilusschale und geometrischer Progression
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Favoriten in der Bibliothek**
  * Markieren Sie ein beliebiges Bibliothekselement mit einem Stern, um es dem dauerhaften Ordner Favoriten hinzuzufügen
  * Greifen Sie an einer Stelle schnell auf Ihre meistgenutzten Grundkörper, Generatoren und gespeicherten Teile zu
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Verbesserungen

* **Ausrichten**
  * Die gestapelte Ausrichtung ist jetzt eine direkte Modus-Schaltfläche statt einer Dropdown-Option
  * Klarere Modi Einfach, Versatz und Gestapelt zum Ausrichten von Kanten, zum Einfügen präziser Abstände und zum Aufbau geordneter Stapel hinzugefügt
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Dateiunterstützung**
  * Unterstützung für das Bildformat WEBP in bildbasierten Operationen hinzugefügt
  * Verbesserte Analyse von SVG-Dateien für zuverlässigere Importe

* **Zuverlässigkeit**
  * Verbesserte Geschwindigkeit und Zuverlässigkeit beim Laden von 3MF-Dateien
  * Bessere Wiederherstellung von Tabs zwischen Sitzungen

## Wichtigste Fehlerbehebungen

* **Anmeldung und Zugriff auf die Cloud-Bibliothek**
  * Anmeldung und Zugriff auf die Cloud-Bibliothek sind wiederhergestellt, nachdem ein Upgrade des Backend-Servers die Anmeldung gestört hatte.
  * MatterCAD fordert Sie jetzt zum erneuten Anmelden auf, wenn beim Cloud-Zugriff abgelaufene oder ungültige Anmeldedaten festgestellt werden.

* **Auswahl im Szenenbaum**
  * Uneinheitliches Auswahlverhalten beim Auswählen von Objekten im Szenenbaum behoben.

* **Navigation in der Hilfe**
  * Navigationsprobleme in der mitgelieferten Hilfe und der Versionsdokumentation behoben.

* **Rechtsklick in der Bibliothek**
  * Rechtsklick-Verhalten in der Baumansicht der Bibliothek behoben.

* **Blätter**
  * Ein Absturz behoben, der beim Arbeiten mit Blättern auftreten konnte.

---

# MatterCAD 2.2026.3 (12. März 2026)
[Windows-Download](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Neue Merkmale

* **Völlig neue Direct3D-11-Rendering-Engine**
  * Vollständige Umstellung von OpenGL auf Direct3D 11 für deutlich bessere Leistung
  * FXAA-Kantenglättung für scharfe, saubere Kanten
  * Dual Depth Peeling für korrekte reihenfolgeunabhängige Transparenz
  * Hardwarebeschleunigte Schatten auf dem Druckbett
  * Verbesserte Objektumrisse und Auswahldarstellung
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Transparenz von Objekten**
  * Alpha/Transparenz für jedes einzelne Objekt in der Szene festlegen
  * Netze mit Farben pro Fläche unterstützen Alpha ohne Farbverfälschung
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Objekte sperren und ausblenden**
  * Objekte sperren, um versehentliches Auswählen oder Bearbeiten zu verhindern
  * Objekte ausblenden, um die Ansicht beim Arbeiten an bestimmten Teilen übersichtlich zu halten
  * Befehle Alle einblenden und Alle entsperren, um die Sichtbarkeit schnell wiederherzustellen
  * Gesperrte und ausgeblendete Objekte werden von der strahlbasierten Auswahl korrekt ausgeschlossen
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Verbessertes boolesches Subtrahieren**
  * Mehrfach-Subtraktionen sind deutlich zuverlässiger und genauer

## Verbesserungen

* **Dateihandhabung**
  * Projekte werden jetzt standardmäßig als 3MF statt als STL gespeichert und behalten dabei Farben, Materialien und den Designverlauf
  * Erweiterte Drag-and-drop-Unterstützung für Dateien und Ordner in der 3D-Ansicht

* **Arbeitsablauf**
  * Die Dialoge Speichern unter und Verschieben merken sich Ihren zuletzt verwendeten Ordner
  * Ausdrucksfelder unterstützen jetzt `pi`, `tau`, `e` und `count`
  * Die Esc-Taste führt beim Bearbeiten von Designs einen Undo-Schritt aus
  * 3D-Bedienelemente bleiben sichtbar, wenn die Maus die Szene verlässt

* **Leistung und Stabilität**
  * Startabstürze und rekursive Ladeprobleme behoben
  * Rendering-Fehler bei Beleuchtung und Mipmapping behoben
  * Verbesserte Aktualisierung der Baumansicht der Bibliothek
  * Dynamische Berechnung von Nah- und Fernebene für besseres Zoomverhalten
  * Aktualisierung auf .NET 10

---

# MatterCAD 2.2025.6 (20. Juni 2025)
[Windows-Download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Neue Merkmale

* **Unterstützung für SVG-Dateien**  
  * Vollständige Drag-and-drop-Unterstützung für SVG-Dateien
  * Direkte Umwandlung von SVG-Grafiken in 3D-Objekte
  * Nahtlose Integration in bestehende CAD-Arbeitsabläufe

* **Erweiterte Handhabung von OBJ-Dateien**  
  * Unterstützung für das Laden von Materialien aus ZIP-Archiven
  * Verbesserte Analyse von OBJ-Dateien und Materialverarbeitung
  * Bessere Unterstützung für komplexe 3D-Modelle mit mehreren Materialien

* **Erweitertes Tab-Verwaltungssystem**
  * Tabs der Cloud-Bibliothek bleiben jetzt korrekt erhalten – Ihre Arbeit bleibt genau dort, wo Sie sie verlassen haben
  * Verbesserte Organisation und Navigation von Tabs
  * Automatische Wiederherstellung geöffneter Tabs zwischen Sitzungen

## Verbesserungen der Benutzerfreundlichkeit

* **Optimierte Oberfläche**
  * Neu organisiertes Menü „Zuletzt verwendet“ für schnelleren Zugriff
  * Besseres visuelles Feedback bei langen Vorgängen
  * Verbesserte Startzeit und Reaktionsfähigkeit der Anwendung

* **Zuverlässigkeit**
  * Kritische Abstürze bei Interaktionen in der 3D-Szene behoben
  * Probleme bei der Speicherverwaltung behoben
  * Verbesserte Anwendungsstabilität auf allen Plattformen

---

# MatterCAD 2.21.5 (13. Feb. 2025)

[Windows-Download](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Bestehende Merkmale

*Die folgenden Merkmale bilden die Grundlage, auf der MatterCAD aus dem Erbe von MatterControl aufbaut:*

* Merkmal Hohl hinzugefügt  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Polygon-Reduzierung hinzugefügt  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Netzreparatur hinzugefügt  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Vollautomatische Stützstruktur (herkömmliche Stützstruktur) zusätzlich zur neuen manuellen Option eingebaut
* Unterstützung für gsSlicer hinzugefügt (experimentelle neue Slicing-Engine)
* Fehler behoben

## Änderungen

* Verbesserte Gruppierungsauflösung von Netzen (Aufteilen in mehrere Netze)
    * Entartete Flächen werden verworfen
    * Mikroskopisch kleine diskrete Merkmale werden verworfen

## Änderungen

* Suchleiste für die Anwendung hinzugefügt
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Verbesserte Design-Werkzeugleiste
    * Gruppierung für einige Elemente hinzugefügt
    * Schaltfläche für doppelte Ausrichtung hinzugefügt
    * Schaltfläche „Alle anordnen“ hinzugefügt
* Elemente auf dem Druckbett mit den Pfeiltasten verschieben
* Der Downloads-Ordner ist nach Datum sortiert

## Änderungen

* Verbesserungen der Benutzeroberfläche
    * Schnellere Aktualisierungen in Ordnern der Cloud-Bibliothek
    * Wiederherstellung der Benutzeroberfläche beim erneuten Öffnen
    * Bessere Unterstützung der Tastaturnavigation
* Neues System zur Fehlererkennung und Warnung
    * Mehr Hardwarefehler werden behandelt
* Verbesserungen und Optimierungen der Designwerkzeuge
    * Neue Verdrehen-Werkzeuge 
    * Verbessertes Werkzeug Kurve
    * Verbessertes Ausrichten


## Änderungen

* Verbessertes Abflachen
* Verbesserte Undo-Unterstützung
* Verbesserter Designverlauf

## Änderungen
* Versionierung: Umstellung auf eine Versionsnummer nach dem Schema (Version).(Jahr).(Monat). Leichter zu lesen und aussagekräftiger.
* Neues, hochmodernes Subtrahieren, Vereinen und Schnittmenge (nur Windows)
* Wir starten jetzt mit einer „Feature-Tour“, damit sich neue Anwender leichter zurechtfinden

## Änderungen
* Designwerkzeuge – Die Möglichkeit, mit einem vollständigen Satz an Modellier-Grundkörpern in 3D zu modellieren
* Verwenden Sie einen Grundkörper, um Ihre eigenen angepassten Stützstrukturen zu erstellen
* Design-Apps – Design-Apps: anspruchsvolle, anpassbare Designs
* 64-Bit-Verarbeitung
