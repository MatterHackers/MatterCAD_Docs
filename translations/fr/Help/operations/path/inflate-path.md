---
title: Dilater le tracé
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Dilater le tracé

Dilater le tracé étend un chemin 2D vers l'extérieur, agrandissant la forme tout en conservant son allure générale. Cela revient à appliquer un décalage uniforme à toutes les arêtes.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Utilisation

1. Sélectionnez un chemin 2D
2. Appliquez **Dilater le tracé** depuis le menu des opérations de Chemin
3. Ajustez la valeur de dilatation

## Dilater une ligne ouverte

Dilater est la façon de transformer une ligne en forme. Décochez **Fermé** sur un [Chemin personnalisé](../../2d-paths/custom-path.md) pour dessiner une ligne ouverte, puis dilatez-la : le résultat est un ruban plein, aussi large de chaque côté de la ligne que la valeur définie. À partir de là, il s'extrude comme n'importe quel autre chemin.

**Style** détermine la façon dont les deux extrémités de la ligne sont terminées, ainsi que la façon dont ses angles sont raccordés :

- **Plat** arrête le ruban à l'équerre à chaque point d'extrémité
- **Arrondir** ajoute un demi-cercle au-delà de chaque point d'extrémité
- **Vif** ajoute un carré au-delà de chaque point d'extrémité

Une ligne ouverte n'a pas d'intérieur dans lequel se rétracter : une valeur nulle ou négative ne laisserait donc rien du tout. Lorsque le chemin est *entièrement* ouvert, Dilater ramène la valeur à un petit nombre positif et réinscrit cette valeur ajustée dans le champ afin que vous puissiez voir ce qui s'est passé.

Un chemin qui mélange contours ouverts et fermés n'est pas ajusté : les contours fermés se rétractent normalement et les contours ouverts disparaissent simplement. Les chemins fermés continuent de se rétracter sur les valeurs négatives, exactement comme auparavant.

## Astuces

- Utilisez des valeurs négatives pour rétracter le chemin vers l'intérieur au lieu de l'étendre
- Dilater est utile pour créer des décalages de tolérance autour des formes
- Combiner avec [Chemin de contour](outline-path.md) pour créer des bordures de largeurs précises

## Voir aussi

- [Chemin de contour](outline-path.md) - Créer un contour à partir d'un chemin
- [Tracé de bordure](border-path.md) - Ajouter un décalage de bordure
- [Lisser le chemin](smooth-path.md) - Arrondir les angles d'un chemin
