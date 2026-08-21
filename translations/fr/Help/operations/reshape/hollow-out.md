---
title: Évider
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Évider

Évider crée une coquille creuse à partir d'un objet solide en décalant la surface vers l'intérieur. Le résultat est une version à paroi mince de la forme d'origine.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Utilisation

1. Sélectionnez un objet solide
2. Appliquez l'opération **Évider** depuis le menu Remodeler
3. Définissez l'épaisseur de paroi souhaitée

## Paramètres

- **Distance** - L'épaisseur de paroi en millimètres (par défaut : 2 mm). C'est l'épaisseur qu'aura la coquille résultante.
- **Nb cellules** - Résolution de l'algorithme d'évidement (par défaut : 64). Des valeurs plus élevées produisent des surfaces internes plus lisses mais demandent plus de temps de calcul.

## Astuces

- Évider est utile pour créer des boîtiers, des conteneurs, des vases et des pièces légères
- Une épaisseur de paroi de 1 à 2 mm est typique pour la plupart des pièces imprimées en 3D
- Augmentez Nb cellules si la surface interne paraît rugueuse ou en escalier
- L'évidement crée un fond ouvert -- combinez-le avec un [Cube](../../primitives/cube.md) si vous avez besoin d'une base fermée
- Pour les formes complexes, le calcul peut prendre quelques secondes

## Voir aussi

- [Coupe par plan](plane-cut.md) - Couper un objet à une hauteur précise
- [Soustraire](../boolean/subtract.md) - Retirer de la matière manuellement
