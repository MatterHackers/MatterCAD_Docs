---
title: Ruota
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Ruota

Ruota fa girare un oggetto attorno a un asse specificato di un dato angolo. Puoi ruotare attorno a qualsiasi direzione dell'asse e scegliere il punto centrale di rotazione.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Ruota** dal menu Trasforma
3. Imposta l'angolo e l'asse di rotazione nel pannello Proprietà

Puoi anche ruotare gli oggetti direttamente nella vista facendo clic sui controlli di rotazione agli angoli di un oggetto selezionato. Spostando il mouse sugli indicatori dell'angolo, lo scatto avviene a incrementi di 45 gradi.

## Parametri

- **Angolo** - L'angolo di rotazione in gradi (intervallo: 3-360). Supporta le [espressioni](../../workspace/expressions.md).
- **Ruota attorno a** - Definisce l'asse di rotazione e il punto di origine. Puoi ruotare attorno all'asse X, Y o Z, oppure specificare una direzione personalizzata.

## Suggerimenti

- Per impostazione predefinita la rotazione è centrata sul centro del riquadro di delimitazione dell'oggetto
- Per le rotazioni di 90 gradi, gli indicatori di scatto semplificano l'ottenimento di valori esatti
- Usa l'operazione Ruota (anziché i controlli nella vista) quando ti serve un angolo preciso che non sia un multiplo di 45 gradi
- Puoi cambiare l'asse di rotazione dopo aver applicato l'operazione modificando la proprietà Ruota attorno a

## Correlati

- [Trasla](translate.md) - Sposta un oggetto di una distanza specifica
- [Scala](scale.md) - Ridimensiona un oggetto
- [Specchia](mirror.md) - Crea un riflesso speculare
