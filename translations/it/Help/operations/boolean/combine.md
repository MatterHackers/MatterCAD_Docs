---
title: Combina
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Combina

Combina unisce tutto in un unico solido. Le facce interne dove le forme si sovrapponevano vengono rimosse, così il risultato è una mesh continua anziché gusci sovrapposti.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Combina, [Sottrai](subtract.md), [Interseca](intersect.md) e [Sottrai e Sostituisci](subtract-and-replace.md) vengono eseguiti tutti da un unico oggetto booleano: il pulsante della barra degli strumenti lo crea con Combina già selezionato e puoi passare in qualsiasi momento a una delle altre tre operazioni dalla riga di icone **Operazione** in cima al pannello Proprietà.

Combina funziona sui solidi e sui percorsi 2D. Valuta ciò che gli hai fornito ed esegue il tipo di operazione corretto, quindi combinando due percorsi si ottiene un percorso e combinando due mesh si ottiene un solido.

## Come si usa

1. Seleziona due o più oggetti
2. Fai clic su **Combina** nella barra degli strumenti
3. Cambia idea in qualsiasi momento facendo clic su un'icona diversa nella riga **Operazione** in cima al pannello Proprietà: la forma viene ricostruita con la nuova operazione

## Parametri

- **Operazione** - Quale operazione booleana eseguire. Mostrata come riga di icone in cima al pannello
- **Mantieni geometria invertita** - Tratta un guscio invertito come materiale solido invece di lasciare che annulli il volume circostante. Attiva questa opzione quando un modello che dovrebbe essere solido presenta parti mancanti. Impone l'uso del motore booleano esatto, più lento
- **Ripara ordine di avvolgimento** - Corregge l'avvolgimento dei gusci invertiti di ogni parte prima dell'esecuzione dell'operazione booleana. Questo sistema corregge la geometria una volta per tutte, invece di modificare ciò che ogni operazione successiva considera solido, ed è di solito la migliore delle due soluzioni per un modello invertito

## Suggerimenti

- Combina unisce in un'unica mesh anche oggetti non sovrapposti, ma questi restano visivamente separati
- Combina gestisce automaticamente gli oggetti Foro: tutto ciò che è contrassegnato come foro viene sottratto dal risultato anziché aggiunto
- Combina mantiene i colori per faccia degli oggetti originali
- Se un risultato sembra errato, verifica che gli oggetti di origine siano a tenuta stagna. **Ripara ordine di avvolgimento** corregge i gusci invertiti; [Ripara](../mesh/repair.md) corregge danni più estesi nei modelli importati

## Correlati

- [Sottrai](subtract.md) - Ritaglia una forma da un'altra
- [Interseca](intersect.md) - Mantiene solo il volume in cui gli oggetti si sovrappongono
- [Sottrai e Sostituisci](subtract-and-replace.md) - Sottrae una forma e conserva la parte asportata
- [Taglio con piano](../reshape/plane-cut.md) - Taglia con un piano invece che con un'altra forma
- [Foro](../../primitives/hole.md) - Un cubo preconfigurato per la sottrazione
- [Ripara](../mesh/repair.md) - Corregge le mesh importate danneggiate prima di un'operazione booleana

Questa pagina riguarda anche i vecchi oggetti Combina ancora presenti nei progetti salvati prima dell'unificazione delle operazioni. Continuano a funzionare esattamente come prima; i nuovi progetti usano l'oggetto booleano condiviso con l'operazione Combina selezionata.
