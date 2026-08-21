---
title: Extrusion linéaire
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Extrusion linéaire

L'Extrusion linéaire donne de la hauteur à un chemin 2D, transformant une forme plane en solide 3D. C'est la principale façon de convertir des chemins en objets 3D.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Utilisation

1. Sélectionnez un chemin 2D ou un objet basé sur un chemin
2. Appliquez **Extrusion linéaire** depuis le menu des opérations de Chemin
3. Définissez la hauteur souhaitée

## Paramètres

- **Hauteur** - Hauteur de l'extrusion (par défaut : 5 mm, plage : 0,1-50 mm)
- **Chanfreiner le haut** - Ajoute une arête chanfreinée (arrondie) sur le dessus de l'extrusion (par défaut : désactivé)

### Paramètres du chanfrein (visibles lorsque Chanfreiner le haut est activé)

- **Style** - Le style de profil du chanfrein (Vif ou arrondi)
- **Rayon** - Largeur d'extension du chanfrein (par défaut : 3 mm)
- **Segments** - Régularité de la courbe du chanfrein (par défaut : 9)

## Astuces

- Cela fonctionne avec n'importe quel chemin 2D : [Cercle](../../2d-paths/circle-path.md), [Boîte](../../2d-paths/box-path.md), [Étoile](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) et les chemins [Personnalisé](../../2d-paths/custom-path.md)
- Activez Chanfreiner le haut pour un rendu plus soigné et professionnel
- Pour faire tourner un chemin autour d'un axe au lieu de l'extruder verticalement, voir [Révolution](revolve.md)

## Voir aussi

- [Révolution](revolve.md) - Faire tourner un chemin autour d'un axe
- [Chemins 2D](../../2d-paths/index.md) - Formes de chemins disponibles
- [Texte](../../primitives/text.md) - Le texte est extrudé automatiquement
