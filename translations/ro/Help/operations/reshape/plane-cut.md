---
title: Tăiere cu plan
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Tăiere cu plan

Tăiere cu plan secționează un obiect la o înălțime specificată cu un plan orizontal, păstrând doar porțiunea aflată sub tăietură. Suprafața rezultată este acoperită cu o față plană.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Mod de utilizare

1. Selectați un obiect
2. Aplicați operația **Tăiere cu plan** din meniul Remodelează
3. Setați înălțimea de decupare

## Parametri

- **Înălțime decupare** - Înălțimea pe axa Z la care este secționat obiectul (implicit: 10mm, interval: 1-200mm)

## Sfaturi

- Folosiți Tăiere cu plan pentru a aplatiza partea superioară a unui model la o anumită înălțime
- Utilă pentru ajustarea modelelor importate sau pentru crearea unor baze plane
- Pentru tăierea cu o formă care nu este plană, folosiți în schimb [Scădere](../boolean/subtract.md) cu un alt obiect
- Pentru tăierea cu un plan înclinat, rotiți mai întâi obiectul, aplicați Tăiere cu plan, apoi rotiți-l înapoi

## Subiecte conexe

- [Intersectare](../boolean/intersect.md) - Păstrează doar zona în care obiectele se suprapun
- [Scădere](../boolean/subtract.md) - Taie cu orice formă, nu doar cu un plan
- [Golire interioară](hollow-out.md) - Creează un înveliș gol
