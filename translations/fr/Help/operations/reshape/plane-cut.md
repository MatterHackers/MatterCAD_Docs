---
title: Coupe par plan
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Coupe par plan

Coupe par plan tranche un objet à une hauteur donnée à l'aide d'un plan horizontal, en ne conservant que la portion située sous la coupe. La surface de coupe est fermée par une face plane.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Coupe par plan** depuis le menu Remodeler
3. Définissez la hauteur de coupe

## Paramètres

- **Hauteur de coupe** - La hauteur Z à laquelle trancher l'objet (valeur par défaut : 10 mm, plage : 1-200 mm)

## Conseils

- Utilisez Coupe par plan pour aplanir le sommet d'un modèle à une hauteur précise
- Pratique pour rogner des modèles importés ou créer des bases planes
- Pour couper avec une forme non planaire, utilisez plutôt [Soustraire](../boolean/subtract.md) avec un autre objet
- Pour couper avec un plan incliné, faites d'abord pivoter l'objet, appliquez Coupe par plan, puis remettez-le dans son orientation initiale

## Voir aussi

- [Intersecter](../boolean/intersect.md) - Ne conserver que la zone de chevauchement des objets
- [Soustraire](../boolean/subtract.md) - Couper avec n'importe quelle forme, pas seulement un plan
- [Évider](hollow-out.md) - Créer une coque creuse
