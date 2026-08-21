---
title: Groupement
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Groupement

Le groupement combine plusieurs objets en une seule unité qui peut être déplacée, copiée et manipulée comme un objet unique. Contrairement à [Combiner](../operations/boolean/combine.md), le groupement ne fusionne pas la géométrie : chaque objet reste distinct à l'intérieur du groupe.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Utilisation

### Grouper des objets

1. Sélectionnez au moins deux objets (Maj-clic ou Ctrl-clic pour une sélection multiple)
2. Cliquez sur le bouton **Grouper** dans la barre d'outils
3. Les objets sont désormais groupés : ils se déplacent ensemble comme une seule unité

### Dissocier des objets

1. Sélectionnez un groupe
2. Cliquez sur le bouton **Dissocier** dans la barre d'outils
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Les objets individuels sont rétablis comme éléments distincts

La dissociation tente également de séparer plusieurs corps au sein d'un même fichier STL importé, le cas échéant.

## Grouper ou Combiner

| Caractéristique | Grouper | Combiner |
|---------|-------|---------|
| Les objets restent distincts | Oui | Non |
| Dissociation possible ultérieurement | Oui | Non (destructif) |
| Fusionne les géométries superposées | Non | Oui |
| Les objets peuvent avoir des couleurs différentes | Oui | Couleurs conservées par face |
| Cas d'usage | Organisation et déplacement | Création de formes solides uniques |

## Astuces

- Les groupes peuvent être imbriqués : vous pouvez grouper des objets qui appartiennent déjà à des groupes
- Sélectionnez un groupe et consultez l'arborescence de conception pour voir et sélectionner les objets individuels qu'il contient
- Le groupement est non destructif et peut toujours être annulé avec Dissocier

## Voir aussi

- [Combiner](../operations/boolean/combine.md) - Fusionner des objets en un solide unique au lieu de les grouper
- [Sélection](selection.md) - Comment sélectionner plusieurs objets en vue de les grouper
- [Composants](components.md) - Créer des groupes paramétrés réutilisables
