---
title: Sélectionner des trajectoires
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Sélectionner des trajectoires

Sélectionner des trajectoires filtre les sous-chemins conservés dans un objet chemin complexe. C'est particulièrement utile lorsque l'on travaille avec des polices décoratives ou en plusieurs parties, où l'on a besoin des formes extérieures des lettres et des découpes intérieures sous forme de pièces distinctes — par exemple pour les imprimer en 3D dans deux couleurs différentes.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Fonctionnement de la profondeur de chemin

Lorsqu'un objet chemin contient des formes avec des zones fermées (comme l'intérieur de la lettre « O » ou le creux d'une volute décorative), ces zones fermées sont des **trous** à la profondeur 1. Le contour extérieur de chaque lettre ou forme se trouve à la **profondeur 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Préréglages de filtre

### Tout
Inclut tous les chemins sans modification. C'est la valeur par défaut, équivalente à ne pas appliquer Sélectionner des trajectoires du tout.

### Contours extérieurs uniquement
Ne conserve que le contour extérieur de chaque forme (profondeur == 0). Utilisez ce préréglage pour n'obtenir que les silhouettes des lettres d'une police décorative, sans les zones découpées intérieures.

### Trous uniquement
Ne conserve que les trous fermés (profondeur > 0). Utilisez ce préréglage pour n'obtenir que les zones découpées intérieures des lettres et des formes.

### Par index de groupe
Ne conserve que les chemins appartenant à une seule forme disjointe. Le groupe 0 est la première forme, le groupe 1 la deuxième, et ainsi de suite. Utilisez ce préréglage pour isoler un seul caractère d'un mot.

### Personnalisé
Écrivez une expression évaluée pour chaque chemin. Le chemin est **inclus** lorsque l'expression est non nulle et **exclu** lorsqu'elle vaut zéro.

Les expressions doivent commencer par `=` pour activer la substitution de variables. Sans `=`, la valeur est traitée comme un simple nombre (par exemple, `1` inclut toujours, `0` exclut toujours).

## Exemples d'expressions personnalisées

| Expression | Effet |
|------------|--------|
| `=PathDepth==0` | Contours extérieurs uniquement (identique à Contours extérieurs uniquement) |
| `=PathDepth>0` | Trous uniquement (identique à Trous uniquement) |
| `=GroupIndex==0` | Première forme disjointe uniquement |
| `=PathArea>100` | Formes dont l'aire dépasse 100 mm² |
| `=PathLength>50` | Formes dont le périmètre dépasse 50 mm |

## Variables des expressions personnalisées

| Variable | Signification |
|----------|---------|
| `PathDepth` | 0 = contour extérieur ; 1 et plus = trou ou forme imbriquée |
| `GroupIndex` | Index de la forme disjointe (0, 1, 2…) |
| `GroupOuterArea` | Aire du chemin extérieur de ce groupe |
| `GroupOuterLength` | Périmètre du chemin extérieur de ce groupe |
| `ChildCount` | Nombre de trous à l'intérieur du chemin extérieur de ce groupe |
| `PathIndex` | Index séquentiel de ce chemin au sein de son groupe |
| `PathArea` | Aire de ce chemin individuel |
| `PathLength` | Périmètre de ce chemin individuel |

## Exemple : impression multicolore d'une police de Noël

Un usage courant de Sélectionner des trajectoires est l'impression de textes décoratifs dont les lettres comportent des découpes intérieures. Pour imprimer les lettres extérieures dans une couleur et les découpes intérieures dans une seconde couleur :

1. Ajoutez un objet **Texte** et réglez-le sur **sortie 2D**
2. Appliquez **Sélectionner des trajectoires** → réglez le préréglage sur **Contours extérieurs uniquement**
3. Appliquez **Extrusion linéaire** pour lui donner de la hauteur → attribuez la couleur de votre premier filament
4. Revenez à l'objet texte d'origine
5. Appliquez une seconde fois **Sélectionner des trajectoires** → réglez le préréglage sur **Trous uniquement**
6. Appliquez **Extrusion linéaire** avec la même hauteur → attribuez la couleur de votre second filament
7. Positionnez un objet extrudé sur l'autre — les deux couleurs s'alignent parfaitement

## Voir aussi

- [Extrusion linéaire](linear-extrude.md) — Donnez de la hauteur aux chemins filtrés pour créer un objet 3D
- [Révolution](revolve.md) — Faites tourner les chemins filtrés autour d'un axe
- [Objet SVG](../../primitives/svg-object.md) — Importez des chemins vectoriels pouvant contenir plusieurs sous-chemins
- [Texte](../../primitives/text.md) — Les objets texte en mode 2D produisent une sortie à chemins multiples
