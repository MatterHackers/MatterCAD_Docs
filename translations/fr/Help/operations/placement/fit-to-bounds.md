---
title: Ajuster aux limites
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Ajuster aux limites

Ajuster aux limites met à l'échelle un objet pour qu'il tienne dans des dimensions de largeur, de profondeur et de hauteur spécifiées. Vous pouvez contrôler la façon dont l'objet s'étire et s'aligne à l'intérieur des limites cibles.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Ajuster aux limites** depuis le menu Placement
3. Saisissez les dimensions cibles
4. Choisissez le verrouillage des proportions et le comportement d'étirement

## Paramètres

- **Verrouiller les proportions** - Comment contraindre les proportions :
  - **Aucun** - Chaque axe peut être défini indépendamment
  - **X et Y** - La largeur et la profondeur sont verrouillées ensemble
  - **X, Y et Z** - Mise à l'échelle uniforme sur tous les axes
- **Largeur** - Largeur cible (dimension X)
- **Profondeur** - Profondeur cible (dimension Y)
- **Hauteur** - Hauteur cible (dimension Z)

### Lorsque Verrouiller les proportions est réglé sur X et Y ou X, Y et Z

- **Étirer** - Comment l'objet s'ajuste :
  - **Intérieur** - Réduire l'échelle pour tenir entièrement dans les limites (peut laisser des espaces)
  - **Développer** - Augmenter l'échelle pour remplir les limites (peut dépasser dans certaines dimensions)

### Lorsque Verrouiller les proportions est réglé sur Aucun

Chaque axe possède ses propres réglages :

- **Étirer** - Intérieur ou Développer par axe
- **Aligner** - Où se positionner à l'intérieur des limites (Min, Centre, Max)

## Astuces

- Utilisez cette opération pour redimensionner des modèles importés à des dimensions cibles exactes
- Verrouillez toutes les proportions pour une mise à l'échelle uniforme qui conserve la forme d'origine
- Utilisez le contrôle par axe lorsque vous devez respecter une largeur précise sans vous soucier des autres dimensions

## Voir aussi

- [Échelle](../transform/scale.md) - Mettre à l'échelle par rapport ou pourcentage plutôt que par taille cible
- [Ajuster au cylindre](fit-to-cylinder.md) - Ajuster à l'intérieur d'une limite cylindrique
- [Aligner](align.md) - Positionner les objets les uns par rapport aux autres
