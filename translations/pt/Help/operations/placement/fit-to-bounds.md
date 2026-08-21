---
title: Ajustar aos Limites
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Ajustar aos Limites

Ajustar aos Limites dimensiona um objeto para caber dentro das medidas especificadas de largura, profundidade e altura. Você pode controlar como o objeto se estica e se alinha dentro dos limites de destino.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Como Usar

1. Selecione um objeto
2. Aplique a operação **Ajustar aos Limites** no menu Posicionamento
3. Insira as dimensões de destino
4. Escolha o bloqueio de proporção e o comportamento de esticamento

## Parâmetros

- **Bloquear Proporção** - Como restringir as proporções:
  - **Nenhum** - Cada eixo pode ser definido de forma independente
  - **X & Y** - Largura e profundidade ficam bloqueadas juntas
  - **X, Y & Z** - Escala uniforme em todos os eixos
- **Largura** - Largura de destino (dimensão X)
- **Profundidade** - Profundidade de destino (dimensão Y)
- **Altura** - Altura de destino (dimensão Z)

### Quando Bloquear Proporção é X & Y ou X, Y & Z

- **Esticar** - Como o objeto se ajusta:
  - **Interno** - Reduz a escala para caber inteiramente dentro dos limites (pode deixar espaços vazios)
  - **Expandir** - Aumenta a escala para preencher os limites (pode exceder em algumas dimensões)

### Quando Bloquear Proporção é Nenhum

Cada eixo tem o seu próprio:

- **Esticar** - Interno ou Expandir por eixo
- **Alinhar** - Onde posicionar dentro dos limites (Mín, Centro, Máx)

## Dicas

- Use este recurso para redimensionar modelos importados para dimensões de destino exatas
- Bloqueie todas as proporções para obter uma escala uniforme que mantenha a forma original
- Use o controle por eixo quando precisar ajustar uma largura específica, mas não se importar com as outras dimensões

## Relacionados

- [Escala](../transform/scale.md) - Dimensione por proporção ou porcentagem em vez de tamanho de destino
- [Ajustar ao Cilindro](fit-to-cylinder.md) - Ajuste dentro de um limite cilíndrico
- [Alinhar](align.md) - Posicione objetos uns em relação aos outros
