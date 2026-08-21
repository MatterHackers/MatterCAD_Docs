---
title: Gjenger
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Gjenger

Opprett skruegjenger med konfigurerbar diameter, stigning og gjengeprofil. Gjenger kan brukes som frittstående bolter/skruer eller trekkes fra andre objekter for å lage gjengede hull.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Slik bruker du den

1. Legg til **Gjenger** fra Mekanisk-verktøyene eller Primitiver-panelet
2. Angi diameter, stigning og antall rotasjoner
3. Aktiver eventuelt «Bruk som Hull» for å lage gjengede hull

## Parametere

### Bruk

- **Bruk som Hull** - Når dette er aktivert, dimensjoneres gjengene med ekstra toleranse for bruk som et fratrukket hull (standard: av)
- **Toleranse** - Ekstra klaring for passform når den brukes som hull (standard: 0,2 mm, synlig når Bruk som Hull er på)

### Attributter

- **Diameter** - Ytre diameter på den gjengede seksjonen (standard: 10 mm)
- **Stigning** - Avstand mellom hver gjengeomdreining (standard: 2 mm). Mindre stigning = finere gjenger
- **Gjengeskala** - Gjengenes bredde som et forhold til stigningen (standard: 1,0, område: 0,1-1,0)
- **Rotasjoner** - Antall hele gjengeomdreininger (standard: 10)

### Geometri

- **Sider** - Antall segmenter rundt omkretsen (standard: 40). Flere = jevnere

### Spisser (gjengeender)

- **Spissskala** - Hvor mye gjengeendene skal avsmalnes (standard: 0, område: 0-1). Sett høyere enn 0 for å lage avsmalnet innføring i endene
- **Spissvinkel** - Vinkelen som spissene avsmalnes over (standard: 90 grader)

## Tips

- Slik lager du et gjenget hull: aktiver «Bruk som Hull», plasser gjengene, og [Trekk fra](../operations/boolean/subtract.md) objektet ditt
- Legg til Toleranse når du bruker den som hull for å sikre at de utskrevne delene passer sammen
- Standard metriske gjengestigninger: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Bruk Spissskala for å lage en innføring som gjør det enklere å starte gjengingen

## Relatert

- [Tannhjul](gears.md) - Opprett mekaniske tannhjulformer
- [Sylinder](../primitives/cylinder.md) - En enkel rund søyle (uten gjenger)
- [Trekk fra](../operations/boolean/subtract.md) - Klipp ut gjenger fra andre objekter for å lage hull
