---
title: Taglio con piano
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Taglio con piano

Taglio con piano seziona un oggetto a un'altezza specificata con un piano orizzontale, mantenendo solo la porzione al di sotto del taglio. La superficie di taglio viene chiusa con una faccia piana.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Taglio con piano** dal menu Rimodella
3. Imposta l'altezza di taglio

## Parametri

- **Altezza di taglio** - L'altezza Z alla quale sezionare l'oggetto (predefinito: 10mm, intervallo: 1-200mm)

## Suggerimenti

- Usa Taglio con piano per appiattire la parte superiore di un modello a un'altezza specifica
- Utile per rifilare modelli importati o creare basi piane
- Per tagliare con una forma non planare, usa invece [Sottrai](../boolean/subtract.md) con un altro oggetto
- Per tagliare con un piano inclinato, ruota prima l'oggetto, applica Taglio con piano, quindi ruotalo di nuovo

## Correlati

- [Interseca](../boolean/intersect.md) - Mantieni solo le zone in cui gli oggetti si sovrappongono
- [Sottrai](../boolean/subtract.md) - Taglia con qualsiasi forma, non solo con un piano
- [Svuota](hollow-out.md) - Crea un guscio cavo
