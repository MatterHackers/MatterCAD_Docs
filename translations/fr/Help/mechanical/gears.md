---
title: Engrenages
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Engrenages

Créez des engrenages 3D dont la géométrie de denture est entièrement paramétrable. MatterCAD génère de véritables profils de dents en développante qui s'engrènent correctement avec d'autres engrenages de même module et de même angle de pression.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Utilisation

1. Ajoutez un **Engrenage** depuis les outils Mécanique ou le panneau Primitives
2. Définissez le nombre de dents et les autres paramètres
3. Le profil de l'engrenage est généré automatiquement

## Paramètres

### Fonctions

- **Type d'engrenage** - Engrenage Externe ou Crémaillère (barre droite dentée)
- **Hauteur** - Épaisseur de l'engrenage (hauteur d'extrusion)
- **Nombre de dents** - Nombre de dents réparties sur l'engrenage (par défaut : 30, plage : 4-60)
- **Pas circulaire** - Distance en arc entre les dents le long du cercle primitif (plage : 3-30). Cette valeur détermine la taille globale.
- **Diamètre du trou central** - Diamètre du trou d'arbre central (par défaut : 4 mm, mettre 0 pour aucun trou). Engrenages externes uniquement.
- **Largeur du bord extérieur** - Largeur du bord situé à l'extérieur des dents internes
- **Nombre de dents du pignon intérieur** - Nombre de dents de l'engrenage interne conjugué

### Avancé

- **Angle de pression** - Angle de la surface de contact des dents (valeurs courantes : 14,5, 20 ou 25 degrés). Tous les engrenages qui s'engrènent doivent utiliser le même angle de pression.
- **Jeu** - Écart minimal entre le sommet de la dent et le creux de la dent conjuguée
- **Jeu mécanique** - Écart minimal entre les dents en prise afin d'éviter tout coincement

### Données de l'engrenage (lecture seule)

- **Rayon primitif** - Rayon auquel les engrenages s'engrènent entre eux
- **Diamètre extérieur** - Diamètre total mesuré au sommet des dents

## Astuces

- Deux engrenages s'engrènent correctement lorsqu'ils ont le même Pas circulaire et le même Angle de pression
- Utilisez les valeurs de Rayon primitif pour espacer correctement les engrenages en prise -- la distance entre les centres des engrenages doit être égale à la somme de leurs rayons primitifs
- Ajoutez du Jeu mécanique pour les engrenages imprimés en 3D afin de tenir compte des tolérances d'impression
- Pour les profils d'engrenage 2D (à utiliser avec Extruder), voir [Engrenage 2D](gear-2d.md)

## Voir aussi

- [Engrenage 2D](gear-2d.md) - Tracé d'engrenage 2D pour les opérations sur tracés
- [Filets](threads.md) - Créer des fonctions filetées
