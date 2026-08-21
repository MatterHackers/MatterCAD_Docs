---
title: Déplacer
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# Déplacer

Déplacer déplace un objet d'une distance précise le long des axes X, Y et/ou Z. Contrairement au glissement d'un objet à la souris, Déplacer vous permet de saisir des valeurs de décalage exactes.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Déplacer** depuis le menu Transformer
3. Saisissez les valeurs de décalage souhaitées pour X, Y et Z dans le panneau Propriétés

## Paramètres

- **X, Y, Z** (Déplacement) - La distance dont l'objet est déplacé le long de chaque axe, en millimètres. Prend en charge les [expressions](../../workspace/expressions.md) pour les valeurs calculées.

## Astuces

- Utilisez Déplacer lorsque vous avez besoin d'un positionnement précis et reproductible, que vous pourrez ajuster ultérieurement
- Les valeurs de déplacement sont relatives à la position actuelle de l'objet : saisir 10 pour X le déplace de 10 mm vers la droite depuis sa position actuelle
- Pour un repositionnement rapide, vous pouvez également faire glisser les objets directement dans la fenêtre 3D. Voir [Modification des objets](../../getting-started/editing-objects.md)

## Voir aussi

- [Pivoter](rotate.md) - Faire pivoter un objet d'un angle précis
- [Échelle](scale.md) - Redimensionner un objet avec précision
- [Aligner](../placement/align.md) - Positionner des objets les uns par rapport aux autres
