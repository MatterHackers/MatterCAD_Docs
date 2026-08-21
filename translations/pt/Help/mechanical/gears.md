---
title: Engrenagens
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Engrenagens

Crie engrenagens 3D com geometria de dentes totalmente configurável. O MatterCAD gera perfis de engrenagem em evolvente adequados, que engrenam corretamente com outras engrenagens de mesmo módulo e ângulo de pressão.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Como Usar

1. Adicione uma **Engrenagem** a partir das ferramentas Mecânico ou do painel Primitivas
2. Defina o número de dentes e os demais parâmetros
3. O perfil da engrenagem é gerado automaticamente

## Parâmetros

### Recursos

- **Tipo de Engrenagem** - Engrenagem Externo ou Cremalheira (barra reta com dentes)
- **Altura** - Espessura da engrenagem (altura de extrusão)
- **Número de Dentes** - Número de dentes ao redor da engrenagem (padrão: 30, faixa: 4-60)
- **Passo Circular** - A distância em arco entre os dentes ao longo do círculo primitivo (faixa: 3-30). Isso determina o tamanho geral.
- **Diâmetro do Furo Central** - Diâmetro do furo central do eixo (padrão: 4mm, defina como 0 para não ter furo). Somente para engrenagens externas.
- **Largura da borda externa** - Largura da borda fora dos dentes internos
- **Número de Dentes da Engrenagem Interna** - Número de dentes da engrenagem interna acoplada

### Avançado

- **Ângulo de Pressão** - O ângulo da superfície de contato do dente (valores comuns: 14,5, 20 ou 25 graus). Todas as engrenagens acopladas devem usar o mesmo ângulo de pressão.
- **Folga** - Espaço mínimo entre a ponta do dente e o vão do dente acoplado
- **Folga** - Espaço mínimo entre os dentes das engrenagens acopladas para evitar travamento

### Dados da Engrenagem (Somente Leitura)

- **Raio Primitivo** - O raio no qual as engrenagens se acoplam entre si
- **Diâmetro externo** - O diâmetro total até a ponta dos dentes

## Dicas

- Duas engrenagens se acoplam corretamente quando possuem o mesmo Passo Circular e Ângulo de Pressão
- Use os valores de Raio Primitivo para espaçar corretamente as engrenagens acopladas -- a distância entre os centros das engrenagens deve ser igual à soma de seus raios primitivos
- Adicione Folga em engrenagens impressas em 3D para compensar as tolerâncias de impressão
- Para perfis de engrenagem 2D (para uso com Extrudar), consulte [Engrenagem 2D](gear-2d.md)

## Relacionados

- [Engrenagem 2D](gear-2d.md) - Caminho de engrenagem 2D para operações de caminho
- [Roscas](threads.md) - Crie recursos rosqueados
