---
title: Sottrai e sostituisci
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Sottrai e sostituisci

Sottrai e sostituisci sottrae le parti scelte dalle parti non scelte, ma conserva il pezzo asportato come parte a sé stante invece di eliminarlo. Usa **Parte/i da sottrarre** per scegliere le forme di taglio; tutto il resto è la base che viene tagliata.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Combina](combine.md), [Sottrai](subtract.md), [Interseca](intersect.md) e Sottrai e sostituisci vengono eseguite tutte da un unico oggetto booleano: il pulsante della barra degli strumenti lo crea con Sottrai e sostituisci già selezionata e puoi passare in qualsiasi momento a una delle altre tre dalla riga di icone **Operazione** in cima al pannello Proprietà.

Sottrai e sostituisci non è disponibile per i percorsi 2D: una regione non ha alcun volume rimosso da restituire.

## Come si usa

1. Seleziona due o più oggetti
2. Fai clic su **Sottrai e sostituisci** nella barra degli strumenti
3. Usa **Parte/i da sottrarre** per scegliere quali oggetti figlio sono le forme di taglio
4. Cambia idea in qualsiasi momento facendo clic su un'icona diversa nella riga **Operazione** in cima al pannello Proprietà: la forma viene ricostruita con la nuova operazione

## Parametri

- **Operazione** - Quale operazione booleana eseguire. Mostrata come riga di icone in cima al pannello
- **Parte/i da sottrarre** - Quali oggetti figlio sono le forme di taglio
- **Mantieni geometria invertita** - Tratta un guscio invertito come materiale solido invece di lasciare che annulli il volume circostante. Attivalo quando un modello che dovrebbe essere solido risulta con parti mancanti. Impone l'uso del motore booleano esatto, più lento
- **Ripara ordine di avvolgimento** - Riavvolge i gusci invertiti di ciascuna parte prima dell'esecuzione dell'operazione booleana. In questo modo la geometria viene corretta una volta per tutte, invece di modificare ciò che ogni operazione successiva considera solido, ed è di solito la migliore delle due soluzioni per un modello invertito

## Suggerimenti

- Le due parti combaciano esattamente, perché derivano dalla stessa operazione
- Usala per progetti multicolore, assiemi a incastro e intarsi
- Se il risultato sembra errato, verifica che gli oggetti di partenza siano a tenuta stagna. **Ripara ordine di avvolgimento** corregge i gusci invertiti; [Ripara](../mesh/repair.md) corregge danni più estesi nei modelli importati

## Correlati

- [Combina](combine.md) - Unisci più oggetti in un'unica forma solida
- [Sottrai](subtract.md) - Taglia una forma da un'altra
- [Interseca](intersect.md) - Mantieni solo il volume in cui gli oggetti si sovrappongono
- [Taglio con piano](../reshape/plane-cut.md) - Taglia con un piano invece che con un'altra forma
- [Ripara](../mesh/repair.md) - Correggi le mesh importate danneggiate prima di un'operazione booleana

Questa pagina riguarda anche i vecchi oggetti Sottrai e sostituisci ancora presenti nei progetti salvati prima dell'unificazione delle operazioni. Continuano a funzionare esattamente come prima; i nuovi progetti usano l'oggetto booleano condiviso con l'operazione Sottrai e sostituisci selezionata.
