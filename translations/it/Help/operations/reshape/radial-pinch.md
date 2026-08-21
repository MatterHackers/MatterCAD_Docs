---
title: Compressione radiale
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Compressione radiale

La Compressione radiale comprime un oggetto verso l'interno a partire da un punto centrale, con una curva di profilo personalizzabile. A differenza del [Restringimento](pinch.md) normale, che agisce dal retro verso il fronte, la Compressione radiale comprime in modo simmetrico attorno a un asse centrale.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Compressione radiale** dal menu Rimodella
3. Modifica il profilo del percorso per definire quanta compressione viene applicata a ciascuna altezza
4. Regola il numero di sezioni per ottenere una maggiore levigatezza

## Parametri

- **Percorso** - Un editor di curve di profilo che definisce l'entità della compressione a ogni livello di altezza. Modifica la curva per creare profili di compressione personalizzati
- **Sezioni** - Numero di tagli orizzontali per una compressione uniforme, distribuiti in modo regolare lungo il pezzo. Più sezioni = risultati più levigati

### Parametri avanzati

- **Tipo di compressione** - Direzione della compressione:
  - **Radiale** - Comprime in modo uniforme da tutti i lati verso il centro
  - **Asse X** - Comprime solo lungo l'asse X
  - **Asse Y** - Comprime solo lungo l'asse Y
- **Offset rotazione** - Sposta il centro dell'effetto di compressione

## Suggerimenti

- Usa l'editor del percorso per creare forme a clessidra, a bottiglia o a vaso
- La compressione radiale è ideale per creare forme organiche e arrotondate a partire da oggetti cilindrici
- Aumenta le Sezioni per ottenere curve più levigate, soprattutto con profili di compressione molto stretti

## Correlati

- [Restringimento](pinch.md) - Compressione semplice dal retro verso il fronte
- [Torsione](twist.md) - Rotazione a spirale lungo l'altezza
- [Curva](curve.md) - Piega ad arco
