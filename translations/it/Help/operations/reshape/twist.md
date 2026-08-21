---
title: Torsione
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Torsione

La Torsione ruota la parte superiore di un oggetto rispetto a quella inferiore, creando un effetto a spirale o attorcigliato lungo l'altezza. Per impostazione predefinita la rotazione progredisce in modo uniforme dal basso verso l'alto; nella sezione Avanzate puoi disegnare in quali punti dell'altezza avviene effettivamente la rotazione.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Torsione** dal menu Rimodella
3. Imposta l'angolo di torsione e regola la suddivisione in sezioni per ottenere un risultato più uniforme
4. Attiva **Avanzate** se vuoi disegnare come la torsione viene distribuita lungo il pezzo

## Il Profilo di torsione

Nella sezione Avanzate, la curva **Profilo di torsione** determina dove avviene la torsione. La quantità totale di torsione è comunque impostata dal controllo Angolo (o Distanza di rotazione): la curva si limita a distribuirla:

- **Lungo la curva** è l'altezza sul pezzo in percentuale: 0 in basso, 100 in alto. Una linea guida che attraversa l'editor segna il 100 percento ed è etichettata con l'altezza reale del pezzo in mm.
- **In orizzontale sulla curva** è la percentuale della torsione totale raggiunta a quell'altezza: 0 per nessuna, 100 per tutta.

Una nuova Torsione inizia con una diagonale retta da 0 a 100, che corrisponde alla semplice torsione uniforme che si ottiene senza usare affatto le Avanzate.

Un tratto piatto nella curva è una fascia del pezzo che non si torce. Dove la curva non copre l'intera altezza, viene mantenuto il valore della sua estremità più vicina, quindi una curva disegnata solo tra il 40 e il 60 percento lascia il pezzo rigido sopra e sotto: è così che si fa iniziare e terminare una torsione a metà altezza.

Un tratto che scende mentre sale svolge la torsione: quella fascia del pezzo ruota nella direzione opposta, tornando verso il punto di partenza. Disegnare il profilo oltre il 100 e poi di nuovo verso il basso è il modo per superare il totale e poi tornarci.

## Parametri

- **Tipo di rotazione** - Scegli tra:
  - **Angolo** - Specifica l'angolo totale di torsione in gradi (3-360)
  - **Distanza** - Specifica la torsione come distanza lungo la circonferenza
- **Sezioni** - Numero di tagli orizzontali aggiunti per una torsione uniforme, distribuiti in modo regolare lungo il pezzo. Più sezioni = torsione più uniforme
- **Lati minimi** - Il numero minimo di lati che il pezzo dovrebbe avere attorno all'asse di torsione. Una forma grossolana come un cubo non ha geometria lungo il perimetro in grado di seguire la rotazione, quindi le sue facce piatte si sfaccettano invece di curvarsi; questo parametro aggiunge tagli verticali attraverso l'asse di torsione affinché quelle facce possano seguire la torsione. 0 (il valore predefinito) lascia il pezzo invariato
- **Torci a destra** - Direzione della torsione: destra (in senso orario) o sinistra (in senso antiorario)
- **Raggio preferito** - Sola lettura: il raggio che il pezzo stesso riporta, oppure quello implicito nella sua forma, che è quello attorno al quale viene misurata una distanza di torsione (solo in modalità Distanza)
- **Modifica raggio** - Disattiva il raggio riportato per poterne impostare uno personalizzato (solo in modalità Distanza e solo quando il pezzo ne riporta uno)
- **Sostituisci raggio** - Raggio personalizzato per il calcolo della torsione (solo in modalità Distanza)

### Parametri avanzati

- **Profilo di torsione** - L'editor di curve descritto sopra: la percentuale della torsione totale raggiunta a ciascuna altezza espressa in percentuale
- **Offset rotazione** - Sposta il centro attorno al quale il pezzo viene ruotato, allontanandolo dal centro del pezzo

## Suggerimenti

- Valori più alti di Sezioni producono risultati più uniformi ma generano più geometria
- Se un cubo torto o un'altra forma con facce piatte appare sfaccettata invece che curva, aumenta i Lati minimi
- Disegna il profilo piatto in basso e crescente dopo quel punto per lasciare una base diritta sotto una colonna torta
- Una torsione di 90 gradi su una colonna quadrata crea un elegante effetto architettonico
- Disegna due tratti piatti uniti da una breve salita per torcere la parte centrale del pezzo e lasciare rigide entrambe le estremità

## Correlati

- [Curva](curve.md) - Piega un oggetto in un arco
- [Restringimento](pinch.md) - Comprimi verso il centro
- [Compressione radiale](radial-pinch.md) - Modella il profilo con una curva nello stesso modo
