---
title: Testo
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Testo

Crea testo 3D estruso con contenuto, carattere, dimensione e altezza personalizzabili. Gli oggetti Testo sono ideali per etichette, insegne, targhette e lettering decorativo.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Come si usa

1. Aggiungi una primitiva **Testo** dal pannello Primitive
2. Digita il tuo testo nel campo **Nome** nel pannello Proprietà
3. Regola il carattere, la dimensione e l'altezza di estrusione secondo necessità

## Parametri

- **Nome** - Il contenuto di testo da visualizzare
- **Dimensione punto** - La dimensione del carattere. È accurata rispetto alle dimensioni di stampa standard: una dimensione di 12 punti in MatterCAD corrisponde a un carattere di 12 punti su una stampante 2D
- **Altezza** - L'altezza di estrusione (quanto il testo sporge dalla superficie)
- **Carattere** - Seleziona tra i caratteri di sistema disponibili

## Suggerimenti

- Usa [Sottrai](../operations/boolean/subtract.md) per incidere il testo in una superficie invece di farlo sporgere
- Per testi molto piccoli, aumenta la Dimensione punto e poi riduci con [Scala](../operations/transform/scale.md) l'intero oggetto per ottenere un dettaglio migliore
- Ogni lettera del testo è un percorso separato che viene estruso insieme agli altri

## Correlati

- [Braille](braille.md) - Genera testo in Braille stampabile in 3D
- [Codice QR](qr-code.md) - Genera un codice QR come oggetto 3D
- [Oggetto Immagine](image-object.md) - Converti immagini in 3D
