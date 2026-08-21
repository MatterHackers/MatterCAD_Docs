---
title: Percorso stella
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Percorso stella

Un percorso 2D a forma di stella con numero di punte e raggio interno/esterno configurabili. Usalo con [Estrusione lineare](../operations/path/linear-extrude.md) per creare forme a stella 3D.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parametri

- **Punti** - Numero di punte della stella
- **Raggio esterno** - Distanza dal centro alla punta di ciascun vertice
- **Raggio interno** - Distanza dal centro agli incavi tra le punte

## Suggerimenti

- Il rapporto tra Raggio interno e Raggio esterno determina quanto è "appuntita" la stella. Un Raggio interno ridotto crea punte nette e pronunciate.
- Imposta Punti su 5 per una stella classica, su 6 per una stella di David, oppure su valori più alti per forme simili a ingranaggi
- Usa [Leviga percorso](../operations/path/smooth-path.md) su un Percorso stella per creare forme a stella arrotondate

## Correlati

- [Percorso cerchio](circle-path.md) - Un cerchio levigato
- [Ingranaggio 2D](../mechanical/gear-2d.md) - Un vero profilo di ingranaggio
- [Estrusione lineare](../operations/path/linear-extrude.md) - Dai altezza ai percorsi
