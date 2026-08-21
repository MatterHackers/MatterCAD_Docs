---
title: Réseau
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Réseau

Réseau crée plusieurs copies d'un objet disposées selon un motif. Sélectionnez un mode à l'aide des boutons situés en haut — **Linéaire**, **Radial** ou **Transformer** — pour changer de type de motif.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Réseau** depuis le menu Duplication
3. Choisissez un mode (Linéaire, Radial ou Transformer)
4. Ajustez les paramètres du mode choisi

## Mode : Linéaire

Le mode Linéaire place les copies le long d'une direction, avec une progression facultative de rotation et d'échelle.

**Nombre** — Nombre de copies (entier ou expression). L'objet source constitue la première copie ; les copies supplémentaires en sont décalées.

**Méthode de décalage** — Mode de calcul de l'espacement :
- **Relatif** — Le décalage est multiplié par la taille de la boîte englobante de l'objet. Un Décalage relatif de (1, 0, 0) espace les copies d'exactement une largeur d'objet le long de X.
- **Décalage** — Distance fixe en mm dans l'espace monde pour chaque copie.
- **Point final** — Définit la position de la dernière copie ; l'espacement est réparti uniformément entre les copies.

**Décalage relatif** / **Décalage** / **Point final** — Le vecteur d'espacement, selon la Méthode de décalage sélectionnée.

**Mode de rotation** — Manière dont la rotation s'accumule d'une copie à l'autre :
- **Local** — Chaque copie pivote sur place autour de son propre centre ; la direction du décalage reste alignée sur les axes du monde.
- **Composition** — La rotation s'accumule et oriente le décalage, produisant des spirales, des éventails et des hélices.

**Rotation** — Rotation par copie, en degrés, sur chaque axe.

**Échelle** — Échelle cumulative par copie sur chaque axe. Les valeurs inférieures à 1 réduisent les copies ; les valeurs supérieures à 1 les agrandissent.

**L'échelle affecte le décalage** — Lorsque cette option est activée, l'espacement entre les copies évolue également à chaque étape. Utilisez-la pour les spirales resserrées et les progressions géométriques (coquilles de nautile, courbes empilées en coquille de clou).

## Mode : Radial

Le mode Radial répartit les copies uniformément autour d'un axe central, à un rayon fixe.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Méthode de comptage** — Manière dont le nombre de copies est déterminé :
- **Nombre** — Nombre de copies explicite.
- **Distance** — Écart angulaire entre les copies en degrés ; le nombre est calculé pour remplir le balayage.

**Nombre** / **Distance angulaire** — Nombre de copies (mode Nombre) ou espacement angulaire en degrés (mode Distance). Prend en charge les expressions.

**Axe central** — L'axe autour duquel effectuer la rotation (par défaut : Z).

**Segment de cercle** — Indique si les copies couvrent un cercle complet de 360° (**Complet**) ou un arc partiel (**Arc**).

**Rayon** — Distance entre l'axe central et chaque copie.

**Angle de balayage** — Degrés d'arc à remplir (affiché lorsque Segment de cercle est réglé sur Arc). Prend en charge les expressions.

**Aligner la rotation** — Fait pivoter chaque copie de sorte que son axe avant pointe vers l'extérieur depuis le centre.

**Axe avant** — Axe de la copie considéré comme « avant » pour l'alignement (affiché lorsque Aligner la rotation est activé).

## Mode : Transformer

Le mode Transformer incrémente les copies à l'aide d'une transformation manuelle ou en suivant la transformation d'un autre objet.

**Nombre** — Nombre de copies (entier ou expression).

**Référence de transformation** — Provenance de la transformation appliquée à chaque étape :
- **Entrée** — Vous spécifiez directement la translation, la rotation et l'échelle.
- **Objet** — La transformation est lue depuis un objet frère désigné par son nom.

**Translation** — Décalage par étape dans l'espace monde, en mm (affiché lorsque la Référence est Entrée).

**Rotation** — Rotation par étape, en degrés pour chaque axe (affiché lorsque la Référence est Entrée).

**Échelle** / **Axes de mise à l'échelle** — Échelle uniforme et par axe appliquée à chaque étape (affiché lorsque la Référence est Entrée).

**Nom de la transformation** — Nom de l'objet frère dont la transformation sert d'incrément à chaque étape (affiché lorsque la Référence est Objet).

**Espace relatif** — Lorsque cette option est activée, la transformation de chaque copie se compose dans le repère local de la copie précédente ; lorsqu'elle est désactivée, chaque étape est appliquée dans l'espace monde (affiché lorsque la Référence est Objet).

## Rendre aléatoire

Activez **Rendre aléatoire** pour ajouter des variations à toutes les copies.

- **Décalage aléatoire** — Décalage de position aléatoire maximal par axe, en mm.
- **Rotation aléatoire** — Rotation aléatoire maximale par axe, en degrés.
- **Axes d'échelle aléatoire** — Variation d'échelle aléatoire maximale par axe.
- **Exclure le premier** — Conserve la première copie à sa position calculée exacte (par défaut : activé).
- **Exclure le dernier** — Conserve la dernière copie à sa position calculée exacte.
- **Graine aléatoire** — Modifiez cette valeur pour obtenir une disposition aléatoire différente. Prend en charge les expressions.

## Fusionner

- **Créer un maillage unique** — Combine toutes les copies en un seul objet maillé fusionné.
- **Fusionner les sommets** — Soude les sommets situés en deçà du seuil de distance de fusion (affiché lorsque Créer un maillage unique est activé).
- **Distance** — Seuil de fusion en mm (affiché lorsque Fusionner les sommets est activé).

## Conseils

- Utilisez des expressions pour Nombre, Rotation ou Point final afin de créer des motifs paramétriques
- Pour les motifs circulaires, utilisez le mode Radial — réglez le Rayon pour contrôler la taille du cercle et activez Aligner la rotation si les copies doivent être orientées vers l'extérieur
- La rotation en Composition dans le mode Linéaire crée des spirales et des éventails sans avoir à calculer manuellement les décalages angulaires
- L'échelle affecte le décalage produit naturellement des dispositions en coquille de nautile et en progression géométrique
- Combinez Réseau avec [Sélectionner l'enfant](select-child.md) pour créer des motifs où chaque copie affiche une variante différente

## Rubriques associées

- [Aligner](../placement/align.md) - Positionner des objets les uns par rapport aux autres
- [Sélectionner l'enfant](select-child.md) - Choisir une copie précise d'un réseau par index ou par nom
