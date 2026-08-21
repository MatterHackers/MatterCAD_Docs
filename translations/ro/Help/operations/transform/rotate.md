---
title: Rotire
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Rotire

Rotire întoarce un obiect în jurul unei axe specificate cu un unghi dat. Puteți roti în jurul oricărei direcții de axă și puteți alege punctul central al rotației.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Mod de utilizare

1. Selectați un obiect
2. Aplicați operațiunea **Rotire** din meniul Transformare
3. Setați unghiul și axa de rotație în panoul Proprietăți

De asemenea, puteți roti obiectele direct în fereastra de vizualizare, făcând clic pe controalele de rotire din colțurile unui obiect selectat. Deplasarea mouse-ului peste indicatorii de unghi face fixarea la incremente de 45 de grade.

## Parametri

- **Unghi** - Unghiul de rotație în grade (interval: 3-360). Acceptă [expresii](../../workspace/expressions.md).
- **Rotire în jurul** - Definește axa de rotație și punctul de origine. Puteți roti în jurul axei X, Y sau Z ori puteți specifica o direcție personalizată.

## Sfaturi

- În mod implicit, rotația este centrată pe centrul casetei de încadrare a obiectului
- Pentru rotații de 90 de grade, indicatorii de fixare facilitează obținerea valorilor exacte
- Folosiți operațiunea Rotire (în locul controalelor din fereastra de vizualizare) atunci când aveți nevoie de un unghi precis care nu este un multiplu de 45 de grade
- Puteți schimba axa de rotație după aplicarea operațiunii, editând proprietatea Rotire în jurul

## Articole conexe

- [Translatare](translate.md) - Mută un obiect cu o distanță specificată
- [Scalare](scale.md) - Redimensionează un obiect
- [Oglindire](mirror.md) - Creează o reflexie în oglindă
