---
title: Échelle
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Échelle

L'opération Échelle redimensionne un objet avec un contrôle précis des dimensions, des proportions et de la conversion d'unités. Vous pouvez mettre à l'échelle de façon uniforme, verrouiller certains axes entre eux ou redimensionner chaque axe indépendamment.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Échelle** depuis le menu Transformer
3. Choisissez votre méthode de mise à l'échelle et saisissez les valeurs souhaitées

Vous pouvez aussi mettre à l'échelle des objets dans la fenêtre de visualisation en cliquant sur les poignées d'échelle situées aux coins d'un objet sélectionné et en les faisant glisser.

## Paramètres

### Type de mise à l'échelle

Choisissez un préréglage ou une mise à l'échelle personnalisée :

- **Personnalisé** - Saisissez vos propres dimensions ou pourcentages
- **Pouces en mm** - Multiplie par 25,4 (conversion des unités impériales en unités métriques)
- **mm en pouces** - Multiplie par 0,0393 (conversion des unités métriques en unités impériales)
- **mm en cm** - Multiplie par 0,1
- **cm en mm** - Multiplie par 10

### Méthode de mise à l'échelle (mode Personnalisé)

- **Direct** - Saisissez la Largeur, la Profondeur et la Hauteur souhaitées en millimètres
- **Pourcentage** - Saisissez la Largeur, la Profondeur et la Hauteur en pourcentage de la taille d'origine

### Verrouiller les proportions

- **Aucun (Mise à l'échelle libre)** - Chaque axe est mis à l'échelle indépendamment
- **X et Y** - La Largeur et la Profondeur sont verrouillées ensemble ; la Hauteur est mise à l'échelle indépendamment
- **X, Y et Z** - Les trois axes sont mis à l'échelle uniformément ensemble

### Dimensions

- **Largeur** - Taille le long de l'axe X
- **Profondeur** - Taille le long de l'axe Y
- **Hauteur** - Taille le long de l'axe Z

## Conseils

- Utilisez « Pouces en mm » si vous avez importé un fichier STL conçu en pouces et qu'il apparaît trop petit
- Réglez Verrouiller les proportions sur X, Y et Z pour une mise à l'échelle uniforme : modifier une dimension les met toutes à jour
- La position de la base de l'objet est conservée pendant la mise à l'échelle, afin qu'il reste posé sur la surface de l'espace de travail
- Vous pouvez saisir des valeurs exactes pour un dimensionnement précis, ou utiliser les curseurs pour des ajustements rapides

## Voir aussi

- [Déplacer](translate.md) - Déplacer un objet
- [Pivoter](rotate.md) - Faire pivoter un objet
- [Ajuster aux limites](../placement/fit-to-bounds.md) - Mettre à l'échelle pour tenir dans une taille donnée
