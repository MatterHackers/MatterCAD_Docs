---
title: Ingranaggi
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Ingranaggi

Crea ingranaggi 3D con geometria dei denti completamente configurabile. MatterCAD genera profili a evolvente corretti, che ingranano correttamente con altri ingranaggi dello stesso modulo e angolo di pressione.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Come si usa

1. Aggiungi un **Ingranaggio** dagli strumenti Meccanico o dal pannello Primitive
2. Imposta il numero di denti e gli altri parametri
3. Il profilo dell'ingranaggio viene generato automaticamente

## Parametri

### Feature

- **Tipo di ingranaggio** - Ingranaggio Esterno o Cremagliera (barra dritta con denti)
- **Altezza** - Spessore dell'ingranaggio (altezza di estrusione)
- **Numero denti** - Numero di denti lungo la circonferenza dell'ingranaggio (predefinito: 30, intervallo: 4-60)
- **Passo circolare** - La distanza in arco tra i denti lungo la circonferenza primitiva (intervallo: 3-30). Determina la dimensione complessiva.
- **Diametro foro centrale** - Diametro del foro centrale per l'albero (predefinito: 4mm, imposta 0 per non avere il foro). Solo per ingranaggi esterni.
- **Larghezza bordo esterno** - Larghezza del bordo esterno rispetto ai denti interni
- **Numero denti ingranaggio interno** - Numero di denti dell'ingranaggio interno accoppiato

### Avanzate

- **Angolo di pressione** - L'angolo della superficie di contatto del dente (valori comuni: 14.5, 20 o 25 gradi). Tutti gli ingranaggi accoppiati devono usare lo stesso angolo di pressione.
- **Gioco** - Distanza minima tra la testa del dente e il fondo del dente accoppiato
- **Gioco** - Distanza minima tra i denti degli ingranaggi accoppiati per evitare l'impuntamento

### Dati ingranaggio (sola lettura)

- **Raggio primitivo** - Il raggio in corrispondenza del quale gli ingranaggi si accoppiano
- **Diametro esterno** - Il diametro totale fino alla testa dei denti

## Suggerimenti

- Due ingranaggi si accoppiano correttamente quando hanno lo stesso Passo circolare e lo stesso Angolo di pressione
- Usa i valori del Raggio primitivo per distanziare correttamente gli ingranaggi accoppiati: la distanza tra i centri degli ingranaggi deve essere uguale alla somma dei rispettivi raggi primitivi
- Aggiungi Gioco per gli ingranaggi stampati in 3D, per tenere conto delle tolleranze di stampa
- Per i profili di ingranaggio 2D (da usare con Estrudi), vedi [Ingranaggio 2D](gear-2d.md)

## Correlati

- [Ingranaggio 2D](gear-2d.md) - Percorso di ingranaggio 2D per le operazioni su percorso
- [Filetti](threads.md) - Crea feature filettate
