---
title: Trou
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Trou

Un objet en forme de cube préconfiguré pour servir d'outil de soustraction booléenne. Lorsque vous utilisez [Combiner](../operations/boolean/combine.md), les objets Trou sont automatiquement soustraits des autres formes au lieu de leur être ajoutés.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Fonctionnement

La primitive Trou fonctionne comme un [Cube](cube.md), mais son type de sortie est défini sur « Trou ». Lorsque vous combinez des objets comprenant un Trou, le volume du Trou est supprimé du résultat.

## Paramètres

Identiques à ceux du [Cube](cube.md) :

- **Largeur** - Taille selon l'axe X
- **Profondeur** - Taille selon l'axe Y
- **Hauteur** - Taille selon l'axe Z

## Conseils

- Positionnez le Trou de manière à ce qu'il chevauche l'objet que vous souhaitez découper
- Faites en sorte que le Trou traverse entièrement l'objet cible si vous voulez un trou débouchant
- Vous pouvez obtenir le même effet avec des formes ordinaires et [Soustraire](../operations/boolean/subtract.md), mais les Trous sont pratiques car ils fonctionnent automatiquement avec [Combiner](../operations/boolean/combine.md)
- Pour des trous ronds, utilisez plutôt un [Cylindre](cylinder.md) avec Soustraire

## Voir aussi

- [Cube](cube.md) - La même forme, sans le comportement de trou
- [Combiner](../operations/boolean/combine.md) - Fusionne les formes et soustrait automatiquement les Trous
- [Soustraire](../operations/boolean/subtract.md) - Soustraire manuellement une forme d'une autre
