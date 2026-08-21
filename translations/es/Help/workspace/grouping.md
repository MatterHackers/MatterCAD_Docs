---
title: Agrupar
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Agrupar

Agrupar combina varios objetos en una sola unidad que se puede mover, copiar y manipular como un único objeto. A diferencia de [Combinar](../operations/boolean/combine.md), agrupar no fusiona la geometría: cada objeto permanece independiente dentro del grupo.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Cómo se usa

### Agrupar objetos

1. Seleccione dos o más objetos (Mayús+clic o Ctrl+clic para selección múltiple)
2. Haga clic en el botón **Agrupar** de la barra de herramientas
3. Los objetos ya están agrupados: se mueven juntos como una sola unidad

### Desagrupar objetos

1. Seleccione un grupo
2. Haga clic en el botón **Desagrupar** de la barra de herramientas
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Los objetos individuales se restauran como elementos independientes

Al desagrupar también se intenta separar varios cuerpos dentro de un mismo archivo STL importado, si los hubiera.

## Agrupar frente a Combinar

| Característica | Agrupar | Combinar |
|---------|-------|---------|
| Los objetos permanecen independientes | Sí | No |
| Se puede desagrupar después | Sí | No (destructivo) |
| Fusiona la geometría superpuesta | No | Sí |
| Los objetos pueden tener colores distintos | Sí | Colores conservados por cara |
| Caso de uso | Organización y movimiento | Creación de formas sólidas únicas |

## Consejos

- Los grupos se pueden anidar: puede agrupar objetos que ya forman parte de otros grupos
- Seleccione un grupo y consulte el Árbol de diseño para ver y seleccionar los objetos individuales que contiene
- Agrupar no es destructivo y siempre se puede revertir con Desagrupar

## Relacionado

- [Combinar](../operations/boolean/combine.md) - Combinar objetos en un único sólido en lugar de agruparlos
- [Selección](selection.md) - Cómo seleccionar varios objetos para agruparlos
- [Componentes](components.md) - Crear grupos parametrizados reutilizables
