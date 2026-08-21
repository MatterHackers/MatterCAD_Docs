---
title: Reducere
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Reducere (Decimare)

Reducere scade numărul de poligoane al unei plase păstrând forma generală. Este utilă pentru simplificarea modelelor foarte detaliate, reducerea dimensiunii fișierului și accelerarea operațiilor pe geometrii complexe.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Mod de utilizare

1. Selectați un obiect
2. Aplicați operația **Reducere** din meniul Plasă
3. Alegeți ținta (număr sau procentaj) și ajustați-o

## Parametri

- **Mod** - Alegeți cum se specifică ținta:
  - **Procent** - Păstrează un procent din poligoanele originale (implicit: 50%)
  - **Număr** - Vizează un număr specific de poligoane
- **Număr poligoane sursă** - Numărul original de poligoane (doar citire)
- **Procent țintă** - Procentul de poligoane păstrate (vizibil în modul Procent)
- **Număr țintă** - Numărul exact de poligoane păstrate (vizibil în modul Număr)
- **Număr după reducerea procentuală** - Numărul final de poligoane după reducerea procentuală (doar citire)
- **Menține suprafața** - Proiectează vârfurile înapoi pe suprafața originală pentru o acuratețe mai mare (mai lent, dar mai fidel formei originale)

## Sfaturi

- O reducere de 50% păstrează de obicei bine calitatea vizuală
- Activați Menține suprafața atunci când acuratețea contează mai mult decât viteza
- Reducerea numărului de poligoane accelerează operațiile booleene pe modelele importate complexe
- Un număr foarte mic de poligoane va degrada vizibil forma -- verificați rezultatul înainte de a-l accepta

## Articole conexe

- [Repară](repair.md) - Remediază problemele plasei
