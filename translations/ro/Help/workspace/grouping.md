---
title: Grupare
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Grupare

Gruparea combină mai multe obiecte într-o singură unitate care poate fi mutată, copiată și prelucrată ca un singur obiect. Spre deosebire de [Combină](../operations/boolean/combine.md), gruparea nu îmbină geometria -- fiecare obiect rămâne separat în interiorul grupului.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Mod de utilizare

### Gruparea obiectelor

1. Selectați două sau mai multe obiecte (Shift-clic sau Ctrl-clic pentru selecție multiplă)
2. Faceți clic pe butonul **Grupează** din bara de instrumente
3. Obiectele sunt acum grupate -- se deplasează împreună, ca o singură unitate

### Degruparea obiectelor

1. Selectați un grup
2. Faceți clic pe butonul **Degrupează** din bara de instrumente
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Obiectele individuale sunt restaurate ca elemente separate

Degruparea încearcă, de asemenea, să separe mai multe corpuri dintr-un singur fișier STL importat, dacă acestea există.

## Grupează vs. Combină

| Caracteristică | Grupează | Combină |
|---------|-------|---------|
| Obiectele rămân separate | Da | Nu |
| Se poate degrupa ulterior | Da | Nu (distructiv) |
| Îmbină geometria suprapusă | Nu | Da |
| Obiectele pot avea culori diferite | Da | Culori păstrate per față |
| Caz de utilizare | Organizare și deplasare | Crearea de forme solide unice |

## Sfaturi

- Grupurile pot fi imbricate -- puteți grupa obiecte care se află deja în grupuri
- Selectați un grup și consultați Arborele de proiectare pentru a vedea și selecta obiectele individuale din interiorul acestuia
- Gruparea este nedistructivă și poate fi întotdeauna anulată cu Degrupează

## Articole conexe

- [Combină](../operations/boolean/combine.md) - Îmbină obiectele într-un singur solid în loc să le grupeze
- [Selecție](selection.md) - Cum să selectați mai multe obiecte pentru grupare
- [Componente](components.md) - Creați grupuri parametrizate reutilizabile
