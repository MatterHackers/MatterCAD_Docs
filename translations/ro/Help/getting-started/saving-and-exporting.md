---
title: Se salvează și Se exportă
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Se salvează și Se exportă

MatterCAD acceptă mai multe formate de fișier pentru salvarea și exportarea proiectelor dumneavoastră. Formatul pe care îl alegeți depinde de modul în care intenționați să utilizați fișierul.

## Formate de salvare

### MCX (format nativ)

MCX este formatul de fișier nativ al MatterCAD și cea mai bună alegere pentru proiectele pe care doriți să le editați ulterior. Acesta păstrează:

- Arborele complet al proiectului, cu toate obiectele și ierarhia lor
- Toți parametrii și setările fiecărui obiect
- Operațiile booleene, matricele și alte operații în formă editabilă
- Relațiile dintre componente

**Folosiți MCX când:** doriți să vă salvați lucrarea și să continuați editarea ei ulterior.

### STL

STL este cel mai utilizat format pentru imprimarea 3D. Conține doar geometria finală a rețelei de triunghiuri, fără istoricul proiectului sau parametri.

**Folosiți STL când:** doriți să imprimați 3D proiectul sau să îl partajați cu cineva care nu folosește MatterCAD.

### OBJ

OBJ (Wavefront) este un format 3D uzual, acceptat de majoritatea programelor 3D. La fel ca STL, conține doar geometria de tip rețea.

**Folosiți OBJ când:** trebuie să deschideți proiectul în alte programe 3D, precum Blender sau un motor de joc.

### SVG

Exportul SVG creează un fișier vectorial 2D din vederea de sus a proiectului. Acest lucru este util pentru tăierea cu laser sau frezarea CNC.

**Folosiți SVG când:** aveți nevoie de un contur 2D al proiectului pentru tăiere cu laser sau gravare.

## Cum se salvează

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Deschideți **meniul de brand** (sigla MatterCAD din colțul din stânga sus)
2. Alegeți **Salvare ca** pentru a alege o locație și un format
3. Selectați formatul de fișier din lista derulantă de formate
4. Alegeți unde să salvați fișierul și faceți clic pe **Salvare**

Proiectul este salvat automat și pe măsură ce lucrați, așa că nu veți pierde modificările dacă închideți aplicația.

## Sfaturi

- Salvați întotdeauna o copie MCX a proiectului înainte de a exporta în STL sau OBJ, pentru a putea face modificări ulterior
- La exportul STL, toate obiectele din scenă sunt îmbinate într-o singură rețea
- Dacă trebuie să partajați un proiect cu cineva care folosește MatterCAD, trimiteți fișierul MCX pentru a păstra editabilitatea completă
- De asemenea, puteți salva proiecte în [Bibliotecă cloud](../library/cloud-library.md) pentru a le accesa de pe orice computer

## Articole conexe

- [Adăugarea obiectelor existente](adding-existing-objects.md) - Importați fișiere în MatterCAD
- [Bibliotecă](../library/index.md) - Organizați-vă proiectele salvate
- [Bibliotecă cloud](../library/cloud-library.md) - Stocați proiecte în cloud
