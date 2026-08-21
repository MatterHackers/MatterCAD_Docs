---
title: Häufig gestellte Fragen
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Warum haben meine Objekte die falsche Größe?
- STL-Dateien speichern keine Einheiteninformationen. MatterCAD erwartet STL-Abmessungen in Millimetern, während die meisten CAD-Programme in ihren eigenen Einheiten exportieren (üblicherweise Zoll). Dies führt beim Importieren von Konstruktionen zu Skalierungsabweichungen.

- Die beste Lösung ist, Ihre Konstruktionssoftware so einzustellen, dass STL-Dateien in Millimetern exportiert werden. In SolidWorks verwenden Sie zum Beispiel die Schaltfläche Optionen im Dialogfeld Speichern unter, um die Parameter für den STL-Export festzulegen.

- Alternativ können Sie das Bauteil in MatterCAD neu skalieren. Wechseln Sie in der 3D-Ansicht in den Modus Bearbeiten und wählen Sie SKALIEREN in der rechten Symbolleiste. Verwenden Sie das Dropdown-Menü für gängige Umrechnungsfaktoren oder geben Sie bestimmte Abmessungen in den Achsenfeldern ein.

# Wie lösche ich die Anwendungsdaten?

- Wenn sich ein Problem durch eine Neuinstallation nicht beheben lässt, müssen Sie unter Umständen die von MatterCAD gespeicherten Daten löschen. Diese Daten bleiben nach der Deinstallation erhalten. Um die Standardeinstellungen vollständig wiederherzustellen, entfernen Sie den Anwendungsordner. Sie können auch vorübergehend die SQLite-Datenbankdatei (MatterCAD.db) umbenennen, um zu prüfen, ob die Einstellungen die Probleme verursachen.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - Benutzerbibliothek und Einstellungen werden unter C:\Users\{user}\AppData\Local\MatterCAD gespeichert.
