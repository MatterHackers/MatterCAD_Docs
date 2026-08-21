---
title: Torsion
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Torsion

La torsion fait pivoter le haut d'un objet par rapport à son bas, créant un effet de spirale ou de vrille sur toute la hauteur. Par défaut, la rotation progresse uniformément du bas vers le haut ; sous **Avancé**, vous pouvez dessiner l'endroit de la hauteur où la rotation se produit réellement.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Utilisation

1. Sélectionnez un objet
2. Appliquez l'opération **Torsion** depuis le menu Remodeler
3. Définissez l'angle de torsion et ajustez le tranchage pour obtenir un résultat lisse
4. Activez **Avancé** si vous souhaitez dessiner la répartition de la torsion le long de la pièce

## Le Profil de torsion

Sous Avancé, la courbe **Profil de torsion** détermine où la torsion se produit. La quantité totale de torsion reste définie par la commande Angle (ou Distance de rotation) — la courbe ne fait que la répartir :

- **L'axe vertical de la courbe** correspond à la hauteur sur la pièce en pourcentage — 0 en bas, 100 en haut. Une ligne de repère traversant l'éditeur marque 100 pour cent et porte l'étiquette de la hauteur réelle de la pièce en mm.
- **L'axe horizontal de la courbe** correspond au pourcentage de la torsion totale atteint à cette hauteur — 0 pour aucune, 100 pour la totalité.

Une nouvelle Torsion commence par une diagonale droite allant de 0 à 100, ce qui correspond à la torsion parfaitement uniforme que vous obtenez sans utiliser Avancé.

Un segment plat dans la courbe correspond à une bande de la pièce qui ne subit aucune torsion. Là où la courbe ne couvre pas toute la hauteur, son extrémité la plus proche est maintenue : une courbe tracée uniquement entre 40 et 60 pour cent laisse donc la pièce rigide en dessous et au-dessus — c'est ainsi que l'on démarre et arrête une torsion à mi-hauteur.

Un segment qui redescend en montant produit un déroulement : cette bande de la pièce tourne dans l'autre sens, revenant vers sa position de départ. Tracer le profil au-delà de 100 puis le faire redescendre permet de dépasser la valeur totale avant d'y revenir.

## Paramètres

- **Type de rotation** — Choisissez entre :
  - **Angle** — Spécifiez l'angle de torsion total en degrés (3-360)
  - **Distance** — Spécifiez la torsion sous forme de distance le long de la circonférence
- **Tranches** — Nombre de coupes horizontales ajoutées pour une torsion lisse, réparties uniformément sur la hauteur de la pièce. Plus de tranches = torsion plus lisse
- **Nombre minimal de côtés** — Le nombre minimal de côtés que la pièce doit présenter autour de l'axe de torsion. Une forme grossière telle qu'un cube ne possède aucune géométrie sur son périmètre pour porter la rotation : ses faces planes se facettent au lieu de se courber. Ce paramètre ajoute des coupes verticales à travers l'axe de torsion afin que ces faces puissent suivre la torsion. La valeur 0 (par défaut) laisse la pièce inchangée
- **Torsion à droite** — Sens de la torsion : à droite (sens horaire) ou à gauche (sens antihoraire)
- **Rayon préféré** — Lecture seule : le rayon indiqué par la pièce elle-même, ou celui impliqué par sa forme, autour duquel une distance de torsion est mesurée (mode Distance uniquement)
- **Modifier le rayon** — Désactive le rayon indiqué afin que vous puissiez définir le vôtre (mode Distance uniquement, et seulement lorsque la pièce en indique un)
- **Remplacer le rayon** — Rayon personnalisé pour le calcul de la torsion (mode Distance uniquement)

### Paramètres avancés

- **Profil de torsion** — L'éditeur de courbe décrit ci-dessus : le pourcentage de la torsion totale atteint à chaque hauteur, exprimée en pourcentage
- **Décalage de rotation** — Déplace le centre autour duquel la pièce pivote, à l'écart du milieu de la pièce

## Astuces

- Des valeurs de Tranches plus élevées produisent des résultats plus lisses mais génèrent davantage de géométrie
- Si un cube tordu ou une autre forme à faces planes paraît facetté plutôt que courbé, augmentez le Nombre minimal de côtés
- Tracez le profil plat en bas puis ascendant ensuite pour conserver une base droite sous une colonne torsadée
- Une torsion de 90 degrés sur une colonne carrée crée un élégant effet architectural
- Tracez deux segments plats reliés par une courte montée pour tordre le milieu de la pièce tout en laissant les deux extrémités rigides

## Voir aussi

- [Courbe](curve.md) — Plier un objet en arc de cercle
- [Pincement](pinch.md) — Comprimer vers le centre
- [Pincement radial](radial-pinch.md) — Façonner le profil avec une courbe de la même manière
