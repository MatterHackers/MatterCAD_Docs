---
title: Crearea de obiecte noi
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Crearea de obiecte noi

MatterCAD oferă un set bogat de unelte pentru crearea obiectelor 3D. Puteți începe cu forme primitive, puteți folosi unelte specializate precum textul și codurile QR sau puteți construi forme complexe cu ajutorul operațiilor booleene și al matricelor.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Adăugarea de primitive

Cel mai rapid mod de a începe un proiect este adăugarea de forme primitive. Deschideți panoul Primitive din bibliotecă și faceți clic pe orice formă pentru a o adăuga în spațiul de lucru. Primitivele disponibile includ:

- **Forme de bază** - Cub, Cilindru, Sferă, Con, Tor, Inel, Piramidă, Pană și variantele lor pe jumătate
- **Text și speciale** - Text, Braille, Cod QR, Obiect Imagine, Obiect SVG

Fiecare primitivă are parametri pe care îi puteți ajusta în panoul Proprietăți după ce o selectați. De exemplu, un Cub are controalele Lățime, Adâncime și Înălțime. Consultați [Primitive](../primitives/index.md) pentru detalii despre fiecare formă.

## Bara de unelte pentru operații

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

Bara de unelte din partea de sus a ferestrei de vizualizare vă oferă acces rapid la operațiile uzuale:

- **Anulează / Refacere** - Anulați sau reaplicați modificările. De asemenea, puteți folosi **Ctrl+Z** pentru anulare și **Ctrl+Y** pentru refacere
- **Grupează / Degrupează** - Combinați obiectele selectate într-un grup care se mută și funcționează ca o singură unitate sau desfaceți un grup
- **Copiază / Ștergere** - Duplicați sau eliminați obiectele selectate. Funcționează și scurtăturile standard **Ctrl+C**, **Ctrl+X** și **Ctrl+V**
- **Aliniere** - Poziționați mai multe obiecte unul față de celălalt
- **Operații booleene** - [Combină](../operations/boolean/combine.md), [Scădere](../operations/boolean/subtract.md), [Intersectare](../operations/boolean/intersect.md) și [Scade și înlocuiește](../operations/boolean/subtract-and-replace.md)
- **Matrice** - Creați [tipare liniare, radiale, pe curbă și de transformare](../operations/array/array.md) din obiecte duplicate
- **Transformări** - Aplicați [Rotire](../operations/transform/rotate.md), [Scalare](../operations/transform/scale.md), [Oglindire](../operations/transform/mirror.md) și alte modificări

## Construirea formelor complexe

Majoritatea proiectelor din MatterCAD sunt construite prin combinarea unor forme simple:

1. **Începeți cu primitive** - Adăugați formele de bază de care aveți nevoie
2. **Poziționați-le** - Mutați și rotiți obiectele astfel încât să se suprapună acolo unde doriți
3. **Aplicați operații booleene** - Folosiți [Combină](../operations/boolean/combine.md) pentru a îmbina formele sau [Scădere](../operations/boolean/subtract.md) pentru a decupa o formă din alta
4. **Rafinați** - Folosiți operații [Remodelează](../operations/reshape/index.md) precum Teșitură, Curbă sau Răsucire pentru a adăuga detalii

## Articole conexe

- [Primitive](../primitives/index.md) - Referință completă pentru toate formele primitive
- [Adăugarea obiectelor existente](adding-existing-objects.md) - Importați fișiere în loc să creați de la zero
- [Operații booleene](../operations/boolean/index.md) - Combinați formele în structuri complexe
- [Editarea obiectelor](editing-objects.md) - Mutați, rotiți și scalați obiectele după ce le creați
