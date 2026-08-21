---
title: Interseca
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Interseca

Interseca mantiene solo il volume condiviso da tutti gli oggetti e scarta il resto.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Combina](combine.md), [Sottrai](subtract.md), Interseca e [Sottrai e sostituisci](subtract-and-replace.md) sono tutte eseguite da un unico oggetto booleano: il pulsante della barra degli strumenti lo crea con Interseca già selezionata e puoi passare in qualsiasi momento a una delle altre tre dalla riga di icone **Operazione** in cima al pannello Proprietà.

Interseca funziona sui solidi e sui percorsi 2D. Valuta ciò che gli fornisci ed esegue il tipo di operazione corretto, quindi l'intersezione di due percorsi produce un percorso e l'intersezione di due mesh produce un solido.

## Come si usa

1. Seleziona due o più oggetti
2. Fai clic su **Interseca** nella barra degli strumenti
3. Cambia idea in qualsiasi momento facendo clic su un'icona diversa nella riga **Operazione** in cima al pannello Proprietà: la forma viene ricostruita con la nuova operazione

## Parametri

- **Operazione** - Quale operazione booleana eseguire. Mostrata come riga di icone in cima al pannello
- **Mantieni geometria invertita** - Tratta un guscio invertito come materiale solido invece di lasciare che annulli il volume circostante. Attiva questa opzione quando un modello che dovrebbe essere solido presenta parti mancanti. Impone l'uso del motore booleano esatto, più lento
- **Ripara ordine di avvolgimento** - Riavvolge i gusci invertiti di ogni parte prima dell'esecuzione dell'operazione booleana. In questo modo la geometria viene corretta una volta per tutte, anziché modificare ciò che ogni operazione successiva considera solido, ed è di solito la migliore delle due soluzioni per un modello invertito

## Suggerimenti

- Gli oggetti devono sovrapporsi. Se non si sovrappongono effettivamente, il risultato è vuoto
- Con più di due oggetti l'operazione procede lungo l'elenco: i primi due vengono intersecati, poi il risultato viene intersecato con il terzo e così via
- Se un risultato sembra errato, verifica che gli oggetti di partenza siano a tenuta stagna. **Ripara ordine di avvolgimento** corregge i gusci invertiti; [Ripara](../mesh/repair.md) corregge danni più estesi nei modelli importati

## Correlati

- [Combina](combine.md) - Unisci più oggetti in un'unica forma solida
- [Sottrai](subtract.md) - Ritaglia una forma da un'altra
- [Sottrai e sostituisci](subtract-and-replace.md) - Sottrai una forma e conserva la parte asportata
- [Taglio con piano](../reshape/plane-cut.md) - Taglia con un piano invece che con un'altra forma
- [Ripara](../mesh/repair.md) - Correggi le mesh importate danneggiate prima di un'operazione booleana

Questa pagina descrive anche i vecchi oggetti Intersezione ancora presenti nei progetti salvati prima dell'unificazione delle operazioni. Continuano a funzionare esattamente come prima; i nuovi progetti usano l'oggetto booleano condiviso con l'operazione Interseca selezionata.
