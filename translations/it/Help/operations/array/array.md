---
title: Serie
articleKey: ArrayObject3D_2
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c547fa24e5f47e0d60f0cec0eac979700d946daf
source_lang: en
---
# Serie

Serie crea più copie di un oggetto disposte secondo uno schema. Seleziona una modalità dai pulsanti in alto — **Lineare**, **Radiale** o **Trasforma** — per passare da un tipo di schema all'altro.

<!--  Screenshot of the Array operation panel showing the mode buttons at the top (Linear | Radial | Transform) -->
![20260506 080647 paste 20260506 080647](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080647-paste-20260506-080647.jpg)


## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Serie** dal menu Duplicazione
3. Scegli una modalità (Lineare, Radiale o Trasforma)
4. Regola i parametri della modalità scelta

## Modalità: Lineare

La modalità Lineare dispone le copie lungo una direzione con progressione facoltativa di rotazione e scala.

**Quantità** — Numero di copie (intero o espressione). L'oggetto di origine è la prima copia; le copie successive vengono sfalsate rispetto ad esso.

**Metodo offset** — Come viene calcolata la spaziatura:
- **Relativo** — L'offset viene moltiplicato per le dimensioni del riquadro di delimitazione dell'oggetto. Un Offset relativo di (1, 0, 0) distanzia le copie esattamente di una larghezza dell'oggetto lungo X.
- **Offset** — Distanza fissa nello spazio globale in mm per ogni copia.
- **Punto finale** — Imposta la posizione dell'ultima copia; la spaziatura viene suddivisa uniformemente tra le copie.

**Offset relativo** / **Offset** / **Punto finale** — Il vettore di spaziatura, a seconda del Metodo offset selezionato.

**Modalità rotazione** — Come la rotazione si accumula tra le copie:
- **Locale** — Ogni copia ruota sul posto attorno al proprio centro; la direzione dell'offset rimane sugli assi globali.
- **Composizione** — La rotazione si accumula e orienta l'offset, producendo spirali, ventagli ed eliche.

**Rotazione** — Rotazione per copia in gradi su ciascun asse.

**Scala** — Scala cumulativa per copia su ciascun asse. Valori inferiori a 1 rimpiccioliscono le copie; valori superiori a 1 le ingrandiscono.

**La scala influisce sull'offset** — Se attiva, anche la spaziatura tra le copie viene scalata a ogni passo. Utile per spirali che si stringono e progressioni geometriche (conchiglie di nautilus, curve a conchiglia impilate).

## Modalità: Radiale

La modalità Radiale distribuisce le copie in modo uniforme attorno a un asse centrale a un raggio fisso.

<!--  Screenshot of Array in Radial mode showing 6 copies arranged in a circle, with Radius and Central Axis parameters visible -->
![20260506 092618 paste 20260506 092618](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-092618-paste-20260506-092618.jpg)


**Metodo di conteggio** — Come viene determinato il numero di copie:
- **Quantità** — Numero esplicito di copie.
- **Distanza** — Intervallo angolare tra le copie in gradi; la quantità viene calcolata per riempire lo sweep.

**Quantità** / **Distanza angolare** — Numero di copie (modalità Quantità) o spaziatura angolare in gradi (modalità Distanza). Supporta le espressioni.

**Asse centrale** — L'asse attorno a cui ruotare (predefinito: Z).

**Segmento di cerchio** — Indica se le copie occupano un cerchio completo di 360° (**Completo**) oppure un arco parziale (**Arco**).

**Raggio** — Distanza dall'asse centrale a ciascuna copia.

**Angolo di sweep** — Gradi di arco da riempire (visualizzato quando Segmento di cerchio è impostato su Arco). Supporta le espressioni.

**Allinea rotazione** — Ruota ogni copia in modo che il suo asse anteriore punti verso l'esterno rispetto al centro.

**Asse anteriore** — Quale asse della copia viene considerato "anteriore" per l'allineamento (visualizzato quando Allinea rotazione è attivo).

## Modalità: Trasforma

La modalità Trasforma incrementa le copie usando una trasformazione manuale oppure seguendo la trasformazione di un altro oggetto.

**Quantità** — Numero di copie (intero o espressione).

**Riferimento trasformazione** — Da dove proviene la trasformazione di ogni passo:
- **Ingresso** — Specifichi direttamente traslazione, rotazione e scala.
- **Oggetto** — La trasformazione viene letta da un oggetto di pari livello indicato per nome.

**Traslazione** — Offset nello spazio globale per ogni passo in mm (visualizzato quando Riferimento è Ingresso).

**Rotazione** — Rotazione per ogni passo in gradi per asse (visualizzato quando Riferimento è Ingresso).

**Scala** / **Assi di scala** — Scala uniforme e per asse applicata a ogni passo (visualizzato quando Riferimento è Ingresso).

**Nome trasformazione** — Nome dell'oggetto di pari livello la cui trasformazione viene usata come incremento per ogni passo (visualizzato quando Riferimento è Oggetto).

**Spazio relativo** — Se attivo, la trasformazione di ogni copia si compone nel sistema di riferimento locale della copia precedente; se disattivo, ogni passo viene applicato nello spazio globale (visualizzato quando Riferimento è Oggetto).

## Rendi casuale

Attiva **Rendi casuale** per aggiungere variazione a tutte le copie.

- **Offset casuale** — Massimo offset di posizione casuale per asse in mm.
- **Rotazione casuale** — Massima rotazione casuale per asse in gradi.
- **Assi di scala casuale** — Massima variazione di scala casuale per asse.
- **Escludi primo** — Mantiene la prima copia nella sua esatta posizione calcolata (predefinito: attivo).
- **Escludi ultimo** — Mantiene l'ultima copia nella sua esatta posizione calcolata.
- **Seed casuale** — Modificalo per ottenere una disposizione casuale diversa. Supporta le espressioni.

## Unisci

- **Crea mesh singola** — Combina tutte le copie in un unico oggetto mesh unito.
- **Unisci vertici** — Salda i vertici entro la soglia di distanza di unione (visualizzato quando Crea mesh singola è attivo).
- **Distanza** — Soglia di unione in mm (visualizzata quando Unisci vertici è attivo).

## Suggerimenti

- Usa le espressioni per Quantità, Rotazione o Punto finale per creare schemi parametrici
- Per schemi circolari usa la modalità Radiale — imposta il Raggio per controllare la dimensione del cerchio e attiva Allinea rotazione se le copie devono essere rivolte verso l'esterno
- La rotazione con Composizione nella modalità Lineare crea spirali e ventagli senza dover calcolare manualmente gli offset angolari
- La scala influisce sull'offset crea in modo naturale disposizioni a conchiglia di nautilus e a progressione geometrica
- Combina Serie con [Seleziona figlio](select-child.md) per creare schemi in cui ogni copia mostra una variante diversa

## Correlati

- [Allinea](../placement/align.md) - Posiziona gli oggetti l'uno rispetto all'altro
- [Seleziona figlio](select-child.md) - Scegli una copia specifica di una serie per indice o per nome
