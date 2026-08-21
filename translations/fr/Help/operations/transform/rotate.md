---
title: Pivoter
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Pivoter

Pivoter fait tourner un objet autour d'un axe spécifié selon un angle donné. Vous pouvez pivoter autour de n'importe quelle direction d'axe et choisir le centre de rotation.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Pivoter** depuis le menu Transformer
3. Définissez l'angle et l'axe de rotation dans le panneau Propriétés

Vous pouvez aussi faire pivoter les objets directement dans la fenêtre de visualisation en cliquant sur les poignées de rotation situées aux coins d'un objet sélectionné. En déplaçant la souris sur les indicateurs d'angle, la rotation s'aligne par incréments de 45 degrés.

## Paramètres

- **Angle** - L'angle de rotation en degrés (plage : 3-360). Prend en charge les [expressions](../../workspace/expressions.md).
- **Pivoter autour de** - Définit l'axe de rotation et le point d'origine. Vous pouvez pivoter autour de l'axe X, Y ou Z, ou spécifier une direction personnalisée.

## Conseils

- La rotation est centrée par défaut sur le centre de la boîte englobante de l'objet
- Pour les rotations de 90 degrés, les indicateurs d'alignement facilitent l'obtention de valeurs exactes
- Utilisez l'opération Pivoter (plutôt que les commandes de la fenêtre de visualisation) lorsque vous avez besoin d'un angle précis qui n'est pas un multiple de 45 degrés
- Vous pouvez changer l'axe de rotation après avoir appliqué l'opération en modifiant la propriété Pivoter autour de

## Voir aussi

- [Déplacer](translate.md) - Déplacer un objet d'une distance déterminée
- [Échelle](scale.md) - Redimensionner un objet
- [Symétrie](mirror.md) - Créer une réflexion en miroir
