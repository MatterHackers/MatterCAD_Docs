---
title: Skalér
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Skalér

Skalér ændrer størrelsen på et objekt med præcis kontrol over dimensioner, proportioner og enhedskonvertering. Du kan skalere ensartet, låse bestemte akser sammen eller ændre størrelsen på hver akse uafhængigt.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Skalér** fra menuen Transformér
3. Vælg din skaleringsmetode, og indtast de ønskede værdier

Du kan også skalere objekter i visningen ved at klikke og trække i skaleringshåndtagene i hjørnerne på et valgt objekt.

## Parametre

### Skaleringstype

Vælg en forudindstilling eller brugerdefineret skalering:

- **Brugerdefineret** – Indtast dine egne dimensioner eller procentdele
- **Tommer til mm** – Gang med 25,4 (konvertér fra imperiske til metriske enheder)
- **mm til tommer** – Gang med 0,0393 (konvertér fra metriske til imperiske enheder)
- **mm til cm** – Gang med 0,1
- **cm til mm** – Gang med 10

### Skaleringsmetode (tilstanden Brugerdefineret)

- **Direkte** – Indtast den ønskede Bredde, Dybde og Højde i millimeter
- **Procentdel** – Indtast Bredde, Dybde og Højde som procentdele af den oprindelige størrelse

### Lås proportioner

- **Ingen (Skalér frit)** – Hver akse skaleres uafhængigt
- **X & Y** – Bredde og Dybde er låst sammen; Højde skaleres uafhængigt
- **X, Y & Z** – Alle tre akser skaleres ensartet sammen

### Dimensioner

- **Bredde** – Størrelse langs X-aksen
- **Dybde** – Størrelse langs Y-aksen
- **Højde** – Størrelse langs Z-aksen

## Tips

- Brug "Tommer til mm", hvis du har importeret en STL-fil, der er designet i tommer og virker for lille
- Sæt Lås proportioner til X, Y & Z for ensartet skalering – ændrer du én dimension, opdateres de alle
- Objektets basisposition bevares under skaleringen, så det bliver liggende på arbejdsområdets overflade
- Du kan indtaste præcise værdier for nøjagtig størrelse eller bruge skyderne til hurtige justeringer

## Relateret

- [Flyt](translate.md) – Flyt et objekt
- [Roter](rotate.md) – Roter et objekt
- [Tilpas til grænser](../placement/fit-to-bounds.md) – Skalér til at passe inden for en bestemt størrelse
