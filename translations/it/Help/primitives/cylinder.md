---
title: Cilindro
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Cilindro

Una forma a colonna circolare con diametro, altezza e numero di lati configurabili. Il Cilindro è fondamentale per creare perni, aste, fori e caratteristiche circolari.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parametri

- **Diametro** - La larghezza del cilindro (predefinito: 20mm)
- **Altezza** - L'altezza del cilindro (predefinito: 20mm)
- **Lati** - Numero di segmenti lungo il perimetro (predefinito: 40). Valori più bassi creano forme poligonali (ad esempio, 6 per un esagono)

### Parametri avanzati

Attiva la modalità **Avanzate** per accedere a controlli aggiuntivi:

- **Diametro superiore** - Imposta un diametro diverso per la parte superiore del cilindro per creare forme rastremate o coni troncati (predefinito: corrisponde al Diametro)
- **Angolo iniziale** - Angolo in cui inizia il cilindro (predefinito: 0). Usalo insieme all'Angolo finale per creare cilindri parziali
- **Angolo finale** - Angolo in cui termina il cilindro (predefinito: 360). Imposta un valore inferiore a 360 per ottenere forme a spicchio

## Suggerimenti

- Imposta i Lati su un numero basso per creare poligoni regolari -- 6 per esagoni, 8 per ottagoni, ecc.
- Usa valori diversi per Diametro e Diametro superiore per creare coni troncati e forme rastremate
- Imposta l'Angolo iniziale e l'Angolo finale per creare forme a spicchio o ad arco
- I cilindri sono ottimi strumenti di taglio per creare fori circolari con [Sottrai](../operations/boolean/subtract.md)

## Correlati

- [Cono](cone.md) - Un cilindro che si rastrema fino a un punto
- [Semicilindro](half-cylinder.md) - Un cilindro tagliato a metà nel senso della lunghezza
- [Anello](ring.md) - Un cilindro cavo (tubo)
