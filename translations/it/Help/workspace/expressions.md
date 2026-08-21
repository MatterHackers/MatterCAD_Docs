---
title: Espressioni
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Espressioni

Molti parametri in MatterCAD accettano espressioni matematiche invece di semplici numeri. Questo consente una progettazione parametrica in cui la modifica di un valore aggiorna automaticamente le quote correlate.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Come si usa

Invece di digitare un semplice numero in un campo parametro, puoi digitare un'espressione matematica. Ad esempio:

- `20 + 5` dà come risultato 25
- `pi * 10` dà come risultato 31,416
- `width * 2` fa riferimento a un altro parametro chiamato "width"

## Costanti disponibili

- **pi** - 3,14159... (il rapporto tra circonferenza e diametro)
- **tau** - 6,28318... (2 * pi, un giro completo in radianti)

## Operazioni supportate

- Addizione: `+`
- Sottrazione: `-`
- Moltiplicazione: `*`
- Divisione: `/`
- Parentesi: `(` e `)` per raggruppare

## Suggerimenti

- Le espressioni sono supportate in qualsiasi campo che mostri `DoubleOrExpression`, `IntOrExpression` o `StringOrExpression` nel codice: in pratica, la maggior parte dei campi numerici negli strumenti di progettazione le accetta
- Usa le espressioni per creare relazioni tra i parametri: ad esempio, imposta il diametro di un foro su `outer_diameter - 4` in modo che abbia sempre pareti di 2 mm
- Le espressioni si aggiornano automaticamente quando i valori a cui fanno riferimento cambiano
- Usa un [Foglio variabili](variable-sheet.md) quando più oggetti devono condividere gli stessi valori denominati o le stesse formule
- Puoi usare le espressioni nelle operazioni [Serie](../operations/array/index.md) per creare motivi parametrici

## Correlati

- [Componenti](components.md) - Crea progetti parametrizzati riutilizzabili
- [Foglio variabili](variable-sheet.md) - Memorizza valori e formule condivisi per un progetto
- [Modifica degli oggetti](../getting-started/editing-objects.md) - Lavorare con i parametri degli oggetti
