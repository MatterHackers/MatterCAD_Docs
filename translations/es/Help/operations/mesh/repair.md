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

Reparar corrige problemas habituales en la geometría de la malla, como aristas no múltiples, agujeros, orientación de caras inconsistente y vértices casi coincidentes. Resulta especialmente útil para archivos STL y OBJ importados que puedan tener errores.

![20260324 080517 paste 20260324 080517](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080517-paste-20260324-080517.jpg)


## Cómo se usa

1. Seleccione un objeto con problemas de malla
2. Aplique la operación **Reparar** desde el menú Malla
3. Revise las estadísticas de antes y después para ver qué se corrigió

## Estadísticas (solo lectura)

- **Vértices iniciales / Vértices finales** - Número de vértices antes y después de la reparación
- **Caras iniciales / Caras finales** - Número de caras antes y después de la reparación
- **Aristas no múltiples iniciales / Aristas no múltiples finales** - Número de aristas problemáticas antes y después

### Opciones avanzadas

Active el modo **Avanzado** para un control detallado:

- **Soldar vértices** - Combina los vértices casi coincidentes (predeterminado: activado)
- **Tolerancia de soldadura** - Distancia máxima a la que deben estar los vértices para combinarse
- **Orientación de caras** - Voltea las cáscaras invertidas para dejarlas del derecho, de modo que cada cuerpo se interprete como sólido. Cada cáscara se evalúa por separado, así que un modelo hueco conserva sus cavidades en lugar de que se rellenen. Las cáscaras cuyas propias caras no coinciden entre sí se dejan intactas en vez de adivinar su orientación, y los modelos que no son estancos recurren a una reparación más tolerante: ejecute primero **Rellenar agujeros** si la orientación por sí sola no los corrige.
- **Soldar aristas** - Repara pequeñas grietas y costuras defectuosas
- **Rellenar agujeros** - Rellena los huecos en la superficie de la malla
- **Modo de eliminación** - Elimina geometría interna u ocluida:
  - **Ninguno** - Conserva toda la geometría
  - **Interior** - Elimina los cuerpos internos ocultos dentro de la forma principal
  - **Ocluido** - Elimina las caras que no se ven desde el exterior

## Consejos

- Pruebe primero Reparar si las operaciones booleanas (Combinar, Restar) producen resultados inesperados en modelos importados
- La configuración predeterminada (Soldar vértices activado y todo lo demás desactivado) corrige los problemas más habituales
- Active Rellenar agujeros si puede ver a través de huecos en el modelo
- Use Quitar interior para limpiar modelos que tienen geometría oculta en su interior

## Relacionado

- [Decimar](decimate.md) - Reduce el número de polígonos
- [Agregar objetos existentes](../../getting-started/adding-existing-objects.md) - Importe modelos que puedan necesitar reparación
