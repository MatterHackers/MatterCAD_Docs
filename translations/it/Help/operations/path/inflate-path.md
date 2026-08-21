---
title: Gonfia percorso
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Gonfia percorso

Gonfia percorso espande un percorso 2D verso l'esterno, ingrandendo la forma pur mantenendone l'aspetto complessivo. È simile all'applicazione di un offset uniforme a tutti i bordi.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Come si usa

1. Seleziona un percorso 2D
2. Applica **Gonfia percorso** dal menu delle operazioni Percorso
3. Regola il valore di gonfiaggio

## Gonfiare una linea aperta

Gonfia è il modo in cui si trasforma una linea in una forma. Deseleziona **Chiuso** in un [Percorso personalizzato](../../2d-paths/custom-path.md) per disegnare una linea aperta, quindi gonfiala: il risultato è un nastro pieno, largo su entrambi i lati della linea quanto il valore impostato. Da lì si estrude come qualsiasi altro percorso.

**Stile** determina come vengono chiuse le due estremità della linea e come vengono uniti i suoi angoli:

- **Piatto** interrompe il nastro in modo squadrato a ciascun punto finale
- **Arrotonda** aggiunge un semicerchio oltre ciascun punto finale
- **Vivo** aggiunge un quadrato oltre ciascun punto finale

Una linea aperta non ha un interno in cui contrarsi, quindi un valore pari a zero o negativo non lascerebbe assolutamente nulla. Quando il percorso è *interamente* aperto, Gonfia limita il valore a un piccolo numero positivo e riscrive il numero corretto nella casella, così puoi vedere cosa è successo.

Un percorso che combina contorni aperti e chiusi non viene limitato: i contorni chiusi si contraggono normalmente e quelli aperti semplicemente scompaiono. I percorsi chiusi continuano a contrarsi con valori negativi esattamente come hanno sempre fatto.

## Suggerimenti

- Usa valori negativi per contrarre il percorso verso l'interno invece di espanderlo
- Gonfia è utile per creare offset di tolleranza attorno alle forme
- Combina con [Percorso contorno](outline-path.md) per creare bordi di larghezza specifica

## Correlati

- [Percorso contorno](outline-path.md) - Crea un contorno da un percorso
- [Percorso bordo](border-path.md) - Aggiungi un offset del bordo
- [Leviga percorso](smooth-path.md) - Arrotonda gli angoli di un percorso
