---
title: Sphère
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Sphère

Une forme de boule ronde avec un diamètre et un niveau de détail réglables.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Paramètres

- **Diamètre** - La largeur de la sphère (par défaut : 20 mm)
- **Côtés** - Nombre de segments autour du périmètre (par défaut : 40). Plus de côtés = surface plus lisse

### Paramètres avancés

Activez le mode **Avancé** pour accéder à des contrôles supplémentaires :

- **Angle de départ** - Angle où commence la surface de la sphère (par défaut : 0)
- **Angle final** - Angle où se termine la surface de la sphère (par défaut : 360). Définissez une valeur inférieure à 360 pour obtenir des formes de sphère partielle
- **Côtés en latitude** - Nombre de segments du haut vers le bas (par défaut : 30). Plus = pôles plus lisses

## Astuces

- Pour l'impression 3D, 40 côtés suffisent généralement. Des valeurs plus élevées créent des surfaces plus lisses mais des fichiers plus volumineux
- Utilisez l'Angle de départ et l'Angle final pour créer des formes de sphère partielle comme des bols ou des dômes
- Combinez avec [Soustraire](../operations/boolean/subtract.md) pour créer des cavités sphériques

## Voir aussi

- [Demi-sphère](half-sphere.md) - Uniquement l'hémisphère supérieur
- [Tore](torus.md) - Une forme de beignet
