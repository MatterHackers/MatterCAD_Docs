---
title: Symétrie
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Symétrie

Symétrie crée une copie réfléchie d'un objet par rapport à l'un des trois axes principaux. Le résultat est une version en miroir de la forme d'origine.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Utilisation

1. Sélectionner un objet
2. Appliquer l'opération **Symétrie** depuis le menu Transformer
3. Choisir l'axe par rapport auquel effectuer la symétrie

## Paramètres

- **Symétrie activée** - L'axe par rapport auquel effectuer la symétrie :
  - **Axe X** - Retourne l'objet de gauche à droite
  - **Axe Y** - Retourne l'objet d'avant en arrière
  - **Axe Z** - Retourne l'objet de haut en bas

## Astuces

- La symétrie est centrée sur la boîte englobante de l'objet, de sorte que le résultat en miroir occupe le même espace que l'original
- Les normales des faces sont automatiquement corrigées après la symétrie afin de préserver un rendu correct
- Utilisez Symétrie pour créer des conceptions symétriques : modélisez une moitié, puis appliquez-lui une symétrie et utilisez [Combiner](../boolean/combine.md) avec l'original
- La symétrie est non destructive : vous pouvez changer l'axe de symétrie à tout moment

## Voir aussi

- [Pivoter](rotate.md) - Faire pivoter un objet au lieu de lui appliquer une symétrie
- [Échelle](scale.md) - Redimensionner un objet
- [Combiner](../boolean/combine.md) - Fusionner l'original et la copie en miroir en un seul objet
