---
title: Chemin en étoile
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Chemin en étoile

Un chemin 2D en forme d'étoile dont le nombre de branches et les rayons interne/externe sont configurables. À utiliser avec [Extrusion linéaire](../operations/path/linear-extrude.md) pour créer des formes d'étoile en 3D.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Paramètres

- **Branches** - Nombre de branches de l'étoile
- **Rayon externe** - Distance du centre à la pointe de chaque branche
- **Rayon interne** - Distance du centre aux creux situés entre les branches

## Astuces

- Le rapport entre le Rayon interne et le Rayon externe détermine à quel point l'étoile est « pointue ». Un Rayon interne faible produit des branches nettes et prononcées.
- Réglez Branches sur 5 pour une étoile classique, sur 6 pour une étoile de David, ou sur une valeur plus élevée pour des formes évoquant un engrenage
- Utilisez [Lisser le chemin](../operations/path/smooth-path.md) sur un Chemin en étoile pour créer des formes d'étoile arrondies

## Voir aussi

- [Chemin circulaire](circle-path.md) - Un cercle lisse
- [Engrenage 2D](../mechanical/gear-2d.md) - Un véritable profil d'engrenage
- [Extrusion linéaire](../operations/path/linear-extrude.md) - Donner de la hauteur aux chemins
