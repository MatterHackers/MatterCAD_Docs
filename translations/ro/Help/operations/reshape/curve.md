---
title: Curbă
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Curbă

Curbă îndoaie un obiect drept într-o formă de arc sau de cerc. Poți controla îndoirea specificând fie un unghi, fie un diametru în jurul căruia se înfășoară obiectul.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Cum se utilizează

1. Selectează un obiect
2. Aplică operațiunea **Curbă** din meniul Remodelează
3. Alege între tipul de îndoire Unghi sau Diametru
4. Ajustează parametrii pentru a obține curbura dorită

## Parametri

- **Tip îndoire** - Alege între:
  - **Unghi** - Specifică direct unghiul de îndoire (1-360 de grade)
  - **Diametru** - Specifică diametrul cercului în jurul căruia se înfășoară piesa
- **Direcție îndoire** - Îndoire în sus sau Îndoire în jos
- **Procent inițial** - Locul de-a lungul obiectului unde începe îndoirea (0-100%)
- **Divizare rețea** - Divizează rețeaua pentru curbe netede (implicit: activat)
- **Laturi minime per rotație** - Numărul minim de segmente de rețea pentru o rotație completă. Valori mai mari = curbe mai netede

### Parametri avansați

- **Procent început îndoire** - Procentajul măsurat din stânga la care începe îndoirea
- **Procent îndoire finală** - Procentajul măsurat din stânga la care se termină îndoirea

## Sfaturi

- Folosește Curbă pentru a crea arcade, inele și console îndoite din forme drepte
- Setarea unghiului la 360 înfășoară obiectul într-un inel complet
- Mărește valoarea Laturi minime per rotație pentru rezultate mai netede la îndoiri strânse
- Obiectul este îndoit de-a lungul lungimii sale (axa X)

## Înrudite

- [Răsucire](twist.md) - Rotire de-a lungul înălțimii în loc de îndoire
- [Tor](../../primitives/torus.md) - O formă de inel gata făcută
