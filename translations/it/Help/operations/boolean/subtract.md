---
title: Sottrai
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Sottrai

Sottrai ritaglia le parti che scegli dalle parti che non hai scelto. Usa **Parte/i da sottrarre** per selezionare le forme di taglio; tutto il resto è la base che viene tagliata.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Combina](combine.md), Sottrai, [Interseca](intersect.md) e [Sottrai e Sostituisci](subtract-and-replace.md) sono tutte eseguite da un unico oggetto booleano: il pulsante della barra degli strumenti lo crea con Sottrai già selezionato e puoi passare a una qualsiasi delle altre tre in qualunque momento dalla riga di icone **Operazione** in cima al pannello Proprietà.

Sottrai funziona sui solidi e sui percorsi 2D. Valuta ciò che gli fornisci ed esegue il tipo di operazione corretto, quindi sottrarre un percorso da un altro produce un percorso e sottrarre una mesh da un'altra produce un solido.

## Come si usa

1. Seleziona due o più oggetti
2. Fai clic su **Sottrai** nella barra degli strumenti: viene scelta automaticamente una parte da ritagliare predefinita, così l'operazione produce subito un risultato
3. Usa **Parte/i da sottrarre** per scegliere quali elementi figli sono le forme di taglio
4. Cambia idea in qualsiasi momento facendo clic su un'icona diversa nella riga **Operazione** in cima al pannello Proprietà: la forma viene ricostruita con la nuova operazione

## Parametri

- **Operazione** - Quale operazione booleana eseguire. Mostrata come riga di icone in cima al pannello
- **Parte/i da sottrarre** - Quali elementi figli sono le forme di taglio
- **Mantieni parti sottratte** - Lascia nella scena le parti che sono state ritagliate invece di eliminarle
- **Mantieni geometria invertita** - Tratta un guscio invertito come materiale solido invece di lasciare che annulli il volume circostante. Attiva questa opzione quando un modello che dovrebbe essere solido risulta con parti mancanti. Impone l'uso del motore booleano esatto, più lento
- **Ripara ordine di avvolgimento** - Corregge l'avvolgimento dei gusci invertiti di ciascuna parte prima dell'esecuzione dell'operazione booleana. In questo modo la geometria viene riparata una volta per tutte, invece di modificare ciò che ogni operazione successiva considera solido, ed è di solito la migliore delle due soluzioni per un modello invertito

## Suggerimenti

- Gli oggetti devono sovrapporsi affinché Sottrai produca un effetto
- Per ricavare un foro passante, assicurati che l'oggetto di taglio attraversi completamente la base
- Per un foro semplice, la primitiva [Foro](../../primitives/hole.md) è già configurata per la sottrazione
- Gli oggetti di taglio restano nell'albero del progetto, quindi puoi spostarli o ridimensionarli e il taglio si aggiorna
- Se un risultato sembra errato, verifica che gli oggetti di origine siano a tenuta stagna. **Ripara ordine di avvolgimento** corregge i gusci invertiti; [Ripara](../mesh/repair.md) risolve danni più estesi nei modelli importati

## Correlati

- [Combina](combine.md) - Unisci più oggetti in un'unica forma solida
- [Interseca](intersect.md) - Mantieni solo il volume in cui gli oggetti si sovrappongono
- [Sottrai e Sostituisci](subtract-and-replace.md) - Sottrai una forma e conserva il pezzo che è stato ritagliato
- [Taglio con piano](../reshape/plane-cut.md) - Taglia con un piano anziché con un'altra forma
- [Foro](../../primitives/hole.md) - Un cubo preconfigurato per la sottrazione
- [Ripara](../mesh/repair.md) - Correggi mesh importate danneggiate prima di un'operazione booleana

Questa pagina riguarda anche i vecchi oggetti Sottrai ancora presenti nei progetti salvati prima che le operazioni venissero unificate. Continuano a funzionare esattamente come prima; i nuovi progetti usano l'oggetto booleano condiviso con l'operazione Sottrai selezionata.
