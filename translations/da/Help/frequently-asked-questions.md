---
title: Ofte stillede spørgsmål
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Hvorfor har mine objekter forkert skala?
- STL-filer gemmer ikke oplysninger om enheder. MatterCAD forventer STL-mål i millimeter, mens de fleste CAD-programmer eksporterer i deres egne enheder (typisk tommer). Det giver skalaafvigelser, når designs importeres.

- Den bedste løsning er at indstille dit designprogram til at eksportere STL-filer i millimeter. I SolidWorks bruger du for eksempel knappen Indstillinger i dialogen Gem som til at angive parametre for STL-eksport.

- Alternativt kan du skalere emnet i MatterCAD. Gå til Rediger-tilstand i 3D-visningen, og vælg SKALÉR i værktøjslinjen til højre. Brug rullemenuen til almindelige omregningsfaktorer, eller indtast bestemte mål i aksefelterne.

# Hvordan rydder jeg programmets data?

- Hvis en geninstallation ikke løser problemet, kan det være nødvendigt at slette de data, MatterCAD har gemt. Disse data bevares efter afinstallation. Hvis du vil nulstille helt til standardindstillingerne, skal du fjerne programmappen. Du kan også midlertidigt omdøbe SQLite-databasefilen (MatterCAD.db) for at teste, om indstillingerne er årsag til problemerne.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - Brugerbiblioteket og indstillingerne gemmes i C:\Users\{user}\AppData\Local\MatterCAD.
