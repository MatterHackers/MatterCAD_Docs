---
title: Percorso personalizzato
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Percorso personalizzato

Disegna un percorso 2D personalizzato con punti di controllo. Questo ti offre completa libertà di creare qualsiasi forma 2D, che può poi essere estrusa o fatta ruotare per ottenere un oggetto 3D.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Come si usa

1. Aggiungi un **Percorso personalizzato** dalla libreria dei percorsi 2D
2. Modifica i punti di controllo per definire la tua forma
3. Applica [Estrusione lineare](../operations/path/linear-extrude.md) o altre operazioni sui percorsi per creare un oggetto 3D

## Percorsi aperti e chiusi

La casella di controllo **Chiuso** determina se il percorso ricongiunge il suo ultimo punto al primo.

- **Chiuso** (l'impostazione predefinita) fa sì che il percorso delimiti una regione. È questo che [Estrusione lineare](../operations/path/linear-extrude.md) e [Rivoluzione](../operations/path/revolve.md) riempiono.
- **Apri** trasforma il percorso in una linea. Una linea non racchiude nulla, quindi nella scena appare come un sottile nastro lungo il suo sviluppo anziché come una forma piena. Usa [Gonfia percorso](../operations/path/inflate-path.md) per darle una larghezza e riportarla a qualcosa di solido.

Due cose da sapere prima di deselezionare **Chiuso**:

- **Richiudere non equivale ad annullare.** Aprire un percorso ne elimina il segmento di chiusura. Se quel segmento era curvo, riselezionando **Chiuso** ricomparirà una linea retta, non la curva. Usa invece Ctrl+Z: l'annullamento ripristina esattamente il percorso originale.
- **Alcuni contorni non si aprono.** Un contorno che resterebbe con meno di due punti - una goccia disegnata come un singolo punto e una curva che vi ritorna - rimane chiuso anziché ridursi a qualcosa che non potresti più vedere o selezionare. Lo stesso vale per un contorno che contiene una curva quadratica, presente ad esempio in un SVG importato: aprirlo appiattirebbe la curva in uno spigolo. Il rifiuto vale per singolo contorno, quindi il resto del percorso si apre comunque.

Se un percorso ha più contorni e questi non concordano, la casella di controllo risulta deselezionata. Selezionandola, tutti i contorni vengono allineati.

Le operazioni che richiedono una regione chiuderanno per te un percorso aperto anziché rifiutarlo. Estrusione lineare, Rivoluzione, Sottrai e le altre operazioni booleane si comportano tutte così, quindi un percorso aperto viene estruso ottenendo lo stesso solido della sua versione chiusa.

## Suggerimenti

- Usa Percorso personalizzato quando nessuna delle forme di percorso predefinite corrisponde a ciò che ti serve
- Per importare forme da editor vettoriali esterni, vedi [Oggetto SVG](../primitives/svg-object.md)
- Per disegnare una linea e trasformarla in un pezzo, deseleziona **Chiuso**, applica [Gonfia percorso](../operations/path/inflate-path.md) per darle uno spessore, quindi [Estrusione lineare](../operations/path/linear-extrude.md) per darle altezza

## Correlati

- [Percorso Cerchio](circle-path.md) - Un cerchio già pronto
- [Percorso Riquadro](box-path.md) - Un rettangolo già pronto
- [Oggetto SVG](../primitives/svg-object.md) - Importa percorsi vettoriali da file SVG
- [Estrusione lineare](../operations/path/linear-extrude.md) - Dai altezza ai percorsi
