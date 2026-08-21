---
title: Ring
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Ring

Een holle cilinder (buis) met onafhankelijke binnen- en buitendiameters en een opgegeven hoogte. Ook bekend als een pijp- of buisvorm.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parameters

- **Buitendiameter** - De buitenbreedte van de ring (standaard: 20mm)
- **Binnendiameter** - De diameter van het holle midden (standaard: 15mm)
- **Hoogte** - Hoe hoog de ring is (standaard: 5mm)
- **Zijden** - Aantal segmenten rond de omtrek (standaard: 40)

### Geavanceerde parameters

Schakel de modus **Geavanceerd** in voor extra instellingen:

- **Starthoek** - Hoek waar de ring begint (standaard: 0)
- **Eindhoek** - Hoek waar de ring eindigt (standaard: 360). Stel een waarde kleiner dan 360 in voor een gedeeltelijke ring
- **Rond** - Voeg afronding toe aan de randen (Geen, Omhoog of Omlaag)
- **Richting** - Afronden naar de binnen- of buitenrand (zichtbaar wanneer Rond is ingeschakeld)
- **Ronde segmenten** - Gladheid van de afronding (zichtbaar wanneer Rond is ingeschakeld)

## Tips

- De wanddikte is gelijk aan (Buitendiameter - Binnendiameter) / 2
- Gebruik dit voor ringen, afstandshouders, bussen en buisachtige onderdelen
- Stel de hoogte hoog in voor pijpen of laag voor platte sluitringen
- Gebruik de Starthoek en Eindhoek voor gedeeltelijke ringvormen zoals C-clips

## Gerelateerd

- [Torus](torus.md) - Een donutvormige ring met een ronde doorsnede
- [Cilinder](cylinder.md) - Een massieve ronde kolom (zonder hol midden)
