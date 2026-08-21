---
title: Adatta ai limiti
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Adatta ai limiti

Adatta ai limiti scala un oggetto affinché rientri nelle dimensioni di larghezza, profondità e altezza specificate. Puoi controllare come l'oggetto si estende e si allinea all'interno dei limiti di destinazione.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Adatta ai limiti** dal menu Posizionamento
3. Inserisci le dimensioni di destinazione
4. Scegli il blocco delle proporzioni e il comportamento di estensione

## Parametri

- **Blocca proporzioni** - Come vincolare le proporzioni:
  - **Nessuno** - Ogni asse può essere impostato in modo indipendente
  - **X e Y** - Larghezza e profondità sono bloccate insieme
  - **X, Y e Z** - Scalatura uniforme su tutti gli assi
- **Larghezza** - Larghezza di destinazione (dimensione X)
- **Profondità** - Profondità di destinazione (dimensione Y)
- **Altezza** - Altezza di destinazione (dimensione Z)

### Quando Blocca proporzioni è X e Y oppure X, Y e Z

- **Estendi** - Come l'oggetto viene adattato:
  - **Interno** - Riduce la scala per rientrare completamente nei limiti (può lasciare spazi vuoti)
  - **Espandi** - Aumenta la scala per riempire i limiti (può eccedere in alcune dimensioni)

### Quando Blocca proporzioni è Nessuno

Ogni asse ha i propri parametri:

- **Estendi** - Interno o Espandi per ciascun asse
- **Allinea** - Dove posizionare l'oggetto all'interno dei limiti (Min, Centro, Max)

## Suggerimenti

- Usa questa operazione per ridimensionare i modelli importati alle dimensioni di destinazione esatte
- Blocca tutte le proporzioni per una scalatura uniforme che mantiene la forma originale
- Usa il controllo per singolo asse quando devi rispettare una larghezza specifica ma le altre dimensioni non sono rilevanti

## Correlati

- [Scala](../transform/scale.md) - Scala in base a un rapporto o a una percentuale anziché a una dimensione di destinazione
- [Adatta al cilindro](fit-to-cylinder.md) - Adatta l'oggetto entro un limite cilindrico
- [Allinea](align.md) - Posiziona gli oggetti l'uno rispetto all'altro
