---
title: Litofania
articleKey: LithophaneObject3D
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 170d39ef48f6ac290e56917bcaebeb458d55777f
source_lang: en
---
# Litofania

Una litofania è un pannello 3D sottile in cui un'immagine è codificata come spessore variabile. Con la retroilluminazione, le aree più sottili lasciano passare più luce, rivelando l'immagine. Questo crea un modo suggestivo per esporre fotografie e opere d'arte.

![20260324 080310 paste 20260324 080310](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080310-paste-20260324-080310.jpg)


## Come si usa

1. Importa un'immagine o seleziona un oggetto immagine esistente
2. Applica l'operazione **Litofania**
3. Regola la risoluzione e le dimensioni
4. Stampa il risultato con un materiale di colore chiaro e posizionalo davanti a una sorgente luminosa

## Parametri

- **Pixel per mm** - Risoluzione della litofania (predefinito: 1.5, intervallo: 0.5-3). Valori più alti catturano più dettagli ma generano file più grandi
- **Altezza** - Spessore massimo del pannello della litofania (predefinito: 2.5mm, intervallo: 0.5-3mm)
- **Larghezza** - Larghezza totale della litofania in pixel (predefinito: 150)
- **Inverti** - Inverte la mappatura chiaro/scuro (predefinito: attivo). Di norma si lascia attivo per una visualizzazione corretta in retroilluminazione

## Suggerimenti

- Stampa con materiale bianco o di colore chiaro per ottenere i risultati migliori
- Un'altezza di 2-3mm funziona bene per la maggior parte delle litofanie
- Un valore di Pixel per mm più alto cattura più dettagli ma aumenta il tempo di stampa e la dimensione del file
- Monta la stampa finita in una cornice con retroilluminazione a LED per la migliore visibilità
- I ritratti fotografici con un buon contrasto funzionano particolarmente bene

## Correlati

- [Convertitore immagini](image-converter.md) - Crea invece un rilievo in altorilievo dalle immagini
- [Da immagine a percorso](image-to-path.md) - Traccia i contorni dell'immagine come percorsi
