---
title: Gaură
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Gaură

Un obiect în formă de cub, preconfigurat pentru a acționa ca instrument de scădere booleană. Când folosiți [Combină](../operations/boolean/combine.md), obiectele de tip Gaură sunt scăzute automat din celelalte forme, în loc să fie adăugate la ele.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Cum funcționează

Primitiva Gaură funcționează ca un [Cub](cube.md), dar are tipul de ieșire setat pe „Gaură”. Când combinați obiecte care includ o Gaură, volumul Găurii este eliminat din rezultat.

## Parametri

La fel ca la [Cub](cube.md):

- **Lățime** - Dimensiunea pe axa X
- **Adâncime** - Dimensiunea pe axa Y
- **Înălțime** - Dimensiunea pe axa Z

## Sfaturi

- Poziționați Gaura astfel încât să se suprapună cu obiectul pe care doriți să îl tăiați
- Faceți ca Gaura să treacă complet prin obiectul țintă dacă doriți o gaură străpunsă
- Puteți folosi forme obișnuite cu [Scădere](../operations/boolean/subtract.md) pentru același efect, dar Găurile sunt convenabile deoarece funcționează automat cu [Combină](../operations/boolean/combine.md)
- Pentru găuri rotunde, folosiți în schimb un [Cilindru](cylinder.md) cu Scădere

## Subiecte conexe

- [Cub](cube.md) - Aceeași formă, fără comportamentul de gaură
- [Combină](../operations/boolean/combine.md) - Îmbină formele și scade automat Găurile
- [Scădere](../operations/boolean/subtract.md) - Scădeți manual orice formă dintr-o alta
