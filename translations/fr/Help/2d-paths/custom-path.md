---
title: Chemin personnalisé
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Chemin personnalisé

Dessinez votre propre tracé 2D à l'aide de points de contrôle. Cela vous laisse une liberté totale pour créer n'importe quelle forme 2D, qui pourra ensuite être extrudée ou mise en révolution pour obtenir un objet 3D.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Utilisation

1. Ajoutez un **Chemin personnalisé** depuis la bibliothèque de chemins 2D
2. Modifiez les points de contrôle pour définir votre forme
3. Appliquez [Extrusion linéaire](../operations/path/linear-extrude.md) ou une autre opération de chemin pour créer un objet 3D

## Chemins ouverts et fermés

La case **Fermé** détermine si le tracé relie son dernier point à son premier.

- **Fermé** (valeur par défaut) fait du tracé le contour d'une région. C'est ce que remplissent [Extrusion linéaire](../operations/path/linear-extrude.md) et [Révolution](../operations/path/revolve.md).
- **Ouvrir** fait du tracé une ligne. Une ligne n'enferme rien : elle apparaît donc dans la scène comme un mince ruban suivant sa longueur, et non comme une forme pleine. Utilisez [Dilater le tracé](../operations/path/inflate-path.md) pour lui donner une largeur et en refaire quelque chose de solide.

Deux points à connaître avant de décocher **Fermé** :

- **Refermer n'est pas une annulation.** Ouvrir un tracé supprime son segment de fermeture. Si ce segment était courbe, recocher **Fermé** ramène une ligne droite, et non la courbe. Utilisez plutôt Ctrl+Z : l'annulation restaure exactement le tracé d'origine.
- **Certains contours refusent de s'ouvrir.** Un contour auquel il resterait moins de deux points — une goutte dessinée avec un seul point et une courbe revenant sur lui — reste fermé plutôt que de se réduire à quelque chose que vous ne pourriez plus voir ni cliquer. Il en va de même pour un contour contenant une courbe quadratique, ce qu'un SVG importé peut comporter : l'ouvrir aplatirait la courbe en un angle. Le refus s'applique contour par contour, le reste du tracé s'ouvre donc quand même.

Si un tracé comporte plusieurs contours et qu'ils ne concordent pas, la case est considérée comme ouverte. La cocher aligne tous les contours.

Les opérations qui ont besoin d'une région ferment un tracé ouvert pour vous plutôt que de le refuser. Extrusion linéaire, Révolution, Soustraire et les autres opérations booléennes le font toutes : un tracé ouvert produit donc le même solide que sa version fermée.

## Astuces

- Utilisez Chemin personnalisé lorsqu'aucune des formes de chemin intégrées ne correspond à ce dont vous avez besoin
- Pour importer des formes depuis des éditeurs vectoriels externes, voir [Objet SVG](../primitives/svg-object.md)
- Pour dessiner une ligne et la transformer en pièce, décochez **Fermé**, appliquez [Dilater le tracé](../operations/path/inflate-path.md) pour lui donner une épaisseur, puis [Extrusion linéaire](../operations/path/linear-extrude.md) pour lui donner une hauteur

## Voir aussi

- [Chemin Cercle](circle-path.md) - Un cercle prêt à l'emploi
- [Chemin Boîte](box-path.md) - Un rectangle prêt à l'emploi
- [Objet SVG](../primitives/svg-object.md) - Importer des tracés vectoriels depuis des fichiers SVG
- [Extrusion linéaire](../operations/path/linear-extrude.md) - Donner de la hauteur aux chemins
