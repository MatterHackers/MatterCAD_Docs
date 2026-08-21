---
title: Percorso Anello
articleKey: RingPathObject3D
parent: "2D Paths"
nav_order: 4
source_hash: 3ee3dd9ab102cfabf1e79d1093b237fb90f12aca
source_lang: en
---
# Percorso Anello

Una forma ad anello 2D, ovvero un cerchio con un foro circolare al centro. Da usare con [Estrusione lineare](../operations/path/linear-extrude.md) per creare forme tubolari o rondelle.

<!-- Screenshot of a Ring Path on the workspace -->
![20260506 080211 paste 20260506 080211](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080211-paste-20260506-080211.jpg)

## Parametri

- **Diametro esterno** - Il diametro esterno dell'anello
- **Diametro interno** - Il diametro del foro al centro

## Suggerimenti

- Lo spessore della parete dell'anello è (Diametro esterno - Diametro interno) / 2
- L'estrusione di un Percorso Anello crea un tubo simile alla primitiva [Anello](../primitives/ring.md)

## Correlati

- [Percorso Cerchio](circle-path.md) - Un cerchio pieno (senza foro)
- [Anello](../primitives/ring.md) - Una forma tubolare 3D già pronta
- [Estrusione lineare](../operations/path/linear-extrude.md) - Conferisce altezza ai percorsi
