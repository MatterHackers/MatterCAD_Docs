---
title: Tore
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Tore

Un anneau en forme de beignet offrant un contrôle indépendant de la taille globale et de l'épaisseur de la section de l'anneau.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Paramètres

- **Diamètre extérieur** - La largeur totale du tore (par défaut : 20mm)
- **Diamètre intérieur** - Le diamètre du trou central (par défaut : 10mm)
- **Côtés** - Nombre de segments autour de l'anneau principal (par défaut : 40)

### Paramètres avancés

Activez le mode **Avancé** pour accéder à des contrôles supplémentaires :

- **Angle de départ** - Angle auquel le tore commence (par défaut : 0)
- **Angle final** - Angle auquel le tore se termine (par défaut : 360). Définissez une valeur inférieure à 360 pour obtenir un anneau ouvert ou un arc
- **Côtés de l'anneau** - Nombre de segments autour de la section de l'anneau (par défaut : 15). Plus il y en a, plus le profil du tube est lisse
- **Angle de phase de l'anneau** - Fait pivoter le profil de la section (par défaut : 0)

## Conseils

- L'épaisseur du tube de l'anneau est déterminée par la différence entre le Diamètre extérieur et le Diamètre intérieur
- Utilisez l'Angle de départ et l'Angle final pour créer des segments d'anneau ouverts, des arcs ou des formes en C
- Utile pour créer des joints toriques, des poignées, des anneaux décoratifs et des coudes de tuyauterie

## Voir aussi

- [Anneau](ring.md) - Un cylindre creux à parois droites (tube)
- [Sphère](sphere.md) - Une boule pleine
- [Demi-sphère](half-sphere.md) - Une forme de dôme
