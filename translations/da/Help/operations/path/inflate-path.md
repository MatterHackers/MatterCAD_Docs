---
title: Udvid sti
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Udvid sti

Udvid sti udvider en 2D-sti udad, så formen bliver større, samtidig med at dens overordnede udseende bevares. Det svarer til at anvende en ensartet forskydning på alle kanter.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Sådan bruges den

1. Vælg en 2D-sti
2. Anvend **Udvid sti** fra menuen med sti-operationer
3. Justér udvidelsesmængden

## Udvidelse af en åben linje

Udvid er måden, hvorpå du gør en linje til en form. Fjern markeringen af **Lukket** på en [Tilpasset sti](../../2d-paths/custom-path.md) for at tegne en åben linje, og udvid den derefter: resultatet er et udfyldt bånd, der er lige så bredt på hver side af linjen som den mængde, du angiver. Derfra kan den ekstruderes som enhver anden sti.

**Stil** angiver, hvordan linjens to ender afsluttes, samt hvordan dens hjørner samles:

- **Flad** stopper båndet lige ved hvert endepunkt
- **Rund** tilføjer en halvcirkel ud over hvert endepunkt
- **Skarp** tilføjer en firkant ud over hvert endepunkt

En åben linje har ingen inderside at skrumpe ind i, så en værdi på nul eller en negativ værdi ville slet ikke efterlade noget. Når stien er *helt* åben, begrænser Udvid værdien opad til et lille positivt tal og skriver det begrænsede tal tilbage i feltet, så du kan se, hvad der skete.

En sti, der blander åbne og lukkede konturer, begrænses ikke: de lukkede konturer skrumper som normalt, og de åbne falder simpelthen ud. Lukkede stier skrumper stadig ved negative værdier, præcis som de altid har gjort.

## Tips

- Brug negative værdier til at skrumpe stien indad i stedet for at udvide den
- Udvid er nyttig til at skabe toleranceforskydninger omkring former
- Kombinér med [Konturbane](outline-path.md) for at skabe kanter med bestemte bredder

## Relateret

- [Konturbane](outline-path.md) – Opret et omrids ud fra en sti
- [Kantbane](border-path.md) – Tilføj en kantforskydning
- [Udjævn sti](smooth-path.md) – Afrund hjørnerne på en sti
