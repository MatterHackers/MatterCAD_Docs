---
title: Specchia
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Specchia

Specchia crea una copia riflessa di un oggetto rispetto a uno dei tre assi principali. Il risultato è una versione speculare della forma originale.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Specchia** dal menu Trasforma
3. Scegli l'asse rispetto al quale specchiare

## Parametri

- **Specchio attivo** - L'asse rispetto al quale specchiare:
  - **Asse X** - Ribalta l'oggetto da sinistra a destra
  - **Asse Y** - Ribalta l'oggetto da davanti a dietro
  - **Asse Z** - Ribalta l'oggetto dall'alto verso il basso

## Suggerimenti

- Specchia è centrato sul riquadro di delimitazione dell'oggetto, quindi il risultato speculare occupa lo stesso spazio dell'originale
- Le normali delle facce vengono corrette automaticamente dopo la speculatura per mantenere un rendering corretto
- Usa Specchia per creare progetti simmetrici: modella una metà, poi specchiala e usa [Combina](../boolean/combine.md) con l'originale
- Specchia è non distruttivo: puoi cambiare l'asse di specularità in qualsiasi momento

## Correlati

- [Ruota](rotate.md) - Ruota un oggetto invece di specchiarlo
- [Scala](scale.md) - Ridimensiona un oggetto
- [Combina](../boolean/combine.md) - Unisci l'originale e la copia speculare in un unico oggetto
