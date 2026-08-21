---
title: Allinea
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Allinea

Allinea posiziona con precisione più oggetti rispetto a un oggetto di ancoraggio. Usalo per allineare bordi, centrare parti l'una sull'altra, collocare un oggetto sopra un altro o creare pile spaziate in modo uniforme.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Come si usa

1. Seleziona due o più oggetti.
2. Applica l'operazione **Allinea** dal menu **Posizionamento**.
3. Scegli l'oggetto **Ancoraggio**. L'ancoraggio resta fermo mentre gli altri oggetti si spostano.
4. Imposta l'allineamento per gli assi X, Y e Z in modo indipendente.
5. Usa **Applica** quando vuoi fissare le posizioni allineate nell'albero degli oggetti.

## Parametri

### Ancoraggio

L'elenco **Ancoraggio** seleziona l'oggetto figlio usato come riferimento. L'ancoraggio non si sposta. Ogni altro figlio dell'operazione Allinea viene riposizionato rispetto all'ancoraggio, a meno che un asse non usi la modalità **Impilato**.

### Controlli asse

Ogni asse ha i propri controlli. Puoi allineare su un asse, due assi o tutti e tre. I bordi minimo e massimo prendono il nome dall'asse:

- **Asse X** - Min è a sinistra, Max è a destra.
- **Asse Y** - Min è davanti, Max è dietro.
- **Asse Z** - Min è in basso, Max è in alto.

Per ciascun asse:

- **Allinea** - Sceglie il punto di riferimento dell'ancoraggio per quell'asse. Usa **Nessuno** per lasciare invariate le posizioni su quell'asse.
- **Modalità** - Controlla come viene applicato l'allineamento selezionato:
  - **Semplice** - Fa corrispondere il bordo, il centro o l'origine corrispondente di ciascun oggetto in movimento a quello dell'ancoraggio. Non viene usato alcun offset.
  - **Offset** - Scegli quale parte dell'oggetto in movimento deve appoggiarsi al riferimento dell'ancoraggio, quindi aggiungi la spaziatura con **Offset**.
  - **Impilato** - Colloca gli oggetti uno dopo l'altro lungo quell'asse, usando **Offset** come distanza tra di essi.
- **Sottoallinea** - Disponibile in modalità **Offset**. Sceglie la parte dell'oggetto in movimento da collocare sul riferimento dell'ancoraggio. Se **Sottoallinea** è **Nessuno**, Allinea usa lo stesso bordo, centro o origine selezionato da **Allinea**.
- **Offset** - Disponibile nelle modalità **Offset** e **Impilato**. Aggiunge una distanza lungo quell'asse e supporta le [espressioni](../../workspace/expressions.md).

## Modalità di allineamento

### Semplice

Usa **Semplice** quando devi far corrispondere posizioni dello stesso tipo. Ad esempio, **Allineamento X: Centro** sposta ogni oggetto non ancoraggio in modo che il suo centro X coincida con il centro X dell'ancoraggio. **Allinea Z: Min** sposta ogni oggetto non ancoraggio in modo che la sua base si trovi all'altezza della base dell'ancoraggio.

### Offset

Usa **Offset** quando la parte dell'oggetto in movimento deve essere diversa dal riferimento dell'ancoraggio. Ad esempio, per collocare un oggetto sopra l'ancoraggio:

1. Imposta **Allinea Z** su **Max** (in alto).
2. Imposta **Modalità Z** su **Offset**.
3. Imposta **Sottoallinea Z** su **In basso**.
4. Imposta **Offset Z** sulla distanza desiderata, oppure lascialo a `0` per il contatto diretto.

In questo modo la base dell'oggetto in movimento viene collocata sulla sommità dell'ancoraggio, con una spaziatura facoltativa.

### Impilato

Usa **Impilato** per concatenare più oggetti lungo un asse. Gli oggetti vengono elaborati per nome e poi per ID interno, quindi assegnare nomi chiari agli oggetti rende prevedibile l'ordine della pila.

In modalità **Impilato**, ogni oggetto in movimento viene collocato contro il riferimento precedente su quell'asse:

- L'allineamento **Min** impila verso la direzione positiva, ad esempio da sinistra a destra su X o dal basso verso l'alto su Z.
- L'allineamento **Max** impila verso la direzione negativa, ad esempio da destra a sinistra su X o dall'alto verso il basso su Z.
- Gli allineamenti **Centro** e **Origine** usano l'offset tra il centro o l'origine di ciascun oggetto.

Usa **Offset** in modalità **Impilato** per impostare la distanza tra gli oggetti.

## Esempi

- **Centrare gli oggetti sull'ingombro del piano** - Scegli come **Ancoraggio** l'oggetto che deve restare fermo, quindi imposta **Allineamento X** e **Allineamento Y** su **Centro**.
- **Collocare un oggetto sopra un altro** - Imposta **Allinea Z** su **Max** (in alto), **Modalità Z** su **Offset** e **Sottoallinea Z** su **In basso**.
- **Aggiungere una distanza precisa da un bordo** - Usa la modalità **Offset**, scegli il bordo dell'oggetto in movimento con **Sottoallinea**, quindi imposta **Offset** sulla spaziatura desiderata.
- **Allineare più oggetti uno dopo l'altro** - Imposta **Allineamento X** su **Min** (sinistra), **Modalità X** su **Impilato** e usa **Offset X** per la distanza.
- **Costruire una pila verticale** - Imposta **Allinea Z** su **Min** (in basso), **Modalità Z** su **Impilato** e usa **Offset Z** per lo spazio tra gli oggetti.

## Suggerimenti

- L'oggetto di ancoraggio resta fermo; gli altri oggetti si spostano per allinearsi ad esso.
- Puoi usare modalità diverse su assi diversi, ad esempio **Impilato** su X e **Centro** con **Semplice** su Y.
- Usa i nomi degli oggetti per controllare l'ordine **Impilato** quando allinei più oggetti contemporaneamente.
- Allinea non è distruttivo finché non viene applicato. Puoi modificare le impostazioni in qualsiasi momento per riallineare gli oggetti figli.
- Usa **Origine** quando devi allineare le origini di modellazione anziché i bordi del riquadro di delimitazione.

## Correlati

- [Adatta ai limiti](fit-to-bounds.md) - Scala un oggetto per adattarlo a dimensioni specifiche
- [Trasla](../transform/translate.md) - Sposta di una distanza specifica
- [Raggruppamento](../../workspace/grouping.md) - Raggruppa gli oggetti allineati per tenerli insieme
