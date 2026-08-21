---
title: Seleziona figlio
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Seleziona figlio

Seleziona figlio sceglie un figlio da un gruppo di oggetti in base a un numero di indice oppure a un nome. È particolarmente utile nei progetti parametrici e con script in cui si desidera scegliere dinamicamente quale oggetto visualizzare.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Come si usa

1. Seleziona due o più oggetti
2. Applica l'operazione **Seleziona figlio** dal menu Duplicazione
3. Scegli **Per indice** o **Per nome** per controllare come viene selezionato il figlio
4. Imposta il numero di indice o il nome da far corrispondere

## Parametri

- **Metodo di selezione** - Scegli tra **Per indice** (selezione in base alla posizione) o **Per nome** (selezione in base al nome dell'oggetto). Visualizzato come pulsanti.
- **Indice figlio** - L'indice in base zero del figlio da selezionare (mostrato quando si usa Per indice). Supporta le [espressioni](../../workspace/expressions.md).
- **Nome figlio** - Il nome del figlio da selezionare (mostrato quando si usa Per nome). Supporta le [espressioni](../../workspace/expressions.md).

Se l'indice è fuori intervallo o il nome non corrisponde ad alcun figlio, viene restituito il primo figlio come ripiego. Se non ci sono figli, non viene restituito nulla.

## Uso negli script

Seleziona figlio è progettato per funzionare con le espressioni e con la funzione `rand()` per creare progetti dinamici e guidati dai dati. Ad esempio, puoi costruire una scena con diversi oggetti varianti come figli e usare un'espressione come `rand(42)` come seed dell'indice per sceglierne uno in modo casuale.

**Esempio: libri di scena casuali per uno spettacolo teatrale**

1. Importa 5 mesh di libri diverse come figli di un'operazione Seleziona figlio
2. Imposta il Metodo di selezione su **Per indice**
3. Usa un'espressione per Indice figlio, ad esempio `floor(rand(seed) * 5)` dove `seed` è una variabile del foglio
4. Duplica più volte l'operazione Seleziona figlio, ognuna con un valore di seed diverso
5. Ogni istanza sceglie casualmente un libro diverso dall'insieme

Questo schema funziona in qualsiasi situazione in cui devi scegliere da un insieme di varianti: mobili, decorazioni, elementi architettonici o qualsiasi raccolta di parti intercambiabili.

## Suggerimenti

- Combina con [Serie](array.md) per creare motivi variati in cui ogni copia seleziona un figlio diverso
- Usa le variabili del foglio per l'indice o il nome, così da pilotare la selezione da un foglio di calcolo
- Il comportamento di ripiego sul primo figlio fa sì che il progetto non si rompa mai, anche se l'indice o il nome sono errati

## Correlati

- [Serie](array.md) - Duplica oggetti secondo schemi lineari, radiali, su curva e di trasformazione
