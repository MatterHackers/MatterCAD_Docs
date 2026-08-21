---
title: Ripara
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Ripara

Ripara corregge i problemi più comuni della geometria mesh, tra cui bordi non-manifold, fori, orientamento facce incoerente e vertici quasi coincidenti. È particolarmente utile per i file STL e OBJ importati che possono contenere errori.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Come si usa

1. Seleziona un oggetto con problemi di mesh
2. Applica l'operazione **Ripara** dal menu Mesh
3. Esamina le statistiche prima/dopo per vedere cosa è stato corretto

## Statistiche (sola lettura)

- **Vertici iniziali / Vertici finali** - Numero di vertici prima e dopo la riparazione
- **Facce iniziali / Facce finali** - Numero di facce prima e dopo la riparazione
- **Bordi Non-manifold iniziali / Bordi Non-manifold finali** - Numero di bordi problematici prima e dopo

### Opzioni avanzate

Attiva la modalità **Avanzate** per un controllo dettagliato:

- **Salda vertici** - Unisce i vertici quasi coincidenti (predefinito: attivo)
- **Tolleranza di saldatura** - Quanto devono essere vicini i vertici per essere uniti
- **Orientamento facce** - Raddrizza i gusci rovesciati, in modo che ogni corpo risulti solido. Ogni guscio viene valutato singolarmente, così un modello cavo mantiene le proprie cavità invece di vederle riempite. I gusci le cui facce sono in disaccordo tra loro vengono lasciati invariati anziché interpretati a caso, e i modelli non a tenuta stagna ricadono su una riparazione più tollerante: esegui prima **Riempi fori** se il solo orientamento non li corregge.
- **Salda bordi** - Ripara piccole crepe e giunzioni difettose
- **Riempi fori** - Riempie le lacune nella superficie della mesh
- **Modalità rimozione** - Rimuove la geometria interna o occlusa:
  - **Nessuno** - Mantiene tutta la geometria
  - **Interno** - Rimuove i corpi interni nascosti all'interno della forma principale
  - **Occluso** - Rimuove le facce non visibili dall'esterno

## Suggerimenti

- Prova prima Ripara se le operazioni booleane (Combina, Sottrai) producono risultati inattesi sui modelli importati
- Le impostazioni predefinite (Salda vertici attivo, tutto il resto disattivato) risolvono i problemi più comuni
- Attiva Riempi fori se riesci a vedere attraverso le lacune del modello
- Usa Rimuovi Interno per ripulire i modelli che contengono geometria nascosta all'interno

## Correlati

- [Decima](decimate.md) - Riduce il numero di poligoni
- [Aggiungere oggetti esistenti](../../getting-started/adding-existing-objects.md) - Importa modelli che potrebbero richiedere una riparazione
