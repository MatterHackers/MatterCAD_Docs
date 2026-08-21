---
title: Filete
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Filete

Creați filete de șurub cu diametru, pas și profil de filet configurabile. Filetele pot fi folosite ca șuruburi/bolțuri de sine stătătoare sau pot fi scăzute din alte obiecte pentru a crea găuri filetate.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Mod de utilizare

1. Adăugați **Filete** din instrumentele Mecanic sau din panoul Primitive
2. Setați diametrul, pasul și numărul de rotații
3. Opțional, activați „Utilizare ca Gaură” pentru a crea găuri filetate

## Parametri

### Utilizare

- **Utilizare ca Gaură** - Când este activată, filetele sunt dimensionate cu o toleranță suplimentară pentru a fi folosite ca gaură scăzută (implicit: dezactivat)
- **Toleranță** - Joc suplimentar pentru ajustaj atunci când sunt folosite ca gaură (implicit: 0,2 mm, vizibil când Utilizare ca Gaură este activată)

### Atribute

- **Diametru** - Diametrul exterior al secțiunii filetate (implicit: 10 mm)
- **Pas** - Distanța dintre fiecare spiră a filetului (implicit: 2 mm). Pas mai mic = filete mai fine
- **Scară filet** - Lățimea filetelor ca raport față de pas (implicit: 1,0, interval: 0,1-1,0)
- **Rotații** - Numărul de spire complete ale filetului (implicit: 10)

### Geometrie

- **Laturi** - Numărul de segmente de pe perimetru (implicit: 40). Mai multe = mai neted

### Vârfuri (capetele filetului)

- **Scară vârf** - Cât de mult se conicizează capetele filetului (implicit: 0, interval: 0-1). Setați peste 0 pentru a crea o intrare conică la capete
- **Unghi vârf** - Unghiul pe care se face conicizarea vârfurilor (implicit: 90 de grade)

## Sfaturi

- Pentru a crea o gaură filetată: activați „Utilizare ca Gaură”, poziționați filetele și aplicați [Scădere](../operations/boolean/subtract.md) din obiectul dumneavoastră
- Adăugați Toleranță atunci când le folosiți ca gaură, pentru ca piesele imprimate să se potrivească între ele
- Pași standard pentru filete metrice: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Folosiți Scară vârf pentru a crea o intrare conică ce ușurează începerea înfiletării

## Articole conexe

- [Roți dințate](gears.md) - Creați forme de roți dințate mecanice
- [Cilindru](../primitives/cylinder.md) - O coloană rotundă simplă (fără filete)
- [Scădere](../operations/boolean/subtract.md) - Decupați filete din alte obiecte pentru a crea găuri
