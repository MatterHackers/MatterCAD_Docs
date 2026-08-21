---
title: Criando Novos Objetos
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Criando Novos Objetos

O MatterCAD oferece um rico conjunto de ferramentas para criar objetos 3D. Você pode começar com formas primitivas, usar ferramentas especializadas como texto e códigos QR, ou construir formas complexas usando operações booleanas e matrizes.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Adicionando Primitivas

A maneira mais rápida de iniciar um projeto é adicionando formas primitivas. Abra o painel Primitivas na biblioteca e clique em qualquer forma para adicioná-la ao seu espaço de trabalho. As primitivas disponíveis incluem:

- **Formas básicas** - Cubo, Cilindro, Esfera, Cone, Toro, Anel, Pirâmide, Cunha e suas variantes pela metade
- **Texto e especiais** - Texto, Braille, Código QR, Objeto Imagem, Objeto SVG

Cada primitiva possui parâmetros que você pode ajustar no painel Propriedades após selecioná-la. Por exemplo, um Cubo tem controles de Largura, Profundidade e Altura. Consulte [Primitivas](../primitives/index.md) para detalhes sobre cada forma.

## A Barra de Ferramentas de Operações

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

A barra de ferramentas na parte superior da janela de visualização dá acesso rápido às operações mais comuns:

- **Desfazer / Refazer** - Reverta ou reaplique alterações. Você também pode usar **Ctrl+Z** para desfazer e **Ctrl+Y** para refazer
- **Agrupar / Desagrupar** - Combine os objetos selecionados em um grupo que se move e opera como uma única unidade, ou separe um grupo
- **Copiar / Excluir** - Duplicar ou remover os objetos selecionados. Os atalhos padrão **Ctrl+C**, **Ctrl+X** e **Ctrl+V** também funcionam
- **Alinhar** - Posicione vários objetos uns em relação aos outros
- **Operações booleanas** - [Combinar](../operations/boolean/combine.md), [Subtrair](../operations/boolean/subtract.md), [Intersectar](../operations/boolean/intersect.md) e [Subtrair e Substituir](../operations/boolean/subtract-and-replace.md)
- **Matrizes** - Crie [padrões lineares, radiais, de curva e de transformação](../operations/array/array.md) de objetos duplicados
- **Transformações** - Aplique [Rotacionar](../operations/transform/rotate.md), [Escala](../operations/transform/scale.md), [Espelhar](../operations/transform/mirror.md) e outras modificações

## Construindo Formas Complexas

A maioria dos projetos no MatterCAD é construída combinando formas simples:

1. **Comece com primitivas** - Adicione as formas básicas de que você precisa
2. **Posicione-as** - Mova e rotacione os objetos para que se sobreponham onde você deseja
3. **Aplique operações booleanas** - Use [Combinar](../operations/boolean/combine.md) para mesclar formas, ou [Subtrair](../operations/boolean/subtract.md) para recortar uma forma de outra
4. **Refine** - Use operações de [Remodelar](../operations/reshape/index.md) como Chanfro, Curva ou Torcer para adicionar detalhes

## Relacionados

- [Primitivas](../primitives/index.md) - Referência completa de todas as formas primitivas
- [Adicionando Objetos Existentes](adding-existing-objects.md) - Importe arquivos em vez de criar do zero
- [Operações Booleanas](../operations/boolean/index.md) - Combine formas em formatos complexos
- [Editando Objetos](editing-objects.md) - Mova, rotacione e escale objetos após criá-los
