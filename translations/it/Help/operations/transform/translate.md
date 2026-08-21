---
title: Trasla
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# Trasla

Trasla sposta un oggetto di una distanza specifica lungo gli assi X, Y e/o Z. A differenza del trascinamento di un oggetto con il mouse, Trasla consente di inserire valori di scostamento esatti.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Trasla** dal menu Trasforma
3. Inserisci i valori di scostamento desiderati per X, Y e Z nel pannello Proprietà

## Parametri

- **X, Y, Z** (Traslazione) - La distanza di cui spostare l'oggetto lungo ciascun asse, in millimetri. Supporta le [espressioni](../../workspace/expressions.md) per i valori calcolati.

## Suggerimenti

- Usa Trasla quando hai bisogno di un posizionamento preciso e ripetibile che potrai modificare in seguito
- I valori di traslazione sono relativi alla posizione attuale dell'oggetto: inserendo 10 per X, l'oggetto si sposta di 10 mm verso destra rispetto a dove si trova
- Per un riposizionamento rapido, puoi anche trascinare gli oggetti direttamente nella viewport. Vedi [Modifica degli oggetti](../../getting-started/editing-objects.md)

## Correlati

- [Ruota](rotate.md) - Ruota un oggetto di un angolo specifico
- [Scala](scale.md) - Ridimensiona un oggetto con precisione
- [Allinea](../placement/align.md) - Posiziona gli oggetti l'uno rispetto all'altro
