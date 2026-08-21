---
title: Hul ut
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Hul ut

Hul ut lager et hult skall av et massivt objekt ved å forskyve overflaten innover. Resultatet er en tynnvegget versjon av den opprinnelige formen.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Slik bruker du den

1. Velg et massivt objekt
2. Bruk operasjonen **Hul ut** fra Endre form-menyen
3. Angi ønsket veggtykkelse

## Parametere

- **Avstand** – Veggtykkelsen i millimeter (standard: 2 mm). Dette er hvor tykt det resulterende skallet blir.
- **Ant. celler** – Oppløsningen til uthulingsalgoritmen (standard: 64). Høyere verdier gir jevnere innvendige overflater, men tar lengre tid å beregne.

## Tips

- Hul ut er nyttig for å lage kabinetter, beholdere, vaser og lette deler
- En veggtykkelse på 1–2 mm er vanlig for de fleste 3D-printede deler
- Øk Ant. celler hvis den innvendige overflaten virker ru eller kantete
- Uthulingen gir en åpen bunn – kombiner med en [Kube](../../primitives/cube.md) hvis du trenger en lukket bunn
- For komplekse former kan beregningen ta noen sekunder

## Relatert

- [Plankutt](plane-cut.md) – Klipp ut et objekt i en bestemt høyde
- [Trekk fra](../boolean/subtract.md) – Skjær bort materiale manuelt
