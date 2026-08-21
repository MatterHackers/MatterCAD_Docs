---
title: Raggruppamento
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Raggruppamento

Il raggruppamento combina più oggetti in una singola unità che può essere spostata, copiata e gestita come un unico oggetto. A differenza di [Combina](../operations/boolean/combine.md), il raggruppamento non unisce la geometria: ogni oggetto rimane separato all'interno del gruppo.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Come si usa

### Raggruppare gli oggetti

1. Seleziona due o più oggetti (Shift-clic o Ctrl-clic per la selezione multipla)
2. Fai clic sul pulsante **Raggruppa** nella barra degli strumenti
3. Gli oggetti sono ora raggruppati: si spostano insieme come un'unica unità

### Separare gli oggetti

1. Seleziona un gruppo
2. Fai clic sul pulsante **Separa** nella barra degli strumenti
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. I singoli oggetti vengono ripristinati come elementi separati

L'operazione Separa tenta anche di separare più corpi presenti all'interno di un singolo file STL importato, se presenti.

## Raggruppa e Combina a confronto

| Caratteristica | Raggruppa | Combina |
|---------|-------|---------|
| Gli oggetti rimangono separati | Sì | No |
| È possibile separarli in seguito | Sì | No (distruttivo) |
| Unisce le geometrie sovrapposte | No | Sì |
| Gli oggetti possono avere colori diversi | Sì | Colori conservati per faccia |
| Caso d'uso | Organizzazione e spostamento | Creazione di forme solide uniche |

## Suggerimenti

- I gruppi possono essere annidati: puoi raggruppare oggetti che fanno già parte di gruppi
- Seleziona un gruppo e osserva l'albero di progettazione per vedere e selezionare i singoli oggetti al suo interno
- Il raggruppamento non è distruttivo e può sempre essere annullato con Separa

## Correlati

- [Combina](../operations/boolean/combine.md) - Unisci gli oggetti in un unico solido anziché raggrupparli
- [Selezione](selection.md) - Come selezionare più oggetti da raggruppare
- [Componenti](components.md) - Crea gruppi parametrizzati riutilizzabili
