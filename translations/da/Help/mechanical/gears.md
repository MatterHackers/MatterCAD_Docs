---
title: Tandhjul
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Tandhjul

Opret 3D-tandhjul med fuldt konfigurerbar tandgeometri. MatterCAD genererer korrekte evolvente tandprofiler, der griber korrekt ind i andre tandhjul med samme modul og indgrebsvinkel.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Sådan bruges den

1. Tilføj et **Tandhjul** fra Mekanisk-værktøjerne eller panelet Primitiver
2. Angiv tandantallet og de øvrige parametre
3. Tandprofilen genereres automatisk

## Parametre

### Funktioner

- **Tandhjulstype** - Ekstern tandhjul eller Tandstang (lige stang med tænder)
- **Højde** - Tandhjulets tykkelse (ekstruderingshøjde)
- **Tandantal** - Antal tænder rundt om tandhjulet (standard: 30, interval: 4-60)
- **Cirkulær tandhøjde** - Buelængden mellem tænderne langs stigningscirklen (interval: 3-30). Dette bestemmer den samlede størrelse.
- **Centerhulsdiameter** - Diameter på det centrale akselhul (standard: 4 mm, sæt til 0 for intet hul). Kun eksterne tandhjul.
- **Ydre kantbredde** - Bredden af kanten uden for de indre tænder
- **Antal tænder på indre tandhjul** - Tandantal for det modgående indre tandhjul

### Avanceret

- **Indgrebsvinkel** - Vinklen på tandens kontaktflade (almindelige værdier: 14,5, 20 eller 25 grader). Alle tandhjul, der griber ind i hinanden, skal bruge samme indgrebsvinkel.
- **Frigang** - Mindste afstand mellem tandtoppen og bunden af den modgående tand
- **Slør** - Mindste afstand mellem indgribende tandhjulstænder for at undgå binding

### Tandhjulsdata (skrivebeskyttet)

- **Stigningsradius** - Radius hvor tandhjulene griber ind i hinanden
- **Ydre diameter** - Den samlede diameter ud til tandtoppene

## Tips

- To tandhjul griber korrekt ind i hinanden, når de har samme Cirkulær tandhøjde og Indgrebsvinkel
- Brug værdierne for Stigningsradius til at placere indgribende tandhjul korrekt -- afstanden mellem tandhjulenes centre skal svare til summen af deres stigningsradier
- Tilføj Slør til 3D-printede tandhjul for at tage højde for printtolerancer
- For 2D-tandhjulsprofiler (til brug med Ekstrudér), se [Tandhjul 2D](gear-2d.md)

## Relateret

- [Tandhjul 2D](gear-2d.md) - 2D-tandhjulsbane til baneoperationer
- [Gevind](threads.md) - Opret gevindfunktioner
