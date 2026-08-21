---
title: Rivoluzione
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Rivoluzione

Rivoluzione fa ruotare un percorso 2D attorno a un asse per creare un solido di rivoluzione 3D. È così che si creano vasi, ciotole, ruote e altri oggetti a simmetria rotazionale.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Come si usa

1. Seleziona un percorso 2D
2. Applica **Rivoluzione** dal menu delle operazioni Percorso
3. Regola l'intervallo di rotazione, la posizione dell'asse e il numero di lati

## Parametri

- **Rotazione** - Angolo di rotazione totale della rivoluzione (predefinito: 0, intervallo: 0-360). Imposta 360 per una rivoluzione completa.
- **Posizione asse** - Scostamento dell'asse di rotazione dal centro del percorso (predefinito: 0, intervallo: da -30 a 30). Un valore positivo allontana l'asse dal percorso, creando un'apertura più ampia.
- **Angolo iniziale** - Punto in cui inizia la rivoluzione (predefinito: 0)
- **Angolo finale** - Punto in cui termina la rivoluzione (predefinito: 45). Imposta 360 per una rivoluzione completa.
- **Lati** - Numero di segmenti lungo la rivoluzione (predefinito: 30). Più segmenti = superficie più liscia.

## Suggerimenti

- Usa Posizione asse per controllare il diametro interno della forma di rivoluzione
- Imposta Angolo iniziale e Angolo finale a valori inferiori a 360 per creare rivoluzioni parziali (archi, grondaie)
- Disegna il percorso del profilo del tuo vaso o della tua ciotola, quindi applica la rivoluzione per ottenere una simmetria perfetta
- Un [Percorso Cerchio](../../2d-paths/circle-path.md) sottoposto a rivoluzione crea un toro

## Correlati

- [Estrusione lineare](linear-extrude.md) - Estrude in verticale invece di ruotare
- [Percorsi 2D](../../2d-paths/index.md) - Crea percorsi di profilo da sottoporre a rivoluzione
- [Torus](../../primitives/torus.md) - Una forma ad anello di rivoluzione già pronta
