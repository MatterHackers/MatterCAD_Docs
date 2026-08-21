---
title: Zkroucení
articleKey: TwistObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: 8ea8d2017c16f20dc42b433bcf91815262bb5380
source_lang: en
---
# Zkroucení

Zkroucení otáčí horní část objektu vůči jeho spodní části a vytváří tak podél výšky spirálový nebo zkroucený efekt. Ve výchozím nastavení rotace postupuje rovnoměrně zdola nahoru; v sekci Rozšířené můžete nakreslit, ve které části výšky k otáčení skutečně dochází.

<!--  Before and after showing a cube being twisted into a spiral column -->
![20260506 155620 paste 20260506 155620](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155620-paste-20260506-155620.jpg)

## Jak postupovat

1. Vyberte objekt
2. Použijte operaci **Zkroucení** z nabídky Přetvarovat
3. Nastavte úhel zkroucení a upravte řezy pro dosažení hladkosti
4. Zapněte **Rozšířené**, pokud chcete nakreslit, jak je zkroucení rozloženo po výšce dílu

## Profil zkroucení

V sekci Rozšířené určuje křivka **Profil zkroucení**, kde ke zkroucení dochází. Celkovou míru zkroucení stále nastavuje ovládací prvek Úhel (nebo Vzdálenost rotace) – křivka jej pouze rozloží:

- **Svisle po křivce** je výška na dílu v procentech – 0 dole, 100 nahoře. Vodicí čára napříč editorem označuje 100 procent a je popsána skutečnou výškou dílu v mm.
- **Vodorovně po křivce** je procento celkového zkroucení dosažené v dané výšce – 0 pro žádné, 100 pro celé.

Nové Zkroucení začíná přímou úhlopříčkou z 0 do 100, což je prosté rovnoměrné zkroucení, které dostanete i zcela bez Rozšířené.

Vodorovný úsek křivky je pás dílu, který se nekroutí. Tam, kde křivka nepokrývá celou výšku, se drží její nejbližší konec, takže křivka nakreslená jen mezi 40 a 60 procenty ponechá díl pod ní i nad ní tuhý – tak zkroucení začnete a ukončíte v části výšky.

Úsek, který směrem nahoru klesá, se odvíjí zpět: tento pás dílu se otáčí opačným směrem, zpět k výchozí poloze. Nakreslením profilu nad 100 a poté zpět dolů překročíte celkovou hodnotu a vrátíte se k ní.

## Parametry

- **Typ rotace** – Volba mezi:
  - **Úhel** – Zadejte celkový úhel zkroucení ve stupních (3-360)
  - **Vzdálenost** – Zadejte zkroucení jako vzdálenost po obvodu
- **Řezy** – Počet vodorovných řezů přidaných pro hladké zkroucení, rovnoměrně rozmístěných po výšce dílu. Více řezů = hladší zkroucení
- **Minimální počet stran** – Nejmenší počet stran, které by měl mít díl kolem osy zkroucení. Hrubý tvar, jako je krychle, nemá po svém obvodu geometrii, která by rotaci přenesla, takže se jeho ploché stěny místo zakřivení fasetují; tímto se přidají svislé řezy skrz osu zkroucení, aby tyto stěny mohly zkroucení sledovat. Hodnota 0 (výchozí) ponechá díl beze změny
- **Zkroutit vpravo** – Směr zkroucení: vpravo (po směru hodinových ručiček) nebo vlevo (proti směru hodinových ručiček)
- **Preferovaný radius** – Pouze pro čtení: radius, který díl sám hlásí, nebo ten, který vyplývá z jeho tvaru, a kolem kterého se měří vzdálenost zkroucení (pouze režim Vzdálenost)
- **Upravit radius** – Vypne hlášený radius, abyste mohli nastavit vlastní (pouze režim Vzdálenost a pouze pokud díl nějaký hlásí)
- **Přepsat radius** – Vlastní radius pro výpočet zkroucení (pouze režim Vzdálenost)

### Rozšířené parametry

- **Profil zkroucení** – Výše popsaný editor křivky: procento celkového zkroucení dosažené v každé výšce v procentech
- **Odsazení rotace** – Posune střed, kolem kterého se díl otáčí, mimo střed dílu

## Tipy

- Vyšší hodnoty Řezů poskytují hladší výsledky, ale vytvářejí více geometrie
- Pokud zkroucená krychle nebo jiný tvar s plochými stěnami vypadá spíše fasetovaně než zakřiveně, zvyšte Minimální počet stran
- Nakreslete profil dole vodorovně a teprve poté stoupající, abyste pod zkroucený sloup ponechali rovnou základnu
- Zkroucení o 90 stupňů na hranatém sloupu vytváří elegantní architektonický efekt
- Nakreslete dva vodorovné úseky spojené krátkým stoupáním, abyste zkroutili střed dílu a oba konce ponechali tuhé

## Související

- [Křivka](curve.md) – Ohne objekt do oblouku
- [Zaškrcení](pinch.md) – Stlačení směrem ke středu
- [Radiální stažení](radial-pinch.md) – Tvarování profilu křivkou stejným způsobem
