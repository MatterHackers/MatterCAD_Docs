---
title: Réduire
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Réduire (décimation)

Réduire diminue le nombre de polygones d'un maillage tout en préservant la forme générale. Cette opération est utile pour simplifier les modèles très détaillés, réduire la taille des fichiers et accélérer les opérations sur les géométries complexes.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Réduire** depuis le menu Maillage
3. Choisissez votre cible (nombre ou pourcentage) et ajustez-la

## Paramètres

- **Mode** - Choisissez la façon de définir la cible :
  - **Pourcent** - Conserver un pourcentage des polygones d'origine (par défaut : 50 %)
  - **Nombre** - Viser un nombre de polygones précis
- **Nombre de polygones source** - Nombre de polygones d'origine (lecture seule)
- **Pourcentage cible** - Pourcentage de polygones à conserver (visible en mode Pourcent)
- **Nombre cible** - Nombre exact de polygones à conserver (visible en mode Nombre)
- **Nombre après réduction en pourcentage** - Nombre final de polygones après la réduction en pourcentage (lecture seule)
- **Conserver la surface** - Projette les sommets sur la surface d'origine pour une meilleure précision (plus lent, mais plus fidèle à la forme d'origine)

## Astuces

- Une réduction de 50 % préserve généralement bien la qualité visuelle
- Activez Conserver la surface lorsque la précision compte plus que la vitesse
- Réduire le nombre de polygones accélère les opérations booléennes sur les modèles importés complexes
- Un nombre de polygones très faible dégrade visiblement la forme : vérifiez le résultat avant de valider

## Voir aussi

- [Réparer](repair.md) - Corriger les problèmes de maillage
