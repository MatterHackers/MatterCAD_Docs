---
title: Editando Objetos
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# Editando Objetos

O MatterCAD oferece controles intuitivos integrados diretamente à vista 3D para mover, rotacionar e escalar seus objetos. Você também pode editar os parâmetros do objeto no painel Propriedades.

## Movendo Peças


- **Arraste sobre a mesa** - Clique e arraste qualquer objeto para deslizá-lo pela superfície do espaço de trabalho
- **Mover para cima e para baixo** - Use o controle de seta vertical no topo de um objeto selecionado para ajustar sua altura (posição Z)
- Para posicionamento preciso, use a operação [Transladar](../operations/transform/translate.md) ou digite valores exatos no painel Propriedades

## Rotacionando Peças

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

Clique em qualquer um dos **controles de canto de rotação** que aparecem quando você seleciona um objeto. Eles permitem rotacionar o objeto no plano daquele controle.

- Passe o mouse sobre um dos indicadores de ângulo para ajustar a rotação em **incrementos de 45 graus**
- Para rotação precisa, use a operação [Rotacionar](../operations/transform/rotate.md) e informe um ângulo exato

## Escalando Peças

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


Clique em qualquer um dos **controles de canto de escala** para redimensionar sua peça no espaço de trabalho.

- Arraste um canto para escalar proporcionalmente
- Para dimensionamento preciso ou escala não uniforme, use a operação [Escala](../operations/transform/scale.md), na qual você pode definir dimensões exatas ou escalar cada eixo de forma independente

## Editando Parâmetros

Quando você seleciona um objeto, seus parâmetros aparecem no painel Propriedades, no lado direito da tela. Por exemplo:

- Um **Cubo** exibe Largura, Profundidade, Altura e controles opcionais de arredondamento
- Um **Cilindro** exibe Diâmetro, Altura e Lados
- Um objeto de **Texto** exibe o conteúdo do texto, a fonte, o tamanho e a altura

Você pode digitar valores diretamente, usar controles deslizantes ou inserir [expressões](../workspace/expressions.md) para criar relações paramétricas.

## Menu de Contexto

Clique com o botão direito em qualquer objeto para acessar opções adicionais, incluindo:

- Copiar, Recortar, Excluir
- Agrupar / Desagrupar
- Operações disponíveis para o objeto selecionado
- Ajuda para o tipo específico de objeto (quando disponível)

## Dicas

- Mantenha **Shift** pressionado ao clicar para selecionar vários objetos e, em seguida, mova-os ou opere sobre eles em conjunto
- Pressione **Ctrl+Z** para desfazer qualquer alteração feita
- Use [Alinhar](../operations/placement/align.md) para posicionar com precisão vários objetos uns em relação aos outros
- Pressione **Espaço** para limpar sua seleção

## Relacionados

- [Navegação na Viewport](viewport-navigation.md) - Como rotacionar, deslocar e aplicar zoom na vista
- [Seleção](../workspace/selection.md) - Comportamento detalhado da seleção
- [Operações de Transformar](../operations/transform/index.md) - Controles precisos de transformação
- [Atalhos de Teclado](../workspace/keyboard-shortcuts.md) - Todos os atalhos disponíveis
