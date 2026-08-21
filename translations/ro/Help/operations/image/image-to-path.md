---
title: Imagine în traseu
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Imagine în traseu

Imagine în traseu trasează conturul unei imagini pentru a crea căi 2D. Aceste căi pot fi apoi extrudate, revoluționate sau folosite cu orice altă operație cu căi. Este ideală pentru convertirea siglelor, siluetelor și graficii simple în obiecte 3D.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Mod de utilizare

1. Selectează un obiect imagine în spațiul de lucru
2. Aplică **Imagine în traseu** din meniul de operații Imagine
3. Alege tipul de analiză și ajustează intervalul de selecție

## Parametri

- **Tip de analiză** - Modul în care imaginea este analizată pentru trasare:
  - **Transparență** - Trasează pe baza zonelor transparente față de cele opace (ideal pentru fișiere PNG cu fundal transparent)
  - **Culori** - Trasează pe baza regiunilor de culoare
  - **Intensitate** - Trasează pe baza nivelurilor de luminozitate (ideal pentru majoritatea imaginilor)
- **Selectare interval** - Un control de tip histogramă pentru a selecta valorile de luminozitate/culoare incluse în trasare
- **Suprafață minimă** - Aria minimă necesară pentru ca o buclă de cale să fie inclusă. Mărește valoarea pentru a filtra micile artefacte de zgomot

## Sfaturi

- Cele mai bune rezultate se obțin cu imagini curate, cu contrast ridicat și forme simple
- Folosește modul Transparență pentru imagini PNG cu fundal transparent
- Folosește modul Intensitate pentru fotografii și imagini fără transparență
- După trasare, aplică [Extrudare liniară](../path/linear-extrude.md) pentru a da înălțime căii
- Mărește valoarea Suprafață minimă pentru a elimina din trasare detaliile mici nedorite

## Subiecte conexe

- [Convertor de imagini](image-converter.md) - Creează un relief de tip hartă de înălțime în loc de căi plane
- [Litofanie](lithophane.md) - Creează afișaje de imagini iluminate din spate
- [Obiect SVG](../../primitives/svg-object.md) - Importă direct grafică vectorială (fără a fi nevoie de trasare)
- [Extrudare liniară](../path/linear-extrude.md) - Dă înălțime căii trasate
