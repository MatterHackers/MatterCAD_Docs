---
title: Créer de nouveaux objets
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Créer de nouveaux objets

MatterCAD propose un ensemble complet d'outils pour créer des objets 3D. Vous pouvez partir de formes primitives, utiliser des outils spécialisés comme le texte et les codes QR, ou construire des formes complexes à l'aide d'opérations booléennes et de réseaux.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Ajouter des primitives

Le moyen le plus rapide de commencer une conception est d'ajouter des formes primitives. Ouvrez le panneau Primitives dans la bibliothèque et cliquez sur une forme pour l'ajouter à votre espace de travail. Les primitives disponibles sont les suivantes :

- **Formes de base** - Cube, Cylindre, Sphère, Cône, Tore, Anneau, Pyramide, Coin, ainsi que leurs variantes en demi
- **Texte et spéciales** - Texte, Braille, Code QR, Objet image, Objet SVG

Chaque primitive possède des paramètres que vous pouvez régler dans le panneau Propriétés après l'avoir sélectionnée. Par exemple, un Cube dispose des réglages Largeur, Profondeur et Hauteur. Consultez [Primitives](../primitives/index.md) pour plus de détails sur chaque forme.

## La barre d'outils des opérations

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

La barre d'outils située en haut de la fenêtre d'affichage vous donne un accès rapide aux opérations courantes :

- **Annuler / Rétablir** - Annuler ou rejouer les modifications. Vous pouvez aussi utiliser **Ctrl+Z** pour annuler et **Ctrl+Y** pour rétablir
- **Grouper / Dissocier** - Combiner les objets sélectionnés en un groupe qui se déplace et se manipule comme une seule unité, ou séparer un groupe
- **Copier / Supprimer** - Dupliquer ou supprimer les objets sélectionnés. Les raccourcis standard **Ctrl+C**, **Ctrl+X** et **Ctrl+V** fonctionnent également
- **Aligner** - Positionner plusieurs objets les uns par rapport aux autres
- **Opérations booléennes** - [Combiner](../operations/boolean/combine.md), [Soustraire](../operations/boolean/subtract.md), [Intersecter](../operations/boolean/intersect.md) et [Soustraire et remplacer](../operations/boolean/subtract-and-replace.md)
- **Réseaux** - Créer des [motifs linéaires, radiaux, sur courbe et par transformation](../operations/array/array.md) d'objets dupliqués
- **Transformations** - Appliquer [Pivoter](../operations/transform/rotate.md), [Échelle](../operations/transform/scale.md), [Symétrie](../operations/transform/mirror.md) et d'autres modifications

## Construire des formes complexes

La plupart des conceptions dans MatterCAD sont construites en combinant des formes simples :

1. **Démarrer avec des primitives** - Ajoutez les formes de base dont vous avez besoin
2. **Les positionner** - Déplacez et faites pivoter les objets pour qu'ils se chevauchent à l'endroit voulu
3. **Appliquer des opérations booléennes** - Utilisez [Combiner](../operations/boolean/combine.md) pour fusionner des formes, ou [Soustraire](../operations/boolean/subtract.md) pour découper une forme dans une autre
4. **Affiner** - Utilisez les opérations [Remodeler](../operations/reshape/index.md) comme Chanfrein, Courbe ou Torsion pour ajouter du détail

## Voir aussi

- [Primitives](../primitives/index.md) - Référence complète de toutes les formes primitives
- [Ajouter des objets existants](adding-existing-objects.md) - Importer des fichiers au lieu de créer à partir de zéro
- [Opérations booléennes](../operations/boolean/index.md) - Combiner des formes en volumes complexes
- [Modifier des objets](editing-objects.md) - Déplacer, faire pivoter et mettre à l'échelle les objets après les avoir créés
