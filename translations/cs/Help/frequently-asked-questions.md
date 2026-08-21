---
title: Často kladené otázky
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Proč mají mé objekty nesprávné měřítko?
- Soubory STL neukládají informace o jednotkách. MatterCAD očekává rozměry STL v milimetrech, zatímco většina CAD softwaru exportuje ve svých nativních jednotkách (obvykle v palcích). To při importu návrhů způsobuje nesrovnalosti v měřítku.

- Nejlepším řešením je nastavit váš návrhový software tak, aby exportoval soubory STL v milimetrech. Například v SolidWorks použijte tlačítko **Možnosti** v dialogu **Uložit jako** a nastavte parametry exportu STL.

- Případně můžete díl přeškálovat přímo v MatterCADu. V 3D zobrazení přejděte do režimu **Upravit** a na pravém panelu nástrojů vyberte MĚŘÍTKO. Použijte rozevírací nabídku s běžnými převodními koeficienty nebo zadejte konkrétní rozměry do polí jednotlivých os.

# Jak vymažu data aplikace?

- Pokud problém nevyřeší ani přeinstalace, může být nutné smazat data uložená aplikací MatterCAD. Tato data zůstávají zachována i po odinstalaci. Chcete-li aplikaci zcela vrátit do výchozího nastavení, odeberte složku aplikace. Můžete také dočasně přejmenovat soubor databáze SQLite (MatterCAD.db) a otestovat tak, zda problémy nezpůsobuje nastavení.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - Uživatelská knihovna a nastavení jsou uloženy v C:\Users\{user}\AppData\Local\MatterCAD.
