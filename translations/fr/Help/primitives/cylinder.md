---
title: Cylindre
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Cylindre

Une forme de colonne ronde avec un diamètre, une hauteur et un nombre de côtés configurables. Le Cylindre est essentiel pour créer des broches, des tiges, des trous et des éléments arrondis.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Paramètres

- **Diamètre** - La largeur du cylindre (par défaut : 20 mm)
- **Hauteur** - La hauteur du cylindre (par défaut : 20 mm)
- **Côtés** - Nombre de segments autour du périmètre (par défaut : 40). Des valeurs faibles créent des formes polygonales (par exemple, 6 pour un hexagone)

### Paramètres avancés

Activez le mode **Avancé** pour accéder à des contrôles supplémentaires :

- **Diamètre supérieur** - Définit un diamètre différent pour le haut du cylindre afin de créer des formes coniques ou tronconiques (par défaut : identique au Diamètre)
- **Angle de départ** - Angle où le cylindre commence (par défaut : 0). À utiliser avec l'Angle final pour créer des cylindres partiels
- **Angle final** - Angle où le cylindre se termine (par défaut : 360). Définissez une valeur inférieure à 360 pour obtenir des formes en part de tarte

## Astuces

- Définissez un faible nombre de Côtés pour créer des polygones réguliers -- 6 pour des hexagones, 8 pour des octogones, etc.
- Utilisez des valeurs différentes pour le Diamètre et le Diamètre supérieur afin de créer des cônes tronqués et des formes coniques
- Définissez l'Angle de départ et l'Angle final pour créer des formes en part de tarte ou en arc
- Les cylindres constituent d'excellents outils de découpe pour créer des trous ronds avec [Soustraire](../operations/boolean/subtract.md)

## Voir aussi

- [Cône](cone.md) - Un cylindre qui se termine en pointe
- [Demi-cylindre](half-cylinder.md) - Un cylindre coupé en deux dans le sens de la longueur
- [Anneau](ring.md) - Un cylindre creux (tube)
