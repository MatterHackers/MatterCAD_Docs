---
title: Creare nuovi oggetti
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Creare nuovi oggetti

MatterCAD offre un ricco insieme di strumenti per creare oggetti 3D. Puoi iniziare con forme primitive, usare strumenti specializzati come testo e codici QR, oppure costruire forme complesse con operazioni booleane e serie.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Aggiungere primitive

Il modo più rapido per iniziare un progetto è aggiungere forme primitive. Apri il pannello Primitive nella libreria e fai clic su una forma qualsiasi per aggiungerla all'area di lavoro. Le primitive disponibili includono:

- **Forme di base** - Cubo, Cilindro, Sfera, Cono, Toro, Anello, Piramide, Cuneo e le relative varianti a metà
- **Testo e speciali** - Testo, Braille, Codice QR, Immagine Oggetto, Oggetto SVG

Ogni primitiva ha parametri che puoi regolare nel pannello Proprietà dopo averla selezionata. Ad esempio, un Cubo ha i controlli Larghezza, Profondità e Altezza. Consulta [Primitive](../primitives/index.md) per i dettagli su ciascuna forma.

## La barra degli strumenti delle operazioni

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

La barra degli strumenti nella parte superiore della vista offre un accesso rapido alle operazioni più comuni:

- **Annulla / Ripeti** - Annulla o riapplica le modifiche. Puoi anche usare **Ctrl+Z** per annullare e **Ctrl+Y** per ripetere
- **Raggruppa / Separa** - Combina gli oggetti selezionati in un gruppo che si sposta e opera come una sola unità, oppure scomponi un gruppo
- **Copia / Elimina** - Duplica o rimuovi gli oggetti selezionati. Funzionano anche le scorciatoie standard **Ctrl+C**, **Ctrl+X** e **Ctrl+V**
- **Allinea** - Posiziona più oggetti l'uno rispetto all'altro
- **Operazioni booleane** - [Combina](../operations/boolean/combine.md), [Sottrai](../operations/boolean/subtract.md), [Interseca](../operations/boolean/intersect.md) e [Sottrai e sostituisci](../operations/boolean/subtract-and-replace.md)
- **Serie** - Crea [motivi lineari, radiali, su curva e con trasformazione](../operations/array/array.md) di oggetti duplicati
- **Trasformazioni** - Applica [Ruota](../operations/transform/rotate.md), [Scala](../operations/transform/scale.md), [Specchia](../operations/transform/mirror.md) e altre modifiche

## Costruire forme complesse

La maggior parte dei progetti in MatterCAD si costruisce combinando forme semplici:

1. **Inizia con le primitive** - Aggiungi le forme di base che ti servono
2. **Posizionale** - Sposta e ruota gli oggetti in modo che si sovrappongano dove desideri
3. **Applica le operazioni booleane** - Usa [Combina](../operations/boolean/combine.md) per unire le forme, oppure [Sottrai](../operations/boolean/subtract.md) per ritagliare una forma da un'altra
4. **Rifinisci** - Usa operazioni di [Rimodella](../operations/reshape/index.md) come Smusso, Curva o Torsione per aggiungere dettagli

## Correlati

- [Primitive](../primitives/index.md) - Riferimento completo per tutte le forme primitive
- [Aggiungere oggetti esistenti](adding-existing-objects.md) - Importa file invece di creare da zero
- [Operazioni booleane](../operations/boolean/index.md) - Combina le forme in strutture complesse
- [Modificare gli oggetti](editing-objects.md) - Sposta, ruota e scala gli oggetti dopo averli creati
