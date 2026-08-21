---
title: Feuille de variables
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Feuille de variables

La Feuille de variables stocke les valeurs partagées d'une conception. Utilisez-la lorsque plusieurs objets doivent référencer les mêmes dimensions, quantités, étiquettes ou formules. La modification d'une valeur dans la feuille recalcule les objets dépendants : les conceptions paramétriques restent ainsi cohérentes sans avoir à modifier chaque objet un par un.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Comment ajouter une Feuille de variables

1. Ouvrez la bibliothèque et ajoutez une **Feuille de variables** à la scène.
2. Sélectionnez l'objet Feuille de variables pour afficher l'éditeur de feuille.
3. Sélectionnez une cellule, puis saisissez un **Nom** ainsi qu'une valeur ou une formule.
4. Utilisez le nom de la cellule depuis les autres champs de la conception qui acceptent les expressions.

## Modification des cellules

Chaque cellule comporte deux parties modifiables :

- **Nom** - Un nom de variable facultatif pour la cellule. Les noms ne tiennent pas compte de la casse, les espaces sont convertis en traits de soulignement et les noms en double sont automatiquement ajustés.
- **Expression** - La valeur de la cellule. Le texte brut et les nombres sont stockés directement. Les formules commencent par `=`.

Les cellules peuvent également être référencées par leur adresse, par exemple `A1` ou `B2`. Les cellules nommées sont généralement plus claires pour les paramètres de conception, car elles décrivent l'intention, comme `wall_thickness`, `outer_diameter` ou `hole_count`.

## Formules

Commencez une formule par `=` pour qu'elle soit évaluée dans la feuille :

- `=20 + 5` renvoie `25`
- `=pi * 10` renvoie `31.41592653589793`
- `=A1 * 2` référence une autre cellule par son adresse
- `=wall_thickness + 4` référence une cellule nommée

La feuille prend en charge l'arithmétique, les parenthèses, les opérateurs de comparaison, les fonctions `Math` courantes telles que `sin`, `cos`, `sqrt` et `round`, ainsi que des constantes comme `pi`, `tau` et `e`.

## Utilisation des valeurs de la feuille dans les objets

La plupart des champs numériques de MatterCAD acceptent les expressions. Pour utiliser une valeur de la feuille dans un paramètre d'objet, faites précéder la référence de `=` :

- Définissez la **Largeur** d'un cube sur `=case_width`.
- Définissez le **Nombre** d'un Réseau sur `=hole_count`.
- Définissez une valeur de **Décalage** d'un Déplacer sur `=wall_thickness * 2`.

Lorsque la feuille change, MatterCAD recalcule les objets qui en dépendent.

## Texte et fonctions utilitaires

Les cellules de la Feuille de variables peuvent contenir du texte aussi bien que des nombres. Les valeurs textuelles sont utiles pour les étiquettes générées, les numéros de pièce, les données importées et les applications de conception personnalisées.

Parmi les fonctions utilitaires pratiques :

- `concat()` ou `strcat()` - Concaténer du texte ou des valeurs.
- `substring()` - Extraire une partie d'une valeur textuelle.
- `split()` - Diviser un texte et renvoyer un élément.
- `count()` - Compter les éléments délimités dans un texte.
- `substitute()` - Remplacer du texte.
- `rand(seed)` - Générer une valeur aléatoire déterministe lorsqu'une graine est fournie.
- `importdata()` - Lire une valeur depuis une URL ou un chemin de fichier local.

## Conseils

- Préférez des noms descriptifs aux adresses de cellules pour les valeurs utilisées par d'autres objets.
- Placez les dimensions principales près du coin supérieur gauche de la feuille afin de les retrouver facilement.
- Utilisez des formules pour les valeurs dérivées, comme `inner_diameter = outer_diameter - wall_thickness * 2`.
- Évitez d'utiliser des mots réservés tels que `pi`, `e`, `true`, `false` ou des noms de fonctions comme noms de cellules.
- Si une formule ne peut pas être analysée, MatterCAD conserve la saisie d'origine sous forme de texte.

## Voir aussi

- [Expressions](expressions.md) - Utiliser des expressions dans les paramètres d'objet
- [Composants](components.md) - Créer des conceptions paramétriques réutilisables
- [Réseau](../operations/array/array.md) - Créer des motifs répétés pilotés par les valeurs de la feuille
