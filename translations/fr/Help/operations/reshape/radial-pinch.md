---
title: Pincement radial
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Pincement radial

Le Pincement radial comprime un objet vers l'intérieur à partir d'un point central, selon une courbe de profil personnalisable. Contrairement au [Pincement](pinch.md) classique, qui agit de l'arrière vers l'avant, le Pincement radial comprime symétriquement autour d'un axe central.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Pincement radial** depuis le menu Remodeler
3. Modifiez le profil du chemin pour définir la quantité de pincement appliquée à chaque hauteur
4. Ajustez le nombre de tranches pour plus de régularité

## Paramètres

- **Chemin** - Un éditeur de courbe de profil qui définit la quantité de pincement à chaque niveau de hauteur. Modifiez la courbe pour créer des profils de pincement personnalisés
- **Tranches** - Nombre de coupes horizontales pour un pincement régulier, réparties uniformément sur la hauteur de la pièce. Plus il y a de tranches, plus le résultat est lisse

### Paramètres avancés

- **Type de pincement** - Direction de la compression :
  - **Radial** - Comprime uniformément de tous les côtés vers le centre
  - **Axe X** - Comprime uniquement le long de l'axe X
  - **Axe Y** - Comprime uniquement le long de l'axe Y
- **Décalage de rotation** - Décale le centre de l'effet de pincement

## Astuces

- Utilisez l'éditeur de chemin pour créer des formes de sablier, de bouteille ou de vase
- Le pincement radial est idéal pour créer des formes organiques et arrondies à partir d'objets cylindriques
- Augmentez le nombre de Tranches pour obtenir des courbes plus lisses, en particulier sur les profils de pincement serrés

## Voir aussi

- [Pincement](pinch.md) - Compression simple de l'arrière vers l'avant
- [Torsion](twist.md) - Rotation en spirale sur la hauteur
- [Courbe](curve.md) - Courber en arc
