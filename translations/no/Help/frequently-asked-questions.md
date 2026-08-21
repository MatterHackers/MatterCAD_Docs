---
title: Ofte stilte spørsmål
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Hvorfor har objektene mine feil skala?
- STL-filer lagrer ikke informasjon om enheter. MatterCAD forventer STL-mål i millimeter, mens de fleste CAD-programmer eksporterer i sine egne enheter (vanligvis tommer). Dette fører til avvik i skalering når du importerer design.

- Den beste løsningen er å konfigurere designprogramvaren din til å eksportere STL-filer i millimeter. I SolidWorks bruker du for eksempel knappen **Alternativer** i dialogboksen **Lagre som** for å angi parametere for STL-eksport.

- Alternativt kan du skalere om delen inne i MatterCAD. I 3D Vis går du inn i **Rediger**-modus og velger SKALER fra verktøylinjen til høyre. Bruk nedtrekksmenyen for vanlige konverteringsfaktorer, eller skriv inn bestemte mål i aksefeltene.

# Hvordan tømmer jeg applikasjonsdataene?

- Hvis en ny installasjon ikke løser problemet, må du kanskje slette dataene MatterCAD har lagret. Disse dataene blir liggende etter avinstallering. For å tilbakestille helt til standardinnstillingene, fjern applikasjonsmappen. Du kan også gi SQLite-databasefilen (MatterCAD.db) et midlertidig nytt navn for å teste om innstillingene forårsaker problemer.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - Brukerbiblioteket og innstillingene lagres i C:\Users\{user}\AppData\Local\MatterCAD.
