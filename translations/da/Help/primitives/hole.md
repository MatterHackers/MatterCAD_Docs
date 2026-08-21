---
title: Hul
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Hul

Et terningformet objekt, der er forudkonfigureret til at fungere som et boolesk fratrækningsværktøj. Når du bruger [Kombinér](../operations/boolean/combine.md), bliver Hul-objekter automatisk trukket fra andre former i stedet for at blive lagt til dem.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Sådan fungerer det

Primitivet Hul fungerer som en [Terning](cube.md), men har sin outputtype sat til "Hul". Når du kombinerer objekter, der indeholder et Hul, fjernes hullets volumen fra resultatet.

## Parametre

Samme som [Terning](cube.md):

- **Bredde** - Størrelse langs X-aksen
- **Dybde** - Størrelse langs Y-aksen
- **Højde** - Størrelse langs Z-aksen

## Tips

- Placér hullet, så det overlapper med det objekt, du vil skære i
- Lad hullet gå helt igennem målobjektet, hvis du vil have et gennemgående hul
- Du kan bruge almindelige former med [Træk fra](../operations/boolean/subtract.md) for at opnå den samme effekt, men huller er praktiske, fordi de virker automatisk sammen med [Kombinér](../operations/boolean/combine.md)
- Til runde huller skal du i stedet bruge en [Cylinder](cylinder.md) med Træk fra

## Relateret

- [Terning](cube.md) - Den samme form uden hul-adfærden
- [Kombinér](../operations/boolean/combine.md) - Fletter former og trækker huller fra automatisk
- [Træk fra](../operations/boolean/subtract.md) - Træk manuelt en vilkårlig form fra en anden
