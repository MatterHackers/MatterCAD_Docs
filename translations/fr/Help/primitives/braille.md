---
title: Braille
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braille

Générez du texte en braille imprimable en 3D à partir de texte anglais standard. L'outil Braille prend en charge l'encodage braille de grade 1 (lettre par lettre) et de grade 2 (abrégé).

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Utilisation

1. **Ajouter** une primitive **Braille** depuis le panneau Primitives
2. Saisissez votre texte dans le champ **Texte à encoder**
3. L'outil le convertit automatiquement dans le motif de points braille correct

## Paramètres

- **Texte à encoder** - Le texte anglais à convertir en braille
- **Échelle** - Ajuste la taille globale du résultat en braille
- **Hauteur** - La hauteur des points braille en relief

## Conseils

- Le braille de grade 2 utilise des contractions et des abréviations pour les mots et les combinaisons de lettres courants, ce qui le rend plus compact
- Les dimensions standard des cellules braille sont utilisées afin de garantir la lisibilité du résultat
- **Combiner** avec une base plate de type [Cube](cube.md) pour créer une étiquette ou un panneau en braille complet
- Pour les cartes en braille avec base intégrée, voir [Carte en braille](braille-card.md)

## Voir aussi

- [Carte en braille](braille-card.md) - Braille avec une base de carte intégrée
- [Texte](text.md) - Texte 3D standard
