---
title: Reparar
articleKey: RepairObject3D_2
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: f637470dee4f722b595f07d2da9dcdaac5e8da72
source_lang: en
---
# Reparar

O Reparar corrige problemas comuns na geometria da malha, incluindo arestas não manifold, furos, orientação de face inconsistente e vértices quase coincidentes. Isso é especialmente útil para arquivos STL e OBJ importados que possam conter erros.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Como Usar

1. Selecione um objeto com problemas de malha
2. Aplique a operação **Reparar** no menu Malha
3. Analise as estatísticas de antes/depois para ver o que foi corrigido

## Estatísticas (Somente Leitura)

- **Vértices Iniciais / Vértices Finais** - Contagem de vértices antes e depois do reparo
- **Faces Iniciais / Faces Finais** - Contagem de faces antes e depois do reparo
- **Arestas Não manifold Iniciais / Arestas Não manifold Finais** - Contagem de arestas problemáticas antes e depois

### Opções Avançadas

Ative o modo **Avançado** para um controle detalhado:

- **Soldar Vértices** - Mescla vértices quase coincidentes (padrão: ativado)
- **Tolerância de Solda** - Quão próximos os vértices precisam estar para serem mesclados
- **Orientação da Face** - Vira as cascas invertidas para o lado correto, de modo que todo corpo seja interpretado como sólido. Cada casca é avaliada individualmente, portanto um modelo oco mantém suas cavidades em vez de tê-las preenchidas. Cascas cujas próprias faces divergem entre si são deixadas intactas, em vez de serem adivinhadas, e modelos que não são estanques recorrem a um reparo mais tolerante - execute **Preencher Furos** primeiro se a orientação sozinha não os corrigir.
- **Soldar Arestas** - Repara pequenas fissuras e emendas defeituosas
- **Preencher Furos** - Preenche lacunas na superfície da malha
- **Modo Remover** - Remove geometria interna ou oculta:
  - **Nenhum** - Mantém toda a geometria
  - **Interior** - Remove corpos internos escondidos dentro da forma principal
  - **Oculto** - Remove faces bloqueadas para a visão externa

## Dicas

- Experimente o Reparar primeiro se as operações booleanas (Combinar, Subtrair) produzirem resultados inesperados em modelos importados
- As configurações padrão (Soldar Vértices ativado, todo o resto desativado) corrigem os problemas mais comuns
- Ative o Preencher Furos se você conseguir enxergar através de lacunas no modelo
- Use o Remover Interior para limpar modelos que tenham geometria escondida por dentro

## Relacionados

- [Decimar](decimate.md) - Reduz a contagem de polígonos
- [Adicionar Objetos Existentes](../../getting-started/adding-existing-objects.md) - Importe modelos que possam precisar de reparo
