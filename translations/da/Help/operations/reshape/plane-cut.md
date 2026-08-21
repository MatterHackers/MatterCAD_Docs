---
title: Planskæring
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Planskæring

Planskæring skærer et objekt over i en angivet højde med et vandret plan og beholder kun den del, der ligger under snittet. Snitfladen lukkes med en plan flade.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Planskæring** fra menuen Omform
3. Angiv klippehøjden

## Parametre

- **Klippehøjde** - Den Z-højde, hvor objektet skæres over (standard: 10 mm, interval: 1-200 mm)

## Tips

- Brug Planskæring til at gøre toppen af en model flad i en bestemt højde
- Nyttigt til at beskære importerede modeller eller lave flade bunde
- Hvis du vil skære med en ikke-plan form, skal du i stedet bruge [Træk fra](../boolean/subtract.md) med et andet objekt
- Hvis du vil skære med et hældende plan, skal du først rotere objektet, anvende Planskæring og derefter rotere tilbage

## Relateret

- [Skær](../boolean/intersect.md) - Behold kun der, hvor objekter overlapper
- [Træk fra](../boolean/subtract.md) - Skær med en vilkårlig form, ikke kun et plan
- [Udhul](hollow-out.md) - Opret en hul skal
