---
title: Agrupar
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Agrupar

Agrupar combina vários objetos em uma única unidade que pode ser movida, copiada e manipulada como um só objeto. Ao contrário de [Combinar](../operations/boolean/combine.md), agrupar não mescla a geometria -- cada objeto permanece separado dentro do grupo.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Como Usar

### Agrupando Objetos

1. Selecione dois ou mais objetos (Shift-clique ou Ctrl-clique para seleção múltipla)
2. Clique no botão **Agrupar** na barra de ferramentas
3. Os objetos agora estão agrupados -- eles se movem juntos como uma única unidade

### Desagrupando Objetos

1. Selecione um grupo
2. Clique no botão **Desagrupar** na barra de ferramentas
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Os objetos individuais são restaurados como itens separados

Desagrupar também tenta separar vários corpos dentro de um único arquivo STL importado, se houver.

## Agrupar vs. Combinar

| Recurso | Agrupar | Combinar |
|---------|-------|---------|
| Objetos permanecem separados | Sim | Não |
| Pode desagrupar depois | Sim | Não (destrutivo) |
| Mescla geometria sobreposta | Não | Sim |
| Objetos podem ter cores diferentes | Sim | Cores preservadas por face |
| Caso de uso | Organização e movimentação | Criação de formas sólidas únicas |

## Dicas

- Grupos podem ser aninhados -- você pode agrupar objetos que já estão em grupos
- Selecione um grupo e observe a Árvore de Design para ver e selecionar objetos individuais dentro dele
- Agrupar é não destrutivo e sempre pode ser revertido com Desagrupar

## Relacionados

- [Combinar](../operations/boolean/combine.md) - Mescle objetos em um único sólido em vez de agrupá-los
- [Seleção](selection.md) - Como selecionar vários objetos para agrupar
- [Componentes](components.md) - Crie grupos parametrizados reutilizáveis
