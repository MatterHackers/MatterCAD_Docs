---
title: Häufig gestellte Fragen
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Warum haben meine Objekte die falsche Skalierung?
- STL-Dateien speichern keine Einheiteninformationen. MatterCAD erwartet STL-Abmessungen in Millimetern, während die meisten CAD-Programme in ihren nativen Einheiten (in der Regel Zoll) exportieren. Dies führt beim Importieren von Konstruktionen zu Skalierungsabweichungen.

- Die beste Lösung besteht darin, Ihre Konstruktionssoftware so zu konfigurieren, dass STL-Dateien in Millimetern exportiert werden. In SolidWorks verwenden Sie dafür beispielsweise die Schaltfläche „Optionen“ im Dialogfeld „Speichern unter“, um die Parameter für den STL-Export festzulegen.

- Alternativ können Sie das Teil innerhalb von MatterCAD neu skalieren. Wechseln Sie in der 3D-Ansicht in den Bearbeitungsmodus und wählen Sie SCALE in der rechten Symbolleiste. Verwenden Sie das Dropdown-Menü für gängige Umrechnungsfaktoren oder geben Sie in den Achsenfeldern konkrete Abmessungen ein.

# Wie lösche ich die Anwendungsdaten?

- Wenn eine Neuinstallation ein Problem nicht behebt, müssen Sie möglicherweise die von MatterCAD gespeicherten Daten löschen. Diese Daten bleiben auch nach der Deinstallation erhalten. Um vollständig auf die Standardeinstellungen zurückzusetzen, entfernen Sie den Anwendungsordner. Sie können außerdem die SQLite-Datenbankdatei (MatterCAD.db) vorübergehend umbenennen, um zu prüfen, ob die Einstellungen die Probleme verursachen.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - Benutzerbibliothek und Einstellungen werden unter C:\Users\{user}\AppData\Local\MatterCAD gespeichert.
