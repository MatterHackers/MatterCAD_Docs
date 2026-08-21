---
title: Note di rilascio
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (13 agosto 2026)
[Download per Windows](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## Nuove funzionalità

* **Modifica figli**
  * Fai doppio clic su un oggetto sul piano di stampa o nell'albero della scena per entrarvi e modificare le parti che lo compongono — senza finestre o schede separate
  * Per operazioni come Sottrai, modifichi le parti di origine e il risultato viene ricostruito quando esci
  * Un percorso di navigazione nella parte superiore dell'albero della scena mostra il percorso completo; facendo clic su un livello le modifiche vengono integrate come un unico passaggio annullabile e ogni livello mantiene la propria cronologia di annullamento
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **Un unico strumento booleano**
  * Combina, Sottrai, Interseca e Sottrai e sostituisci sono ora un'unica operazione con una riga di icone nella parte superiore del pannello — cambia modalità con un clic invece di eliminare e riapplicare
  * La stessa operazione gestisce sia le mesh 3D sia i percorsi 2D e mostra l'avanzamento durante l'esecuzione di un'operazione booleana pesante
  * I progetti salvati con i vecchi oggetti booleani separati continuano ad aprirsi normalmente
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **Operazioni booleane che funzionano e basta**
  * Le operazioni booleane utilizzano un nuovo motore nativo, più veloce e in grado di riuscire su mesh che in precedenza fallivano
  * Combina ripara automaticamente le parti con fori: le riparazioni pulite entrano nell'unione, le parti che non possono essere unite in sicurezza vengono mantenute accanto ad essa e nominate per te, e una parte che non è stato possibile riparare conserva la geometria originale
  * Taglio con piano è ora una vera intersezione solida, quindi il risultato è a tenuta stagna e stampabile invece di un guscio aperto
  * Nuove opzioni Mantieni geometria invertita e Ripara ordine di avvolgimento per le mesh importate problematiche


## Miglioramenti

* **Editor percorso 2D**
  * Quattro modalità punto — Spigolo, Simmetrico, Allineato e Libero — applicabili con un clic, sia nell'editor 2D sia nella vista 3D
  * Specchia è ora una modalità di simmetria in tempo reale: le modifiche vengono rispecchiate rispetto al centro mentre le esegui e trascinando una coppia speculare sull'asse questa si fonde in un unico punto
  * Seleziona i punti trascinando un rettangolo di selezione, spostali come gruppo, aggancia alla griglia e premi Esc per annullare un trascinamento
  * Uniforma fa passare una curva attraverso i punti che hai definito con un solo passaggio
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **Visualizzazione e navigazione**
  * Premi Z con un percorso piano selezionato per passare con un'animazione a una vista di modifica dall'alto adattata al percorso
  * Il rendering del testo sub-pixel è ora attivo automaticamente quando lo schermo lo supporta e può comunque essere attivato o disattivato nelle impostazioni Avanzate

* **Modellazione**
  * Estrusione lineare può smussare il bordo inferiore con stile, raggio e numero di segmenti propri
  * Gli oggetti solo per l'editor (Curva 3D, Strumento di misura, Descrizione, Foglio) vengono ancora visualizzati ma sono esclusi dall'esportazione

## Principali correzioni di bug

  * Un salvataggio interrotto a metà poteva troncare il file che stava sostituendo segnalando comunque il successo. Ora i salvataggi vengono completati per intero e poi sostituiscono la destinazione in modo atomico — la stessa protezione vale per i salvataggi nella libreria e le esportazioni
  * Un salvataggio non riuscito lascia il progetto contrassegnato come non salvato, così la chiusura dell'applicazione non può eliminare silenziosamente il tuo lavoro
  * Il salvataggio su disco di un elemento cloud manteneva il vecchio nome della scheda e la scheda andava persa al riavvio
  * Risolto il problema dei sotto-modelli 3MF scartati silenziosamente al caricamento e dei file 3MF caricati contemporaneamente che si contaminavano a vicenda
  * Risolti arresti anomali, un filtro istogramma non funzionante e le copie di una parte immagine che non restavano sincronizzate con l'originale
  * Risolto un arresto anomalo durante l'eliminazione di un punto di curva e il problema dei punti sulla giunzione di un percorso chiuso che ripristinavano la modalità scelta
  * Il pulsante Stop di un'attività in esecuzione è ora cliccabile e la annulla effettivamente

---

# MatterCAD 2.2026.5 (8 maggio 2026)
[Download per Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## Nuove funzionalità

* **Strumento serie ridisegnato**
  * Un'unica operazione Serie unificata sostituisce le vecchie Serie lineare, Serie radiale e Serie avanzata
  * Modalità **Lineare**: copie lungo una direzione con rotazione opzionale e scala progressiva
  * Modalità **Radiale**: copie attorno a un asse centrale con raggio, angolo di rotazione e schemi ad arco o a cerchio completo configurabili
  * Modalità **Trasforma**: copie ripetute usando una trasformazione manuale o la trasformazione di un oggetto di pari livello specificato
  * La modalità di rotazione Composizione in Lineare crea spirali, ventagli ed eliche in modo naturale
  * Opzione La scala influisce sull'offset per disposizioni a conchiglia di nautilus e a progressione geometrica
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **Preferiti della libreria**
  * Contrassegna con una stella qualsiasi elemento della libreria per aggiungerlo a una cartella Preferiti permanente
  * Accedi rapidamente da un unico posto alle primitive, ai generatori e alle parti salvate che usi più spesso
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## Miglioramenti

* **Allinea**
  * L'allineamento Impilato è ora un pulsante di modalità diretto invece di un'opzione a discesa
  * Aggiunte modalità più chiare Semplice, Offset e Impilato per allineare i bordi, aggiungere spazi precisi e creare pile ordinate
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **Supporto file**
  * Aggiunto il supporto per il formato immagine WEBP nelle operazioni basate su immagini
  * Migliorata l'analisi dei file SVG per importazioni più affidabili

* **Affidabilità**
  * Migliorate la velocità e l'affidabilità di caricamento dei file 3MF
  * Migliore ripristino delle schede tra le sessioni

## Principali correzioni di bug

* **Accesso e Libreria cloud**
  * L'accesso e l'uso della Libreria cloud sono stati ripristinati dopo che un aggiornamento del server backend aveva interrotto l'autenticazione.
  * MatterCAD ora ti chiede di accedere di nuovo quando l'accesso al cloud rileva credenziali scadute o non valide.

* **Selezione nell'albero della scena**
  * Corretto il comportamento incoerente della selezione quando si scelgono oggetti dall'albero della scena.

* **Navigazione della guida**
  * Risolti problemi di navigazione nella guida e nella documentazione delle note di rilascio incluse.

* **Clic destro nella libreria**
  * Corretto il comportamento del clic destro nella vista ad albero della libreria.

* **Fogli**
  * Risolto un arresto anomalo che poteva verificarsi durante il lavoro con i fogli.

---

# MatterCAD 2.2026.3 (12 marzo 2026)
[Download per Windows](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## Nuove funzionalità

* **Nuovissimo motore di rendering Direct3D 11**
  * Migrazione completa da OpenGL a Direct3D 11 per prestazioni nettamente migliori
  * Anti-aliasing FXAA per bordi nitidi e puliti
  * Dual depth peeling per una trasparenza corretta e indipendente dall'ordine
  * Ombre del piano di stampa accelerate via hardware
  * Migliorati i contorni degli oggetti e la resa visiva della selezione
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **Trasparenza degli oggetti**
  * Imposta alfa/trasparenza su qualsiasi singolo oggetto della scena
  * Le mesh con colore per faccia supportano l'alfa senza alterare i colori
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **Blocca e nascondi oggetti**
  * Blocca gli oggetti per evitare selezioni o modifiche accidentali
  * Nascondi gli oggetti per ridurre il disordine visivo mentre lavori su parti specifiche
  * Comandi Mostra tutto e Sblocca tutto per ripristinare rapidamente la visibilità
  * Gli oggetti bloccati e nascosti sono correttamente esclusi dalla selezione tramite raggio
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **Sottrai booleano migliorato**
  * Le operazioni di sottrazione multipla sono molto più affidabili e precise

## Miglioramenti

* **Gestione dei file**
  * I progetti vengono ora salvati per impostazione predefinita in 3MF invece che in STL, conservando colori, materiali e cronologia di progettazione
  * Migliorato il supporto per il trascinamento di file e cartelle nella vista 3D

* **Flusso di lavoro**
  * Le finestre di dialogo Salva con nome e Sposta ricordano l'ultima cartella utilizzata
  * I campi espressione ora supportano `pi`, `tau`, `e` e `count`
  * Il tasto Esc esegue l'annullamento nei contesti di modifica del progetto
  * I controlli 3D restano visibili quando il mouse esce dalla scena

* **Prestazioni e stabilità**
  * Risolti arresti anomali all'avvio e problemi di caricamento ricorsivo
  * Corretti bug di rendering di illuminazione e mipmapping
  * Migliorati gli aggiornamenti della vista ad albero della libreria
  * Calcolo dinamico dei piani near/far per un migliore comportamento dello zoom
  * Aggiornato a .NET 10

---

# MatterCAD 2.2025.6 (20 giugno 2025)
[Download per Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## Nuove funzionalità

* **Supporto File SVG**  
  * Supporto completo per il trascinamento dei file SVG
  * Conversione diretta da grafica SVG a oggetti 3D
  * Integrazione perfetta con i flussi di lavoro CAD esistenti

* **Gestione avanzata dei File OBJ**  
  * Supporto per il caricamento dei materiali da archivi ZIP
  * Analisi dei file OBJ e gestione dei materiali migliorate
  * Migliore supporto per modelli 3D complessi con più materiali

* **Sistema di gestione delle schede migliorato**
  * Le schede della libreria cloud ora persistono correttamente: il tuo lavoro rimane esattamente dove l'hai lasciato
  * Organizzazione e navigazione delle schede migliorate
  * Ripristino automatico delle schede aperte tra le sessioni

## Miglioramenti dell'esperienza utente

* **Interfaccia semplificata**
  * Menu Recenti riorganizzato per un accesso più rapido
  * Migliore feedback visivo durante le operazioni lunghe
  * Migliorati i tempi di avvio e la reattività dell'applicazione

* **Affidabilità**
  * Risolti arresti anomali critici nelle interazioni con la scena 3D
  * Risolti problemi di gestione della memoria
  * Migliorata la stabilità dell'applicazione su tutte le piattaforme

---

# MatterCAD 2.21.5 (13 feb 2025)

[Download per Windows](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# Funzionalità esistenti

*Le seguenti funzionalità rappresentano le fondamenta che MatterCAD eredita da MatterControl:*

* Aggiunta la funzione Cavo  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* Aggiunto Riduci poligoni  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* Aggiunta Ripara mesh  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* Inserito il supporto completamente automatico (supporto legacy) come opzione oltre alla nuova opzione di supporto manuale
* Aggiunto il supporto per gsSlicer (nuovo motore di slicing Sperimentale)
* Corretti bug

## Modifiche

* Migliorata la separazione delle mesh (suddivisione in più mesh)
    * Scarta le facce degeneri
    * Scarta le feature discrete microscopiche

## Modifiche

* Aggiunta la barra di ricerca per l'applicazione
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* Migliorata la barra degli strumenti di progettazione
    * Aggiunto il raggruppamento per alcuni elementi
    * Aggiunto il pulsante di doppio allineamento
    * Aggiunto il pulsante Disponi tutto
* Sposta gli elementi sul piano di stampa con i tasti freccia
* La cartella Download è ordinata per data

## Modifiche

* Miglioramenti dell'interfaccia
    * Aggiornamenti più rapidi nelle cartelle della Libreria cloud
    * Ripristino dell'interfaccia alla riapertura
    * Miglior supporto per la navigazione da tastiera
* Nuovo sistema di rilevamento degli errori e di avviso
    * Gestiti più errori hardware
* Miglioramenti e ottimizzazioni degli strumenti di progettazione
    * Nuovi strumenti Torsione 
    * Strumento Curva migliorato
    * Allinea migliorato


## Modifiche

* Migliorato l'appiattimento
* Migliorato il supporto per l'annullamento
* Migliorata la cronologia di progettazione

## Modifiche
* Versionamento: passaggio a un numero di versione (versione).(anno).(mese). Più facile da leggere e più informativo.
* Nuovi Sottrai, Combina e Intersezione all'avanguardia (solo Windows)
* Ora all'avvio viene mostrato un 'Tour delle funzionalità' per aiutare i nuovi utenti a orientarsi

## Modifiche
* Strumenti di progettazione - La possibilità di modellare in 3D con un set completo di primitive di modellazione
* Usa una primitiva per creare i tuoi supporti personalizzati
* App di progettazione - App di progettazione: progetti sofisticati e personalizzabili
* Elaborazione a 64 bit
