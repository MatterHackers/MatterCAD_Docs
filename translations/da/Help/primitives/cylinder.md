---
title: Cylinder
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Cylinder

En rund søjleform med indstillelig diameter, højde og antal sider. Cylinderen er uundværlig, når du skal lave stifter, stænger, huller og runde detaljer.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parametre

- **Diameter** - Bredden tværs over cylinderen (standard: 20mm)
- **Højde** - Hvor høj cylinderen er (standard: 20mm)
- **Sider** - Antal segmenter hele vejen rundt om omkredsen (standard: 40). Lavere værdier giver polygonale former (f.eks. 6 for en sekskant)

### Avancerede parametre

Aktivér **Avanceret** tilstand for at få adgang til flere indstillinger:

- **Diameter top** - Angiv en anden diameter for toppen af cylinderen for at lave koniske eller afkortede kegleformer (standard: samme som Diameter)
- **Startvinkel** - Den vinkel, hvor cylinderen begynder (standard: 0). Brug den sammen med Slutvinkel til at lave delvise cylindre
- **Slutvinkel** - Den vinkel, hvor cylinderen slutter (standard: 360). Angiv mindre end 360 for lagkageformer

## Tip

- Sæt Sider til et lavt tal for at lave regulære polygoner -- 6 for sekskanter, 8 for ottekanter osv.
- Brug forskellige værdier for Diameter og Diameter top for at lave afkortede kegler og koniske former
- Angiv Startvinkel og Slutvinkel for at lave lagkage- eller bueformer
- Cylindre er fremragende skæreværktøjer til at lave runde huller med [Træk fra](../operations/boolean/subtract.md)

## Relateret

- [Kegle](cone.md) - En cylinder, der spidser til i et punkt
- [Halv cylinder](half-cylinder.md) - En cylinder skåret over på langs
- [Ring](ring.md) - En hul cylinder (rør)
