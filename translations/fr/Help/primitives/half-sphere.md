---
title: Demi-sphère
articleKey: HalfSphereObject3D
parent: "Primitives"
nav_order: 7
source_hash: 4f82c152ab27e32e36e758c83f9135f1c6bb2096
source_lang: en
---
# Demi-sphère

L'hémisphère supérieur d'une sphère -- une forme de dôme. Utile pour créer des sommets bombés, des formes de lentille et des couvercles arrondis.

<!--  Screenshot of a Half Sphere primitive on the workspace -->
![20260318 183343 paste 20260318 183343](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183343-paste-20260318-183343.jpg)


## Paramètres

- **Diamètre** - La largeur à la base du dôme (par défaut : 20mm)
- **Côtés en longitude** - Nombre de segments autour du périmètre (par défaut : 40)
- **Côtés en latitude** - Nombre de segments de la base au sommet (par défaut : 10). Plus il y en a, plus le dôme est lisse

## Astuces

- Combinez deux demi-sphères avec un cylindre pour obtenir une forme de capsule
- Placez-la sur un cylindre pour créer un couvercle bombé ou un bouton
- Utilisez-la avec [Soustraire](../operations/boolean/subtract.md) pour créer des cavités en forme de dôme

## Voir aussi

- [Sphère](sphere.md) - Une boule complète
- [Demi-cylindre](half-cylinder.md) - Un cylindre coupé en deux
