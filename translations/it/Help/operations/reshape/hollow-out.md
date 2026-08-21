---
title: Svuota
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Svuota

Svuota crea un guscio cavo da un oggetto solido spostando la superficie verso l'interno. Il risultato è una versione a parete sottile della forma originale.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Come si usa

1. Seleziona un oggetto solido
2. Applica l'operazione **Svuota** dal menu Rimodella
3. Imposta lo spessore di parete desiderato

## Parametri

- **Distanza** - Lo spessore della parete in millimetri (valore predefinito: 2 mm). Corrisponde allo spessore del guscio risultante.
- **N. celle** - Risoluzione dell'algoritmo di svuotamento (valore predefinito: 64). Valori più alti creano superfici interne più levigate, ma richiedono tempi di calcolo maggiori.

## Suggerimenti

- Svuota è utile per creare custodie, contenitori, vasi e parti leggere
- Uno spessore di parete di 1-2 mm è tipico per la maggior parte delle parti stampate in 3D
- Aumenta N. celle se la superficie interna appare ruvida o sfaccettata
- Lo svuotamento crea un fondo aperto: combinalo con un [Cubo](../../primitives/cube.md) se hai bisogno di una base chiusa
- Per forme complesse, il calcolo può richiedere alcuni secondi

## Correlati

- [Taglio con piano](plane-cut.md) - Taglia un oggetto a un'altezza specifica
- [Sottrai](../boolean/subtract.md) - Rimuovi manualmente il materiale
