---
title: Salvataggio ed esportazione
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Salvataggio ed esportazione

MatterCAD supporta diversi formati di file per salvare ed esportare i tuoi progetti. Il formato da scegliere dipende da come intendi utilizzare il file.

## Formati di salvataggio

### MCX (formato nativo)

MCX è il formato di file nativo di MatterCAD ed è la scelta migliore per i progetti che vuoi continuare a modificare in seguito. Conserva:

- L'intero albero del progetto con tutti gli oggetti e la loro gerarchia
- Tutti i parametri e le impostazioni di ciascun oggetto
- Operazioni booleane, serie e altre operazioni in forma modificabile
- Le relazioni tra i componenti

**Usa MCX quando:** vuoi salvare il tuo lavoro e continuare a modificarlo in seguito.

### STL

STL è il formato più diffuso per la stampa 3D. Contiene solo la geometria finale della mesh triangolare, senza cronologia del progetto né parametri.

**Usa STL quando:** vuoi stampare in 3D il tuo progetto o condividerlo con qualcuno che non usa MatterCAD.

### OBJ

OBJ (Wavefront) è un formato 3D comune, supportato dalla maggior parte dei software 3D. Come STL, contiene solo la geometria della mesh.

**Usa OBJ quando:** devi aprire il tuo progetto in altri software 3D come Blender o un motore di gioco.

### SVG

L'esportazione SVG crea un file vettoriale 2D a partire dalla vista dall'alto del tuo progetto. È utile per il taglio laser o la fresatura CNC.

**Usa SVG quando:** ti serve un profilo 2D del tuo progetto per il taglio laser o l'incisione.

## Come salvare

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Apri il **menu del marchio** (il logo MatterCAD nell'angolo in alto a sinistra)
2. Seleziona **Salva con nome** per scegliere una posizione e un formato
3. Seleziona il formato del file dal menu a discesa dei formati
4. Scegli dove salvare il file e fai clic su **Salva**

Il tuo progetto viene salvato automaticamente anche mentre lavori, così non perderai le modifiche se chiudi l'applicazione.

## Suggerimenti

- Salva sempre una copia MCX del tuo progetto prima di esportarlo in STL o OBJ, così potrai apportare modifiche in seguito
- Durante l'esportazione in STL, tutti gli oggetti della scena vengono uniti in un'unica mesh
- Se devi condividere un progetto con qualcuno che usa MatterCAD, invia il file MCX per conservare la piena modificabilità
- Puoi anche salvare i progetti nella tua [Libreria cloud](../library/cloud-library.md) per accedervi da qualsiasi computer

## Argomenti correlati

- [Aggiunta di oggetti esistenti](adding-existing-objects.md) - Importa file in MatterCAD
- [Libreria](../library/index.md) - Organizza i progetti salvati
- [Libreria cloud](../library/cloud-library.md) - Archivia i progetti nel cloud
