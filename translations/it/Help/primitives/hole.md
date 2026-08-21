---
title: Foro
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Foro

Un oggetto a forma di cubo preconfigurato per funzionare come strumento di sottrazione booleana. Quando usi [Combina](../operations/boolean/combine.md), gli oggetti Foro vengono automaticamente sottratti dalle altre forme invece di essere aggiunti ad esse.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Come funziona

La primitiva Foro funziona come un [Cubo](cube.md), ma ha il tipo di output impostato su "Foro". Quando combini oggetti che includono un Foro, il volume del Foro viene rimosso dal risultato.

## Parametri

Gli stessi del [Cubo](cube.md):

- **Larghezza** - Dimensione lungo l'asse X
- **Profondità** - Dimensione lungo l'asse Y
- **Altezza** - Dimensione lungo l'asse Z

## Suggerimenti

- Posiziona il Foro in modo che si sovrapponga all'oggetto che vuoi tagliare
- Fai in modo che il Foro attraversi completamente l'oggetto di destinazione se desideri un foro passante
- Puoi ottenere lo stesso effetto usando forme normali con [Sottrai](../operations/boolean/subtract.md), ma i Fori sono comodi perché funzionano automaticamente con [Combina](../operations/boolean/combine.md)
- Per fori tondi, usa invece un [Cilindro](cylinder.md) con Sottrai

## Correlati

- [Cubo](cube.md) - La stessa forma senza il comportamento del foro
- [Combina](../operations/boolean/combine.md) - Unisce le forme e sottrae automaticamente i Fori
- [Sottrai](../operations/boolean/subtract.md) - Sottrai manualmente qualsiasi forma da un'altra
