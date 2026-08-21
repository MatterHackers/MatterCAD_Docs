---
title: Aligner
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Aligner

Aligner positionne précisément plusieurs objets par rapport à un objet d'ancrage. Utilisez cette opération pour aligner des arêtes, centrer des pièces les unes sur les autres, placer un objet au-dessus d'un autre ou créer des empilements régulièrement espacés.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Utilisation

1. Sélectionnez au moins deux objets.
2. Appliquez l'opération **Aligner** depuis le menu **Placement**.
3. Choisissez l'objet d'**Ancrage**. L'ancrage reste en place et les autres objets se déplacent.
4. Définissez l'alignement des axes X, Y et Z indépendamment.
5. Utilisez **Appliquer** lorsque vous souhaitez figer les positions alignées dans l'arborescence des objets.

## Paramètres

### Ancrage

La liste **Ancrage** sélectionne l'objet enfant utilisé comme référence. L'ancrage ne bouge pas. Tous les autres enfants de l'opération Aligner sont repositionnés par rapport à l'ancrage, sauf si un axe utilise le mode **Empilé**.

### Commandes d'axe

Chaque axe dispose de ses propres commandes. Vous pouvez aligner sur un axe, deux axes ou les trois. Les arêtes minimale et maximale sont nommées selon l'axe :

- **Axe X** - Min correspond à la gauche, Max à la droite.
- **Axe Y** - Min correspond à l'avant, Max à l'arrière.
- **Axe Z** - Min correspond au bas, Max au haut.

Pour chaque axe :

- **Aligner** - Choisit le point de référence de l'ancrage pour cet axe. Utilisez **Aucun** pour laisser les positions inchangées sur cet axe.
- **Mode** - Détermine la façon dont l'alignement sélectionné est appliqué :
  - **Simple** - Fait correspondre l'arête, le centre ou l'origine de chaque objet déplacé à celui de l'ancrage. Aucun décalage n'est utilisé.
  - **Décalage** - Choisissez quelle partie de l'objet déplacé doit se poser sur la référence de l'ancrage, puis ajoutez un espacement avec **Décalage**.
  - **Empilé** - Place les objets les uns à la suite des autres le long de cet axe, en utilisant **Décalage** comme espace entre eux.
- **Sous-alignement** - Disponible en mode **Décalage**. Choisit la partie de l'objet déplacé à placer sur la référence de l'ancrage. Si **Sous-alignement** est réglé sur **Aucun**, Aligner utilise la même arête, le même centre ou la même origine que ceux sélectionnés par **Aligner**.
- **Décalage** - Disponible dans les modes **Décalage** et **Empilé**. Ajoute une distance le long de cet axe et prend en charge les [expressions](../../workspace/expressions.md).

## Modes d'alignement

### Simple

Utilisez **Simple** pour faire correspondre des positions de même nature. Par exemple, **Alignement X : Centre** déplace chaque objet non ancré de sorte que son centre X corresponde au centre X de l'ancrage. **Alignement Z : Min** déplace chaque objet non ancré de sorte que son dessous se situe à la hauteur du dessous de l'ancrage.

### Décalage

Utilisez **Décalage** lorsque la partie de l'objet déplacé doit être différente de la référence de l'ancrage. Par exemple, pour placer un objet au-dessus de l'ancrage :

1. Réglez **Alignement Z** sur **Max** (haut).
2. Réglez **Mode Z** sur **Décalage**.
3. Réglez **Sous-alignement Z** sur **Dessous**.
4. Réglez **Décalage Z** sur l'espace souhaité, ou laissez-le à `0` pour un contact direct.

Cela place le dessous de l'objet déplacé sur le dessus de l'ancrage, avec un espacement facultatif.

### Empilé

Utilisez **Empilé** pour chaîner plusieurs objets le long d'un axe. Les objets sont traités par nom, puis par identifiant interne : nommer clairement les objets donne donc un ordre d'empilement prévisible.

En mode **Empilé**, chaque objet déplacé est placé contre la référence précédente sur cet axe :

- L'alignement **Min** empile vers la direction positive, par exemple de gauche à droite sur X ou de bas en haut sur Z.
- L'alignement **Max** empile vers la direction négative, par exemple de droite à gauche sur X ou de haut en bas sur Z.
- Les alignements **Centre** et **Origine** utilisent le décalage entre le centre ou l'origine de chaque objet.

Utilisez **Décalage** en mode **Empilé** pour définir l'espace entre les objets.

## Exemples

- **Centrer des objets sur l'emprise du plateau** - Choisissez l'objet qui doit rester fixe comme **Ancrage**, puis réglez **Alignement X** et **Alignement Y** sur **Centre**.
- **Placer un objet au-dessus d'un autre** - Réglez **Alignement Z** sur **Max** (haut), **Mode Z** sur **Décalage** et **Sous-alignement Z** sur **Dessous**.
- **Ajouter un espace précis depuis une arête** - Utilisez le mode **Décalage**, choisissez l'arête de l'objet déplacé avec **Sous-alignement**, puis réglez **Décalage** sur l'espacement voulu.
- **Aligner plusieurs objets bout à bout** - Réglez **Alignement X** sur **Min** (gauche), **Mode X** sur **Empilé**, et utilisez **Décalage X** pour l'espace.
- **Construire un empilement vertical** - Réglez **Alignement Z** sur **Min** (bas), **Mode Z** sur **Empilé**, et utilisez **Décalage Z** pour l'espace entre les objets.

## Conseils

- L'objet d'ancrage reste en place ; les autres objets se déplacent pour s'aligner sur lui.
- Vous pouvez utiliser des modes différents sur des axes différents, par exemple **Empilé** sur X tout en utilisant **Centre** et **Simple** sur Y.
- Utilisez les noms des objets pour contrôler l'ordre **Empilé** lorsque plusieurs objets sont alignés en même temps.
- Aligner est non destructif tant que l'opération n'est pas appliquée. Vous pouvez modifier les réglages à tout moment pour réaligner les enfants.
- Utilisez **Origine** lorsque vous devez aligner les origines de modélisation plutôt que les arêtes des boîtes englobantes.

## Voir aussi

- [Ajuster aux limites](fit-to-bounds.md) - Mettre un objet à l'échelle pour l'adapter à des dimensions précises
- [Déplacer](../transform/translate.md) - Déplacer d'une distance précise
- [Groupement](../../workspace/grouping.md) - Grouper des objets alignés pour les conserver ensemble
