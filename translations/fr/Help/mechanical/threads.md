---
title: Filets
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Filets

Créez des filetages de vis avec un diamètre, un pas et un profil de filet configurables. Les filets peuvent servir de boulons/vis autonomes ou être soustraits d'autres objets pour créer des trous filetés.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Utilisation

1. Ajoutez **Filets** depuis les outils Mécanique ou le panneau Primitives
2. Définissez le diamètre, le pas et le nombre de rotations
3. Activez éventuellement « Utiliser comme trou » pour créer des trous filetés

## Paramètres

### Usage

- **Utiliser comme trou** - Lorsque cette option est activée, les filets sont dimensionnés avec une tolérance supplémentaire afin de servir de trou soustrait (par défaut : désactivé)
- **Tolérance** - Jeu supplémentaire pour l'ajustement lors d'une utilisation comme trou (par défaut : 0,2 mm, visible lorsque Utiliser comme trou est activé)

### Attributs

- **Diamètre** - Le diamètre extérieur de la section filetée (par défaut : 10 mm)
- **Pas** - Distance entre chaque tour de filet (par défaut : 2 mm). Un pas plus petit = des filets plus fins
- **Échelle du filetage** - Largeur des filets exprimée en proportion du pas (par défaut : 1.0, plage : 0.1-1.0)
- **Rotations** - Nombre de tours complets de filet (par défaut : 10)

### Géométrie

- **Côtés** - Nombre de segments sur le pourtour (par défaut : 40). Plus il y en a, plus le résultat est lisse

### Pointes (extrémités des filets)

- **Échelle de pointe** - Degré d'effilement des extrémités du filet (par défaut : 0, plage : 0-1). Réglez une valeur supérieure à 0 pour créer une amorce effilée aux extrémités
- **Angle de pointe** - L'angle sur lequel les pointes sont effilées (par défaut : 90 degrés)

## Conseils

- Pour créer un trou fileté : activez « Utiliser comme trou », positionnez les filets, puis appliquez [Soustraire](../operations/boolean/subtract.md) à votre objet
- Ajoutez une Tolérance lors d'une utilisation comme trou afin que les pièces imprimées s'assemblent correctement
- Pas de filetage métrique standard : M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Utilisez l'Échelle de pointe pour créer une amorce facilitant l'engagement du filetage

## Voir aussi

- [Engrenages](gears.md) - Créez des formes d'engrenage mécanique
- [Cylindre](../primitives/cylinder.md) - Une simple colonne ronde (sans filets)
- [Soustraire](../operations/boolean/subtract.md) - Découpez des filets dans d'autres objets pour créer des trous
