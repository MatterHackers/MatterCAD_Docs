---
title: Skaler
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Skaler

Skaler endrer størrelsen på et objekt med presis kontroll over dimensjoner, proporsjoner og enhetskonvertering. Du kan skalere jevnt, låse bestemte akser sammen eller endre størrelsen på hver akse uavhengig.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Slik bruker du den

1. Velg et objekt
2. Bruk **Skaler**-operasjonen fra Transformer-menyen
3. Velg skaleringsmetode og angi ønskede verdier

Du kan også skalere objekter i visningsområdet ved å klikke og dra skaleringshåndtakene i hjørnene på et valgt objekt.

## Parametere

### Skaleringstype

Velg en forhåndsinnstilling eller egendefinert skalering:

- **Egendefinert** – Angi dine egne dimensjoner eller prosentandeler
- **Tommer til mm** – Multipliser med 25,4 (konverter fra imperiske til metriske enheter)
- **mm til tommer** – Multipliser med 0,0393 (konverter fra metriske til imperiske enheter)
- **mm til cm** – Multipliser med 0,1
- **cm til mm** – Multipliser med 10

### Skaleringsmetode (Egendefinert-modus)

- **Direkte** – Angi ønsket Bredde, Dybde og Høyde i millimeter
- **Prosentandel** – Angi Bredde, Dybde og Høyde som prosentandeler av den opprinnelige størrelsen

### Lås proporsjon

- **Ingen (Skaler fritt)** – Hver akse skaleres uavhengig
- **X og Y** – Bredde og Dybde er låst sammen; Høyde skaleres uavhengig
- **X, Y og Z** – Alle tre aksene skaleres jevnt sammen

### Dimensjoner

- **Bredde** – Størrelse langs X-aksen
- **Dybde** – Størrelse langs Y-aksen
- **Høyde** – Størrelse langs Z-aksen

## Tips

- Bruk «Tommer til mm» hvis du har importert en STL-fil som ble designet i tommer og virker for liten
- Sett Lås proporsjon til X, Y og Z for jevn skalering – endrer du én dimensjon, oppdateres alle
- Objektets basisposisjon beholdes under skalering, slik at det blir liggende på arbeidsområdets overflate
- Du kan skrive inn eksakte verdier for presis størrelse, eller bruke glidebryterne for raske justeringer

## Relatert

- [Flytt](translate.md) – Flytt et objekt
- [Roter](rotate.md) – Roter et objekt
- [Tilpass til grenser](../placement/fit-to-bounds.md) – Skaler for å passe innenfor en bestemt størrelse
