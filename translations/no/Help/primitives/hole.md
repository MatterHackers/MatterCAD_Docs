---
title: Hull
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Hull

Et kubeformet objekt som er forhåndskonfigurert til å fungere som et verktøy for boolsk subtraksjon. Når du bruker [Kombiner](../operations/boolean/combine.md), blir Hull-objekter automatisk trukket fra andre former i stedet for å bli lagt til dem.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Slik fungerer det

Primitivet Hull fungerer som en [Kube](cube.md), men har utdatatypen satt til «Hull». Når du kombinerer objekter som inkluderer et Hull, fjernes Hullets volum fra resultatet.

## Parametere

Samme som for [Kube](cube.md):

- **Bredde** - Størrelse langs X-aksen
- **Dybde** - Størrelse langs Y-aksen
- **Høyde** - Størrelse langs Z-aksen

## Tips

- Plasser Hullet slik at det overlapper med objektet du vil skjære i
- La Hullet gå helt gjennom målobjektet hvis du vil ha et gjennomgående hull
- Du kan bruke vanlige former med [Trekk fra](../operations/boolean/subtract.md) for samme effekt, men Hull er praktiske fordi de fungerer automatisk sammen med [Kombiner](../operations/boolean/combine.md)
- For runde hull bruker du heller en [Sylinder](cylinder.md) med Trekk fra

## Relatert

- [Kube](cube.md) - Den samme formen uten hull-oppførselen
- [Kombiner](../operations/boolean/combine.md) - Slår sammen former og trekker fra Hull automatisk
- [Trekk fra](../operations/boolean/subtract.md) - Trekk manuelt en hvilken som helst form fra en annen
