---
title: Foglio variabili
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# Foglio variabili

Il Foglio variabili memorizza valori condivisi per un progetto. Utilizzalo quando più oggetti devono fare riferimento alle stesse dimensioni, quantità, etichette o formule. La modifica di un valore nel foglio ricalcola gli oggetti dipendenti, così i progetti parametrici restano coerenti senza dover modificare ogni oggetto uno alla volta.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Come aggiungere un Foglio variabili

1. Apri la libreria e aggiungi **Foglio variabili** alla scena.
2. Seleziona l'oggetto Foglio variabili per visualizzare l'editor del foglio.
3. Seleziona una cella, quindi inserisci un **Nome** e un valore o una formula.
4. Utilizza il nome della cella dagli altri campi del progetto che supportano le espressioni.

## Modifica delle celle

Ogni cella ha due parti modificabili:

- **Nome** - Un nome di variabile facoltativo per la cella. I nomi non fanno distinzione tra maiuscole e minuscole, gli spazi vengono convertiti in trattini bassi e i nomi duplicati vengono corretti automaticamente.
- **Espressione** - Il valore della cella. Il testo semplice o i numeri vengono memorizzati direttamente. Le formule iniziano con `=`.

Le celle possono essere richiamate anche tramite indirizzo, come `A1` o `B2`. Le celle con nome sono di solito più chiare per i parametri di progetto perché ne descrivono l'intento, ad esempio `wall_thickness`, `outer_diameter` o `hole_count`.

## Formule

Inizia una formula con `=` per valutarla nel foglio:

- `=20 + 5` restituisce `25`
- `=pi * 10` restituisce `31.41592653589793`
- `=A1 * 2` fa riferimento a un'altra cella tramite indirizzo
- `=wall_thickness + 4` fa riferimento a una cella con nome

Il foglio supporta operazioni aritmetiche, parentesi, operatori di confronto, le comuni funzioni `Math` quali `sin`, `cos`, `sqrt` e `round`, e costanti come `pi`, `tau` e `e`.

## Utilizzo dei valori del foglio negli oggetti

La maggior parte dei campi numerici in MatterCAD supporta le espressioni. Per utilizzare un valore del foglio in un parametro di un oggetto, fai precedere il riferimento da `=`:

- Imposta la **Larghezza** di un Cubo su `=case_width`.
- Imposta la **Quantità** di una Serie su `=hole_count`.
- Imposta il valore **Offset** di una Trasla su `=wall_thickness * 2`.

Quando il foglio cambia, MatterCAD ricalcola gli oggetti che dipendono da esso.

## Testo e funzioni di supporto

Le celle del Foglio variabili possono contenere sia testo sia numeri. I valori di testo sono utili per etichette generate, codici articolo, dati importati e app di progettazione personalizzate.

Tra le funzioni di supporto utili:

- `concat()` o `strcat()` - Unisce testi o valori.
- `substring()` - Estrae una parte di un valore di testo.
- `split()` - Divide il testo e restituisce un elemento.
- `count()` - Conta gli elementi delimitati in un testo.
- `substitute()` - Sostituisce il testo.
- `rand(seed)` - Genera un valore casuale deterministico quando viene fornito un seme.
- `importdata()` - Legge un valore da un URL o da un percorso di file locale.

## Suggerimenti

- Preferisci nomi descrittivi agli indirizzi di cella per i valori utilizzati da altri oggetti.
- Mantieni le dimensioni principali in alto a sinistra nel foglio, così sono facili da trovare.
- Utilizza le formule per i valori derivati, ad esempio `inner_diameter = outer_diameter - wall_thickness * 2`.
- Evita di usare come nomi di cella parole riservate quali `pi`, `e`, `true`, `false` o nomi di funzioni.
- Se una formula non può essere interpretata, MatterCAD conserva l'input originale come testo.

## Correlati

- [Espressioni](expressions.md) - Utilizzare le espressioni nei parametri degli oggetti
- [Componenti](components.md) - Creare progetti parametrici riutilizzabili
- [Serie](../operations/array/array.md) - Creare motivi ripetuti guidati dai valori del foglio
