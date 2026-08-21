---
title: Estrusione lineare
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Estrusione lineare

L'Estrusione lineare conferisce altezza a un percorso 2D, trasformando una forma piatta in un solido 3D. È il metodo principale per convertire i percorsi in oggetti 3D.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Come si usa

1. Seleziona un percorso 2D o un oggetto basato su percorso
2. Applica **Estrusione lineare** dal menu delle operazioni Percorso
3. Imposta l'altezza desiderata

## Parametri

- **Altezza** - Quanto è alta l'estrusione (valore predefinito: 5 mm, intervallo: 0,1-50 mm)
- **Smussa in alto** - Aggiunge un bordo smussato (arrotondato) alla parte superiore dell'estrusione (valore predefinito: disattivato)

### Parametri dello smusso (visibili quando Smussa in alto è attivo)

- **Stile** - Il profilo dello smusso (Vivo o arrotondato)
- **Raggio** - Quanto si estende lo smusso in larghezza (valore predefinito: 3 mm)
- **Segmenti** - Levigatezza della curva dello smusso (valore predefinito: 9)

## Suggerimenti

- Funziona con qualsiasi percorso 2D: percorsi [Cerchio](../../2d-paths/circle-path.md), [Riquadro](../../2d-paths/box-path.md), [Stella](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) e [Personalizzato](../../2d-paths/custom-path.md)
- Attiva Smussa in alto per un aspetto più curato e professionale
- Per far ruotare un percorso attorno a un asse invece di estruderlo verso l'alto, vedi [Rivoluzione](revolve.md)

## Correlati

- [Rivoluzione](revolve.md) - Fa ruotare un percorso attorno a un asse
- [Percorsi 2D](../../2d-paths/index.md) - Forme di percorso disponibili
- [Testo](../../primitives/text.md) - Il testo viene estruso automaticamente
