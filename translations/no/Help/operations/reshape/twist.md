---
title: Vri
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Vri

Vri roterer toppen av et objekt i forhold til bunnen, og skaper en spiral eller vridd effekt langs høyden. Som standard skjer rotasjonen jevnt fra bunn til topp; under Avansert kan du tegne hvor langs høyden vridningen faktisk skjer.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Slik bruker du den

1. Velg et objekt
2. Bruk **Vri**-operasjonen fra Endre form-menyen
3. Angi vridningsvinkelen og juster oppdelingen for jevnhet
4. Slå på **Avansert** hvis du vil tegne hvordan vridningen fordeles oppover delen

## Vriprofilen

Under Avansert bestemmer **Vriprofil**-kurven hvor vridningen skjer. Den totale vridningsmengden angis fortsatt av kontrollen Vinkel (eller Rotasjonsavstand) – kurven fordeler den bare:

- **Oppover kurven** er høyden på delen i prosent – 0 nederst, 100 øverst. En hjelpelinje tvers over redigeringsvinduet markerer 100 prosent og er merket med delens reelle høyde i mm.
- **Tvers over kurven** er prosenten av den totale vridningen som er nådd ved den høyden – 0 for ingenting av den, 100 for hele.

En ny Vri starter med en rett diagonal fra 0 til 100, som er den vanlige jevne vridningen du får uten Avansert i det hele tatt.

Et flatt parti i kurven er et belte av delen som ikke vris. Der kurven ikke dekker hele høyden, holdes den nærmeste enden av den, så en kurve som bare er tegnet mellom 40 og 60 prosent lar delen være stiv under og over – slik starter og stopper du en vridning et stykke oppe.

Et parti som faller tilbake mens det går oppover, vris opp igjen: det beltet av delen dreier andre veien, tilbake mot der det startet. Å tegne profilen opp forbi 100 og så ned igjen er måten du overskyter totalen og vender tilbake til den på.

## Parametere

- **Rotasjonstype** – Velg mellom:
  - **Vinkel** – Angi den totale vridningsvinkelen i grader (3–360)
  - **Avstand** – Angi vridningen som en avstand langs omkretsen
- **Snitt** – Antall horisontale kutt som legges til for jevn vridning, jevnt fordelt oppover delen. Flere snitt = jevnere vridning
- **Minimum sider** – Det minste antallet sider delen bør ha rundt vridningsaksen. En grov form som en kube har ingen geometri rundt omkretsen til å bære rotasjonen, så de flate flatene blir fasetterte i stedet for buede; dette legger til vertikale kutt gjennom vridningsaksen slik at flatene kan følge vridningen. 0 (standard) lar delen være urørt
- **Vri mot høyre** – Retning på vridningen: høyre (med klokken) eller venstre (mot klokken)
- **Foretrukket radius** – Skrivebeskyttet: radiusen delen selv rapporterer, eller den som følger av formen dens, som er det en vridningsavstand måles rundt (kun i Avstand-modus)
- **Rediger radius** – Slå av den rapporterte radiusen slik at du kan angi din egen (kun i Avstand-modus, og bare når delen rapporterer en)
- **Overstyr radius** – Egendefinert radius for vridningsberegningen (kun i Avstand-modus)

### Avanserte parametere

- **Vriprofil** – Kurveredigeringen beskrevet ovenfor: prosenten av den totale vridningen som er nådd ved hver høyde i prosent
- **Rotasjonsforskyvning** – Flytt senteret delen dreies om, bort fra midten av delen

## Tips

- Høyere verdier for Snitt gir jevnere resultater, men genererer mer geometri
- Hvis en vridd kube eller en annen form med flate sider ser fasettert ut i stedet for buet, øk Minimum sider
- Tegn profilen flat nederst og stigende deretter for å beholde en rett base under en vridd søyle
- En vridning på 90 grader på en firkantet søyle gir en elegant arkitektonisk effekt
- Tegn to flate partier forbundet med en kort stigning for å vri midten av delen og la begge ender være stive

## Relatert

- [Kurve](curve.md) – Bøy et objekt til en bue
- [Klem](pinch.md) – Komprimer mot senter
- [Radiell klemming](radial-pinch.md) – Form profilen med en kurve på samme måte
