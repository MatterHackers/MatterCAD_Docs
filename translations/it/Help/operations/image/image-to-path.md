---
title: Da immagine a percorso
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Da immagine a percorso

Da immagine a percorso traccia i contorni di un'immagine per creare percorsi 2D. Questi percorsi possono poi essere estrusi, rivoluzionati o utilizzati con qualsiasi altra operazione sui percorsi. È ideale per convertire loghi, silhouette e grafiche semplici in oggetti 3D.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Come si usa

1. Seleziona un oggetto immagine nell'area di lavoro
2. Applica **Da immagine a percorso** dal menu delle operazioni Immagine
3. Scegli il tipo di analisi e regola l'intervallo di selezione

## Parametri

- **Tipo di analisi** - Come viene analizzata l'immagine per la tracciatura:
  - **Trasparenza** - Traccia in base alle aree trasparenti e opache (ideale per i PNG con sfondo trasparente)
  - **Colori** - Traccia in base alle regioni di colore
  - **Intensità** - Traccia in base ai livelli di luminosità (ideale per la maggior parte delle immagini)
- **Seleziona intervallo** - Un controllo a istogramma per selezionare quali valori di luminosità/colore includere nella tracciatura
- **Area superficie min** - Area minima affinché un anello di percorso venga incluso. Aumentala per filtrare i piccoli artefatti di disturbo

## Suggerimenti

- Le immagini nitide, ad alto contrasto e con forme semplici danno i risultati migliori
- Usa la modalità Trasparenza per le immagini PNG con sfondo trasparente
- Usa la modalità Intensità per fotografie e immagini prive di trasparenza
- Dopo la tracciatura, applica [Estrusione lineare](../path/linear-extrude.md) per dare altezza al percorso
- Aumenta Area superficie min per rimuovere dalla tracciatura i piccoli dettagli indesiderati

## Correlati

- [Convertitore immagini](image-converter.md) - Crea un rilievo basato su mappa di altezza invece di percorsi piatti
- [Litofania](lithophane.md) - Crea immagini retroilluminate
- [Oggetto SVG](../../primitives/svg-object.md) - Importa direttamente grafica vettoriale (senza bisogno di tracciatura)
- [Estrusione lineare](../path/linear-extrude.md) - Dai altezza al percorso tracciato
