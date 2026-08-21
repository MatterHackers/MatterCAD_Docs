---
title: Scala
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Scala

Scala ridimensiona un oggetto con un controllo preciso su dimensioni, proporzioni e conversione delle unità. Puoi scalare in modo uniforme, bloccare insieme assi specifici oppure ridimensionare ogni asse in modo indipendente.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Scala** dal menu Trasforma
3. Scegli il metodo di scalatura e inserisci i valori desiderati

Puoi anche scalare gli oggetti nella vista facendo clic e trascinando i controlli angolari di scala su un oggetto selezionato.

## Parametri

### Tipo di scala

Scegli una preimpostazione o una scalatura personalizzata:

- **Personalizzato** - Inserisci le tue dimensioni o percentuali
- **da pollici a mm** - Moltiplica per 25,4 (converte da imperiale a metrico)
- **mm a pollici** - Moltiplica per 0,0393 (converte da metrico a imperiale)
- **mm a cm** - Moltiplica per 0,1
- **da cm a mm** - Moltiplica per 10

### Metodo di scala (modalità Personalizzato)

- **Diretto** - Inserisci Larghezza, Profondità e Altezza desiderate in millimetri
- **Percentuale** - Inserisci Larghezza, Profondità e Altezza come percentuali della dimensione originale

### Blocca proporzioni

- **Nessuno (Scala libera)** - Ogni asse viene scalato in modo indipendente
- **X e Y** - Larghezza e Profondità sono bloccate insieme; l'Altezza viene scalata in modo indipendente
- **X, Y e Z** - Tutti e tre gli assi vengono scalati insieme in modo uniforme

### Dimensioni

- **Larghezza** - Dimensione lungo l'asse X
- **Profondità** - Dimensione lungo l'asse Y
- **Altezza** - Dimensione lungo l'asse Z

## Suggerimenti

- Usa "da pollici a mm" se hai importato un file STL progettato in pollici che appare troppo piccolo
- Imposta Blocca proporzioni su X, Y e Z per una scalatura uniforme: modificando una qualsiasi dimensione si aggiornano tutte
- La posizione della base dell'oggetto viene mantenuta durante la scalatura, così resta appoggiato sulla superficie dell'area di lavoro
- Puoi digitare valori esatti per un dimensionamento preciso oppure usare i cursori per regolazioni rapide

## Correlati

- [Trasla](translate.md) - Sposta un oggetto
- [Ruota](rotate.md) - Ruota un oggetto
- [Adatta ai limiti](../placement/fit-to-bounds.md) - Scala per rientrare in una dimensione specifica
