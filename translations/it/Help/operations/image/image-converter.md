---
title: Convertitore immagini
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c1a05f9688ebe115babfad5d63fc49445af7c449
source_lang: en
---
# Convertitore immagini

Il Convertitore immagini trasforma un'immagine raster in un rilievo 3D in cui la luminosità dei pixel determina l'altezza. Le aree chiare diventano rialzate e le aree scure diventano basse (o viceversa).

![20260323 210414 paste 20260323 210414](https://matterhackers.github.io/MatterCAD_Docs/assets/20260323-210414-paste-20260323-210414.jpg)


## Come si usa

1. Aggiungi un Convertitore immagini dal pannello Primitive, oppure trascina un file immagine nell'area di lavoro
2. L'immagine viene convertita in una mappa di altezza 3D
3. Regola l'altezza e gli altri parametri

## Suggerimenti

- Le immagini ad alto contrasto con forme nette producono i risultati migliori
- Per tracciare i contorni dell'immagine come percorsi piani anziché come mappe di altezza, usa [Da immagine a percorso](image-to-path.md)
- Per creare display luminosi retroilluminati, usa [Litofania](lithophane.md)
- Puoi trascinare le immagini direttamente dal desktop nell'area di lavoro
- Aggiungi una base combinando il rilievo dell'immagine con un [Cubo](../../primitives/cube.md)

## Correlati

- [Da immagine a percorso](image-to-path.md) - Traccia i contorni anziché creare una mappa di altezza
- [Litofania](lithophane.md) - Crea display luminosi retroilluminati
- [Oggetto Immagine](../../primitives/image-object.md) - La versione primitiva dell'importazione di immagini
