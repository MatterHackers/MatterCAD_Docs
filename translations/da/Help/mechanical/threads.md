---
title: Gevind
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Gevind

Opret skruegevind med indstillelig diameter, stigning og gevindprofil. Gevind kan bruges som selvstændige bolte/skruer eller trækkes fra andre objekter for at lave gevindskårne huller.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Sådan bruges det

1. Tilføj **Gevind** fra værktøjerne under Mekanisk eller panelet Primitiver
2. Angiv diameter, stigning og antal rotationer
3. Aktivér eventuelt "Brug som hul" for at lave gevindskårne huller

## Parametre

### Anvendelse

- **Brug som hul** - Når indstillingen er aktiveret, dimensioneres gevindet med ekstra tolerance, så det kan bruges som et fratrukket hul (standard: fra)
- **Tolerance** - Ekstra spillerum til pasning, når gevindet bruges som hul (standard: 0,2 mm, vises når Brug som hul er aktiveret)

### Attributter

- **Diameter** - Gevindsektionens yderdiameter (standard: 10 mm)
- **Stigning** - Afstand mellem hver gevindomgang (standard: 2 mm). Mindre stigning = finere gevind
- **Gevindskala** - Gevindets bredde som forhold til stigningen (standard: 1,0, interval: 0,1-1,0)
- **Rotationer** - Antal hele gevindomgange (standard: 10)

### Geometri

- **Sider** - Antal segmenter rundt om omkredsen (standard: 40). Flere = glattere

### Spidser (gevindender)

- **Spidsskala** - Hvor meget gevindenderne skal aftrappes (standard: 0, interval: 0-1). Sæt værdien over 0 for at lave en konisk indføring i enderne
- **Spidsvinkel** - Den vinkel, som spidserne aftrappes over (standard: 90 grader)

## Tips

- Sådan laver du et gevindskåret hul: aktivér "Brug som hul", placér gevindet, og brug [Træk fra](../operations/boolean/subtract.md) på dit objekt
- Tilføj Tolerance, når gevindet bruges som hul, så de printede dele passer sammen
- Standardstigninger for metriske gevind: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Brug Spidsskala til at lave en indføring, der gør det lettere at sætte gevindet i gang

## Relateret

- [Tandhjul](gears.md) - Opret mekaniske tandhjulsformer
- [Cylinder](../primitives/cylinder.md) - En almindelig rund søjle (uden gevind)
- [Træk fra](../operations/boolean/subtract.md) - Skær gevind ud af andre objekter for at lave huller
