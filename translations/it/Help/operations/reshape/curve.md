---
title: Curva
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Curva

Curva piega un oggetto rettilineo in una forma ad arco o circolare. Puoi controllare la piegatura specificando un angolo oppure un diametro attorno al quale avvolgere l'oggetto.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Curva** dal menu Rimodella
3. Scegli tra il tipo di piegatura Angolo o Diametro
4. Regola i parametri per ottenere la curvatura desiderata

## Parametri

- **Tipo di piegatura** - Scegli tra:
  - **Angolo** - Specifica direttamente l'angolo di piegatura (1-360 gradi)
  - **Diametro** - Specifica il diametro del cerchio attorno al quale si avvolge il pezzo
- **Direzione di piegatura** - Piega verso l'alto o Piega in basso
- **Percentuale iniziale** - Il punto lungo l'oggetto in cui inizia la piegatura (0-100%)
- **Dividi mesh** - Divide la mesh per ottenere curve morbide (predefinito: attivo)
- **Lati min per rotazione** - Numero minimo di segmenti della mesh per ogni rivoluzione completa. Valori più alti = curve più morbide

### Parametri avanzate

- **Percentuale inizio piega** - Percentuale da sinistra in cui inizia la piegatura
- **Percentuale piegatura finale** - Percentuale da sinistra in cui termina la piegatura

## Suggerimenti

- Usa Curva per creare archi, anelli e staffe piegate a partire da forme rettilinee
- Impostando l'angolo a 360 l'oggetto viene avvolto fino a formare un anello completo
- Aumenta Lati min per rotazione per risultati più morbidi nelle piegature strette
- L'oggetto viene piegato lungo la sua lunghezza (asse X)

## Correlati

- [Torsione](twist.md) - Ruota lungo l'altezza invece di piegare
- [Toro](../../primitives/torus.md) - Una forma ad anello già pronta
