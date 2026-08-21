---
title: Courbe
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Courbe

Courbe plie un objet droit pour lui donner une forme d'arc ou circulaire. Vous pouvez contrôler la courbure en spécifiant soit un angle, soit un diamètre autour duquel enrouler l'objet.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Courbe** depuis le menu Remodeler
3. Choisissez entre le type de courbure Angle ou Diamètre
4. Ajustez les paramètres pour obtenir la courbure souhaitée

## Paramètres

- **Type de courbure** - Choisissez entre :
  - **Angle** - Spécifier directement l'angle de courbure (1 à 360 degrés)
  - **Diamètre** - Spécifier le diamètre du cercle autour duquel la pièce s'enroule
- **Direction de pliage** - Plier vers le haut ou Plier vers le bas
- **Pourcentage de départ** - Endroit, le long de l'objet, où la courbure commence (0 à 100 %)
- **Diviser le maillage** - Divise le maillage pour obtenir des courbes lisses (par défaut : activé)
- **Nombre min. de côtés par rotation** - Nombre minimum de segments de maillage par révolution complète. Des valeurs plus élevées = des courbes plus lisses

### Paramètres avancés

- **Pourcentage de début de courbure** - Pourcentage depuis la gauche où la courbure commence
- **Pourcentage de courbure finale** - Pourcentage depuis la gauche où la courbure se termine

## Conseils

- Utilisez Courbe pour créer des arches, des anneaux et des supports pliés à partir de formes droites
- Régler l'angle sur 360 enroule l'objet en un anneau complet
- Augmentez le Nombre min. de côtés par rotation pour obtenir des résultats plus lisses sur les courbures serrées
- L'objet est plié dans le sens de sa longueur (axe X)

## Voir aussi

- [Torsion](twist.md) - Pivoter le long de la hauteur au lieu de plier
- [Tore](../../primitives/torus.md) - Une forme d'anneau prête à l'emploi
