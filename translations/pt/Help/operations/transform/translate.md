---
title: Transladar
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# Transladar

Transladar move um objeto por uma distância específica ao longo dos eixos X, Y e/ou Z. Diferentemente de arrastar um objeto com o mouse, Transladar permite inserir valores exatos de deslocamento.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## Como usar

1. Selecione um objeto
2. Aplique a operação **Transladar** no menu Transformar
3. Insira os valores de deslocamento desejados para X, Y e Z no painel Propriedades

## Parâmetros

- **X, Y, Z** (Translação) - A distância para mover o objeto ao longo de cada eixo, em milímetros. Suporta [expressões](../../workspace/expressions.md) para valores calculados.

## Dicas

- Use Transladar quando precisar de um posicionamento preciso e repetível que possa ser ajustado depois
- Os valores de translação são relativos à posição atual do objeto -- inserir 10 em X o move 10mm para a direita a partir de onde ele está
- Para um reposicionamento rápido, você também pode arrastar objetos diretamente na viewport. Consulte [Editando objetos](../../getting-started/editing-objects.md)

## Relacionados

- [Rotacionar](rotate.md) - Rotaciona um objeto por um ângulo específico
- [Escala](scale.md) - Redimensiona um objeto com precisão
- [Alinhar](../placement/align.md) - Posiciona objetos uns em relação aos outros
