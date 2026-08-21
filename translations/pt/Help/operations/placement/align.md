---
title: Alinhar
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Alinhar

Alinhar posiciona com precisão vários objetos em relação a um objeto âncora. Use-o para alinhar arestas, centralizar peças umas sobre as outras, colocar um objeto sobre outro ou criar pilhas com espaçamento uniforme.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Como Usar

1. Selecione dois ou mais objetos.
2. Aplique a operação **Alinhar** no menu **Posicionamento**.
3. Escolha o objeto **Âncora**. A âncora permanece no lugar e os demais objetos se movem.
4. Defina o alinhamento para os eixos X, Y e Z de forma independente.
5. Use **Aplicar** quando quiser consolidar as posições alinhadas na árvore de objetos.

## Parâmetros

### Âncora

A lista **Âncora** seleciona o objeto filho usado como referência. A âncora não se move. Todos os outros filhos da operação Alinhar são reposicionados em relação à âncora, a menos que um eixo esteja usando o modo **Empilhado**.

### Controles de Eixo

Cada eixo tem seus próprios controles. Você pode alinhar em um eixo, em dois eixos ou nos três. As arestas mínima e máxima recebem o nome do eixo:

- **Eixo X** - Mín é a esquerda, Máx é a direita.
- **Eixo Y** - Mín é a frente, Máx é o fundo.
- **Eixo Z** - Mín é a base, Máx é o topo.

Para cada eixo:

- **Alinhar** - Escolhe o ponto de referência da âncora para aquele eixo. Use **Nenhum** para deixar as posições inalteradas naquele eixo.
- **Modo** - Controla como o alinhamento selecionado é aplicado:
  - **Simples** - Faz a aresta, o centro ou a origem correspondente de cada objeto móvel coincidir com a âncora. Nenhum deslocamento é usado.
  - **Deslocamento** - Escolha qual parte do objeto móvel deve chegar à referência da âncora e depois adicione espaçamento com **Deslocamento**.
  - **Empilhado** - Posiciona os objetos um após o outro ao longo daquele eixo, usando **Deslocamento** como o vão entre eles.
- **SubAlinhar** - Disponível no modo **Deslocamento**. Escolhe a parte do objeto móvel que será posicionada sobre a referência da âncora. Se **SubAlinhar** for **Nenhum**, Alinhar usa a mesma aresta, centro ou origem selecionada em **Alinhar**.
- **Deslocamento** - Disponível nos modos **Deslocamento** e **Empilhado**. Adiciona distância ao longo daquele eixo e aceita [expressões](../../workspace/expressions.md).

## Modos de Alinhamento

### Simples

Use **Simples** ao fazer coincidir posições semelhantes entre si. Por exemplo, **Alinhamento X: Centro** move cada objeto que não é a âncora para que seu centro em X coincida com o centro em X da âncora. **Alinhamento Z: Mín** move cada objeto que não é a âncora para que sua base fique na altura da base da âncora.

### Deslocamento

Use **Deslocamento** quando a parte do objeto móvel precisar ser diferente da referência da âncora. Por exemplo, para colocar um objeto sobre a âncora:

1. Defina **Alinhamento Z** como **Máx** (topo).
2. Defina **Modo Z** como **Deslocamento**.
3. Defina **SubAlinhar Z** como **Inferior**.
4. Defina **Deslocamento Z** com o vão desejado ou deixe em `0` para contato direto.

Isso coloca a base do objeto móvel no topo da âncora, com espaçamento opcional.

### Empilhado

Use **Empilhado** para encadear vários objetos ao longo de um eixo. Os objetos são processados por nome e depois por ID interno, portanto nomeá-los com clareza garante uma ordem de empilhamento previsível.

No modo **Empilhado**, cada objeto móvel é posicionado contra a referência anterior naquele eixo:

- O alinhamento **Mín** empilha na direção positiva, como da esquerda para a direita em X ou de baixo para cima em Z.
- O alinhamento **Máx** empilha na direção negativa, como da direita para a esquerda em X ou de cima para baixo em Z.
- Os alinhamentos **Centro** e **Origem** usam o deslocamento entre o centro ou a origem de cada objeto.

Use **Deslocamento** no modo **Empilhado** para definir o vão entre os objetos.

## Exemplos

- **Centralizar objetos na área da mesa** - Escolha como **Âncora** o objeto que deve permanecer fixo e depois defina **Alinhamento X** e **Alinhamento Y** como **Centro**.
- **Colocar um objeto sobre outro** - Defina **Alinhamento Z** como **Máx** (topo), **Modo Z** como **Deslocamento** e **SubAlinhar Z** como **Inferior**.
- **Adicionar um vão preciso a partir de uma aresta** - Use o modo **Deslocamento**, escolha a aresta do objeto móvel com **SubAlinhar** e depois defina **Deslocamento** com o espaçamento necessário.
- **Alinhar vários objetos ponta a ponta** - Defina **Alinhamento X** como **Mín** (esquerda), **Modo X** como **Empilhado** e use **Deslocamento X** para o vão.
- **Construir uma pilha vertical** - Defina **Alinhamento Z** como **Mín** (base), **Modo Z** como **Empilhado** e use **Deslocamento Z** para o espaço entre os objetos.

## Dicas

- O objeto âncora permanece no lugar; os outros objetos se movem para se alinhar a ele.
- Você pode usar modos diferentes em eixos diferentes, como **Empilhado** em X enquanto usa **Centro** e **Simples** em Y.
- Use os nomes dos objetos para controlar a ordem **Empilhado** quando vários objetos forem alinhados de uma só vez.
- Alinhar é não destrutivo até ser aplicado. Você pode alterar as configurações a qualquer momento para realinhar os filhos.
- Use **Origem** quando precisar alinhar origens de modelagem em vez de arestas da caixa delimitadora.

## Relacionados

- [Ajustar aos Limites](fit-to-bounds.md) - Escale um objeto para se ajustar a dimensões específicas
- [Transladar](../transform/translate.md) - Mova por uma distância específica
- [Agrupamento](../../workspace/grouping.md) - Agrupe objetos alinhados para mantê-los juntos
