---
title: Wyrównaj
articleKey: AlignObject3D_3
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 1fadae72ba00cb06e36a21f0b96962dcff3f60ad
source_lang: en
---
# Wyrównaj

Wyrównaj precyzyjnie ustawia wiele obiektów względem obiektu zakotwiczenia. Użyj tej operacji, aby zrównać krawędzie, wyśrodkować części względem siebie, umieścić jeden obiekt na drugim lub utworzyć równomiernie rozmieszczone stosy.

<!--  Screenshot showing two objects being aligned with alignment options visible -->
![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)


## Sposób użycia

1. Wybierz dwa lub więcej obiektów.
2. Zastosuj operację **Wyrównaj** z menu **Rozmieszczenie**.
3. Wybierz obiekt **Zakotwiczenie**. Zakotwiczenie pozostaje na miejscu, a pozostałe obiekty się przesuwają.
4. Ustaw wyrównanie niezależnie dla osi X, Y i Z.
5. Użyj **Zastosuj**, gdy chcesz utrwalić wyrównane pozycje w drzewie obiektów.

## Parametry

### Zakotwiczenie

Lista **Zakotwiczenie** służy do wyboru obiektu podrzędnego używanego jako odniesienie. Zakotwiczenie się nie przesuwa. Każdy inny obiekt podrzędny w operacji Wyrównaj jest przemieszczany względem zakotwiczenia, chyba że dana oś korzysta z trybu **Ułożone w stos**.

### Sterowanie osią

Każda oś ma własne elementy sterowania. Możesz wyrównywać wzdłuż jednej osi, dwóch osi lub wszystkich trzech. Krawędzie minimalna i maksymalna są nazywane zgodnie z osią:

- **Oś X** - Min. to lewa strona, Maks. to prawa strona.
- **Oś Y** - Min. to przód, Maks. to tył.
- **Oś Z** - Min. to dół, Maks. to góra.

Dla każdej osi:

- **Wyrównaj** - Wybiera punkt odniesienia zakotwiczenia dla danej osi. Użyj **Brak**, aby pozostawić pozycje na tej osi bez zmian.
- **Tryb** - Określa sposób zastosowania wybranego wyrównania:
  - **Prosty** - Dopasowuje odpowiadającą krawędź, środek lub początek układu każdego przesuwanego obiektu do zakotwiczenia. Nie jest używane żadne przesunięcie.
  - **Przesunięcie** - Wybierz, która część przesuwanego obiektu ma trafić na punkt odniesienia zakotwiczenia, a następnie dodaj odstęp za pomocą **Przesunięcie**.
  - **Ułożone w stos** - Umieszcza obiekty jeden za drugim wzdłuż danej osi, używając **Przesunięcie** jako odstępu między nimi.
- **Podwyrównanie** - Dostępne w trybie **Przesunięcie**. Wybiera część przesuwanego obiektu, która ma zostać umieszczona na punkcie odniesienia zakotwiczenia. Jeśli **Podwyrównanie** ma wartość **Brak**, operacja Wyrównaj używa tej samej krawędzi, środka lub początku układu, jaki wybrano w **Wyrównaj**.
- **Przesunięcie** - Dostępne w trybach **Przesunięcie** i **Ułożone w stos**. Dodaje odległość wzdłuż danej osi i obsługuje [wyrażenia](../../workspace/expressions.md).

## Tryby wyrównania

### Prosty

Użyj trybu **Prosty**, gdy dopasowujesz odpowiadające sobie pozycje. Na przykład **Wyrównanie X: Środek** przesuwa każdy obiekt niebędący zakotwiczeniem tak, aby jego środek w osi X pokrywał się ze środkiem X zakotwiczenia. **Wyrównanie Z: Min.** przesuwa każdy obiekt niebędący zakotwiczeniem tak, aby jego dół znalazł się na wysokości dołu zakotwiczenia.

### Przesunięcie

Użyj trybu **Przesunięcie**, gdy część przesuwanego obiektu ma być inna niż punkt odniesienia zakotwiczenia. Na przykład, aby umieścić obiekt na wierzchu zakotwiczenia:

1. Ustaw **Wyrównanie Z** na **Maks.** (góra).
2. Ustaw **Tryb Z** na **Przesunięcie**.
3. Ustaw **Podwyrównanie Z** na **Dół**.
4. Ustaw **Przesunięcie Z** na żądany odstęp lub pozostaw wartość `0`, aby uzyskać bezpośredni kontakt.

Dzięki temu dół przesuwanego obiektu znajdzie się na górze zakotwiczenia, z opcjonalnym odstępem.

### Ułożone w stos

Użyj trybu **Ułożone w stos**, aby połączyć wiele obiektów w łańcuch wzdłuż osi. Obiekty są przetwarzane według nazwy, a następnie według wewnętrznego identyfikatora, więc czytelne nazywanie obiektów zapewnia przewidywalną kolejność w stosie.

W trybie **Ułożone w stos** każdy przesuwany obiekt jest umieszczany przy poprzednim odniesieniu na danej osi:

- Wyrównanie **Min.** układa stos w kierunku dodatnim, na przykład od lewej do prawej na osi X lub od dołu do góry na osi Z.
- Wyrównanie **Maks.** układa stos w kierunku ujemnym, na przykład od prawej do lewej na osi X lub od góry do dołu na osi Z.
- Wyrównania **Środek** i **Początek układu** korzystają z przesunięcia między środkami lub początkami układu poszczególnych obiektów.

Użyj **Przesunięcie** w trybie **Ułożone w stos**, aby ustawić odstęp między obiektami.

## Przykłady

- **Wyśrodkowanie obiektów na obrysie stołu** - Wybierz obiekt, który ma pozostać nieruchomy, jako **Zakotwiczenie**, a następnie ustaw **Wyrównanie X** i **Wyrównanie Y** na **Środek**.
- **Umieszczenie jednego obiektu na drugim** - Ustaw **Wyrównanie Z** na **Maks.** (góra), **Tryb Z** na **Przesunięcie**, a **Podwyrównanie Z** na **Dół**.
- **Dodanie precyzyjnego odstępu od krawędzi** - Użyj trybu **Przesunięcie**, wybierz krawędź przesuwanego obiektu za pomocą **Podwyrównanie**, a następnie ustaw **Przesunięcie** na potrzebny odstęp.
- **Ustawienie kilku obiektów jeden za drugim** - Ustaw **Wyrównanie X** na **Min.** (lewa strona), **Tryb X** na **Ułożone w stos** i użyj **Przesunięcie X** do określenia odstępu.
- **Zbudowanie pionowego stosu** - Ustaw **Wyrównanie Z** na **Min.** (dół), **Tryb Z** na **Ułożone w stos** i użyj **Przesunięcie Z** do określenia odstępu między obiektami.

## Wskazówki

- Obiekt zakotwiczenia pozostaje na miejscu; pozostałe obiekty przesuwają się, aby się z nim wyrównać.
- Możesz używać różnych trybów na różnych osiach, na przykład **Ułożone w stos** na osi X oraz **Środek** i **Prosty** na osi Y.
- Użyj nazw obiektów, aby kontrolować kolejność w trybie **Ułożone w stos**, gdy jednocześnie wyrównywanych jest kilka obiektów.
- Operacja Wyrównaj jest nieniszcząca do momentu zastosowania. W dowolnej chwili możesz zmienić ustawienia, aby ponownie wyrównać obiekty podrzędne.
- Użyj **Początek układu**, gdy chcesz zrównać początki układów modelowania zamiast krawędzi obwiedni.

## Powiązane

- [Dopasuj do granic](fit-to-bounds.md) - Skalowanie obiektu do określonych wymiarów
- [Przesuń](../transform/translate.md) - Przesuwanie o określoną odległość
- [Grupowanie](../../workspace/grouping.md) - Grupowanie wyrównanych obiektów, aby utrzymać je razem
