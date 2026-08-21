---
title: Expresii
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Expresii

Mulți parametri din MatterCAD acceptă expresii matematice în locul numerelor simple. Acest lucru permite proiectarea parametrică, în care modificarea unei valori actualizează automat dimensiunile asociate.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Mod de utilizare

În loc să introduceți un număr simplu într-un câmp de parametru, puteți introduce o expresie matematică. De exemplu:

- `20 + 5` se evaluează la 25
- `pi * 10` se evaluează la 31,416
- `width * 2` face referire la un alt parametru numit „width”

## Constante disponibile

- **pi** - 3,14159... (raportul dintre circumferință și diametru)
- **tau** - 6,28318... (2 * pi, o rotație completă în radiani)

## Operații acceptate

- Adunare: `+`
- Scădere: `-`
- Înmulțire: `*`
- Împărțire: `/`
- Paranteze: `(` și `)` pentru grupare

## Sfaturi

- Expresiile sunt acceptate în orice câmp care afișează `DoubleOrExpression`, `IntOrExpression` sau `StringOrExpression` în cod -- în practică, majoritatea câmpurilor numerice din instrumentele de proiectare le acceptă
- Folosiți expresii pentru a crea relații între parametri -- de exemplu, setați diametrul unei găuri la `outer_diameter - 4` astfel încât să aibă întotdeauna pereți de 2 mm
- Expresiile se actualizează automat atunci când valorile referite se modifică
- Folosiți o [Foaie de variabile](variable-sheet.md) atunci când mai multe obiecte trebuie să folosească aceleași valori sau formule denumite
- Puteți folosi expresii în operațiile [Matrice](../operations/array/index.md) pentru a crea modele parametrice

## Articole conexe

- [Componente](components.md) - Creați modele parametrizate reutilizabile
- [Foaie de variabile](variable-sheet.md) - Stocați valori și formule partajate pentru un model
- [Editarea obiectelor](../getting-started/editing-objects.md) - Lucrul cu parametrii obiectelor
