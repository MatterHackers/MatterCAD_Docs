---
title: Corte por Plano
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Corte por Plano

O Corte por Plano fatia um objeto em uma altura especificada com um plano horizontal, mantendo apenas a porção abaixo do corte. A superfície cortada é fechada com uma face plana.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Como Usar

1. Selecione um objeto
2. Aplique a operação **Corte por Plano** no menu Remodelar
3. Defina a altura de corte

## Parâmetros

- **Altura de Corte** - A altura Z na qual o objeto será fatiado (padrão: 10 mm, faixa: 1-200 mm)

## Dicas

- Use o Corte por Plano para aplanar o topo de um modelo em uma altura específica
- Útil para aparar modelos importados ou criar bases planas
- Para cortar com uma forma não planar, use [Subtrair](../boolean/subtract.md) com outro objeto
- Para cortar com um plano inclinado, gire o objeto primeiro, aplique o Corte por Plano e depois gire de volta

## Relacionados

- [Intersectar](../boolean/intersect.md) - Mantém apenas onde os objetos se sobrepõem
- [Subtrair](../boolean/subtract.md) - Corta com qualquer forma, não apenas um plano
- [Esvaziar](hollow-out.md) - Cria uma casca oca
