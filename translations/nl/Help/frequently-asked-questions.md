---
title: Veelgestelde vragen
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Waarom hebben mijn objecten de verkeerde schaal?
- STL-bestanden slaan geen eenheidsinformatie op. MatterCAD verwacht STL-afmetingen in millimeters, terwijl de meeste CAD-software exporteert in de eigen eenheden (meestal inches). Dit veroorzaakt schaalverschillen bij het importeren van ontwerpen.

- De beste oplossing is om je ontwerpsoftware zo in te stellen dat STL-bestanden in millimeters worden geëxporteerd. In SolidWorks gebruik je bijvoorbeeld de knop **Opties** in het dialoogvenster **Opslaan als** om de parameters voor STL-export in te stellen.

- Je kunt het onderdeel ook binnen MatterCAD herschalen. Ga in de 3D-weergave naar de modus **Bewerken** en selecteer SCHAAL in de rechterwerkbalk. Gebruik het vervolgkeuzemenu voor gangbare omrekenfactoren of voer specifieke afmetingen in de asvelden in.

# Hoe wis ik de applicatiegegevens?

- Als opnieuw installeren een probleem niet oplost, moet je mogelijk de opgeslagen gegevens van MatterCAD verwijderen. Deze gegevens blijven na het verwijderen van de installatie bestaan. Om volledig terug te zetten naar de standaardinstellingen, verwijder je de applicatiemap. Je kunt ook tijdelijk de naam van het SQLite-databasebestand (MatterCAD.db) wijzigen om te testen of de instellingen problemen veroorzaken.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - De gebruikersbibliotheek en instellingen worden opgeslagen in C:\Users\{user}\AppData\Local\MatterCAD.
