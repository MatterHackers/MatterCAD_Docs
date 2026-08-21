---
title: Cilinder
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Cilinder

Een ronde kolomvorm met instelbare diameter, hoogte en aantal zijden. De Cilinder is onmisbaar voor het maken van pennen, staven, gaten en ronde elementen.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parameters

- **Diameter** - De breedte over de cilinder (standaard: 20mm)
- **Hoogte** - Hoe hoog de cilinder is (standaard: 20mm)
- **Zijden** - Aantal segmenten rond de omtrek (standaard: 40). Lagere waarden geven veelhoekige vormen (bijv. 6 voor een zeshoek)

### Geavanceerde parameters

Schakel de modus **Geavanceerd** in voor extra instellingen:

- **Diameter boven** - Stel een andere diameter in voor de bovenkant van de cilinder om taps toelopende of afgeknotte kegelvormen te maken (standaard: gelijk aan Diameter)
- **Starthoek** - Hoek waar de cilinder begint (standaard: 0). Gebruik samen met Eindhoek om gedeeltelijke cilinders te maken
- **Eindhoek** - Hoek waar de cilinder eindigt (standaard: 360). Stel lager dan 360 in voor taartpuntvormen

## Tips

- Stel Zijden in op een laag aantal om regelmatige veelhoeken te maken -- 6 voor zeshoeken, 8 voor achthoeken, enzovoort.
- Gebruik verschillende waarden voor Diameter en Diameter boven om afgeknotte kegels en taps toelopende vormen te maken
- Stel de Starthoek en Eindhoek in om taartpunt- of boogvormen te maken
- Cilinders zijn uitstekende snijgereedschappen om ronde gaten te maken met [Aftrekken](../operations/boolean/subtract.md)

## Gerelateerd

- [Kegel](cone.md) - Een cilinder die taps toeloopt naar een punt
- [Halve cilinder](half-cylinder.md) - Een cilinder die in de lengte doormidden is gesneden
- [Ring](ring.md) - Een holle cilinder (buis)
