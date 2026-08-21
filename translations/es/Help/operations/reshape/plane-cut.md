---
title: Corte por plano
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Corte por plano

Corte por plano secciona un objeto a una altura determinada mediante un plano horizontal, conservando únicamente la parte situada por debajo del corte. La superficie del corte se cierra con una cara plana.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Cómo se usa

1. Selecciona un objeto
2. Aplica la operación **Corte por plano** desde el menú Remodelar
3. Define la altura de corte

## Parámetros

- **Altura de corte** - La altura Z a la que se secciona el objeto (valor predeterminado: 10mm, intervalo: 1-200mm)

## Consejos

- Usa Corte por plano para aplanar la parte superior de un modelo a una altura concreta
- Resulta útil para recortar modelos importados o crear bases planas
- Para cortar con una forma no plana, usa [Restar](../boolean/subtract.md) con otro objeto en su lugar
- Para cortar con un plano inclinado, gira primero el objeto, aplica Corte por plano y después gíralo de vuelta

## Relacionado

- [Intersecar](../boolean/intersect.md) - Conserva solo la zona donde los objetos se superponen
- [Restar](../boolean/subtract.md) - Corta con cualquier forma, no solo con un plano
- [Vaciar](hollow-out.md) - Crea una carcasa hueca
