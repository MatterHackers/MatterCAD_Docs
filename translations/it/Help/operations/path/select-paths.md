---
title: Seleziona percorsi
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Seleziona percorsi

Seleziona percorsi filtra quali sotto-percorsi di un oggetto percorso complesso vengono mantenuti. È particolarmente utile quando si lavora con caratteri decorativi o composti da più parti, in cui servono le forme esterne delle lettere e le forme ritagliate interne come pezzi separati — ad esempio per stamparle in 3D in due colori diversi.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Come funziona la profondità del percorso

Quando un oggetto percorso contiene forme con aree racchiuse (come l'interno della lettera "O" o il vuoto di una voluta decorativa), tali aree racchiuse sono **fori** alla profondità 1. Il contorno esterno di ogni lettera o forma si trova alla **profondità 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Preset filtro

### Tutto
Include ogni percorso senza modifiche. È l'impostazione predefinita ed equivale a non applicare affatto Seleziona percorsi.

### Solo percorsi esterni
Mantiene solo il contorno esterno di ogni forma (profondità == 0). Usa questa opzione per ottenere unicamente i contorni delle lettere di un carattere decorativo, senza le aree ritagliate interne.

### Solo fori
Mantiene solo i fori racchiusi (profondità > 0). Usa questa opzione per ottenere unicamente le aree tagliate interne di lettere e forme.

### Per indice gruppo
Mantiene solo i percorsi appartenenti a una singola forma non connessa. Il gruppo 0 è la prima forma, il gruppo 1 la seconda e così via. Usa questa opzione per isolare un singolo carattere all'interno di una parola.

### Personalizzato
Scrivi un'espressione che viene valutata per ogni percorso. Il percorso viene **incluso** quando l'espressione è diversa da zero ed **escluso** quando è uguale a zero.

Le espressioni devono iniziare con `=` per abilitare la sostituzione delle variabili. Senza `=`, il valore viene trattato come un semplice numero (ad esempio, `1` include sempre, `0` esclude sempre).

## Esempi di espressioni personalizzate

| Espressione | Effetto |
|------------|--------|
| `=PathDepth==0` | Solo contorni esterni (come Solo percorsi esterni) |
| `=PathDepth>0` | Solo fori (come Solo fori) |
| `=GroupIndex==0` | Solo la prima forma non connessa |
| `=PathArea>100` | Forme con area maggiore di 100 mm² |
| `=PathLength>50` | Forme con perimetro superiore a 50 mm |

## Variabili delle espressioni personalizzate

| Variabile | Significato |
|----------|---------|
| `PathDepth` | 0 = contorno esterno; 1 o più = foro o forma annidata |
| `GroupIndex` | Indice della forma non connessa (0, 1, 2…) |
| `GroupOuterArea` | Area del percorso esterno di questo gruppo |
| `GroupOuterLength` | Perimetro del percorso esterno di questo gruppo |
| `ChildCount` | Numero di fori all'interno del percorso esterno di questo gruppo |
| `PathIndex` | Indice sequenziale di questo percorso all'interno del suo gruppo |
| `PathArea` | Area di questo singolo percorso |
| `PathLength` | Perimetro di questo singolo percorso |

## Esempio: stampa multicolore con carattere natalizio

Un uso comune di Seleziona percorsi è la stampa di testo decorativo in cui le lettere presentano forme ritagliate interne. Per stampare le lettere esterne in un colore e i tagli interni in un secondo colore:

1. Aggiungi un oggetto **Testo** e impostalo su **output 2D**
2. Applica **Seleziona percorsi** → imposta il preset su **Solo percorsi esterni**
3. Applica **Estrusione lineare** per dargli altezza → assegna il colore del primo filamento
4. Torna all'oggetto testo originale
5. Applica un secondo **Seleziona percorsi** → imposta il preset su **Solo fori**
6. Applica **Estrusione lineare** con la stessa altezza → assegna il colore del secondo filamento
7. Posiziona un oggetto estruso sopra l'altro — i due colori si allineano perfettamente

## Correlati

- [Estrusione lineare](linear-extrude.md) — Dai altezza ai percorsi filtrati per creare un oggetto 3D
- [Rivoluzione](revolve.md) — Fai ruotare i percorsi filtrati attorno a un asse
- [Oggetto SVG](../../primitives/svg-object.md) — Importa percorsi vettoriali che possono contenere più sotto-percorsi
- [Testo](../../primitives/text.md) — Gli oggetti testo in modalità 2D producono un output con più percorsi
