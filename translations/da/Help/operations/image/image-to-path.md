---
title: Billede til bane
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Billede til bane

Billede til bane optegner konturerne i et billede for at skabe 2D-baner. Disse baner kan derefter ekstruderes, roteres eller bruges med enhver anden baneoperation. Det er ideelt til at omdanne logoer, silhuetter og enkel grafik til 3D-objekter.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Sådan bruges det

1. Vælg et billedobjekt i dit arbejdsområde
2. Anvend **Billede til bane** fra menuen med billedoperationer
3. Vælg analysetypen, og justér udvalgsområdet

## Parametre

- **Analysetype** - Hvordan billedet analyseres til optegning:
  - **Gennemsigtighed** - Optegn ud fra gennemsigtige kontra uigennemsigtige områder (bedst til PNG-filer med gennemsigtig baggrund)
  - **Farver** - Optegn ud fra farveområder
  - **Intensitet** - Optegn ud fra lysstyrkeniveauer (bedst til de fleste billeder)
- **Vælg område** - En histogramkontrol til at vælge, hvilke lysstyrke-/farveværdier der skal indgå i optegningen
- **Min. overfladeareal** - Mindste areal, før en baneløkke medtages. Øg værdien for at frasortere små støjartefakter

## Tips

- Rene billeder med høj kontrast og enkle former fungerer bedst
- Brug tilstanden Gennemsigtighed til PNG-billeder med gennemsigtig baggrund
- Brug tilstanden Intensitet til fotografier og billeder uden gennemsigtighed
- Efter optegning kan du anvende [Lineær ekstrudering](../path/linear-extrude.md) for at give banen højde
- Øg Min. overfladeareal for at fjerne små uønskede detaljer fra optegningen

## Relateret

- [Billedkonvertering](image-converter.md) - Opret et højdekortrelief i stedet for flade baner
- [Litofan](lithophane.md) - Opret baggrundsbelyste billedvisninger
- [SVG-objekt](../../primitives/svg-object.md) - Importer vektorgrafik direkte (ingen optegning nødvendig)
- [Lineær ekstrudering](../path/linear-extrude.md) - Giv den optegnede bane højde
