Virtuális háziállat program


Készitő : Czeczó Krisztián



A program egy virtuális háziállatot kezelő alkalmazás, amely lehetővé teszi a felhasználók számára, hogy létrehozzanak, gondozzanak és interakcióba lépjenek egy háziállattal. A program folyamatosan csökkenti az állat szükségleteit (éhség, szomjúság, boldogság) 10 percenként. Ha ezek a paraméterek nullára csökkennek, akkor az állat meghal. A felhasználóknak lehetőségük van választani a meglévő háziállatok közül, vagy új háziállatot létrehozni.



A program a következő modulokat használja:


tkinter: A grafikus felület (GUI) kezelésére szolgáló Python modul, amely lehetővé teszi a felhasználói interakciókat, például gombok kattintását, képek megjelenítését és szövegek frissítését.
PIL (Pillow): A képek kezelésére és megjelenítésére szolgáló könyvtár. A program használja az állat képének betöltésére, átméretezésére és megjelenítésére.
json: A háziállatok adatainak tárolására és betöltésére szolgáló könyvtár. A program a háziállatok nevét és állapotát JSON fájlban tárolja, így az adatok a program újraindítása után is megmaradnak.

Függvények

 `create_pet(name)`

Létrehoz egy új háziállatot a megadott névvel, és alapértelmezett állapotokat (éhség, szomjúság, boldogság) ad hozzá.

 `name`: Az új háziállat neve.

`save_pets_to_file()`

 A programban lévő összes háziállatot JSON fájlba menti.

`load_pets_from_file()`
 Betölti a háziállatokat a `pets_data.json` fájlból.
Visszatérési érték: A háziállatok listája.

`feed_pet()`
Az aktuális háziállatot eteti, csökkentve az éhségét.

`give_water_pet()`

Az aktuális háziállatot itatja, csökkentve a szomjúságát.

 `play_pet()`

 Az aktuális háziállattal játszik, növelve a boldogságát.

`get_status()`

Visszaadja az aktuális háziállat állapotát (éhség, szomjúság, boldogság).
Visszatérési érték: A háziállat állapotát szöveges formában.

 `auto_decrease_status()`

 Automatikusan csökkenti az állat szükségleteit (éhség, szomjúság, boldogság) 10 percenként. Ha minden paraméter nullára csökken, az állat meghal.

 `change_pet()`

 Lehetővé teszi a felhasználó számára, hogy válasszon egy új háziállatot, vagy új háziállatot hozzon létre.

 `on_closing()`
A program bezárásakor a háziállat adatait elmenti.


Használat

A program a felhasználónak lehetőséget ad arra, hogy interakcióba lépjen egy virtuális háziállattal. Az alábbi lehetőségek közül választhat:

 Új háziállat létrehozása: Az "Új háziállat neve" mező kitöltésével, majd a "Háziállat váltása" gomb megnyomásával létrehozhatók új háziállatok.
 Háziállat gondozása:
   - Etetés: A "Etetés" gomb megnyomásával csökkentheted az állat éhségét.
   - Ivás: A "Ivás" gomb megnyomásával csökkentheted az állat szomjúságát.
   - Játék: A "Játék" gomb megnyomásával növelheted az állat boldogságát.
 Állapot megtekintése: A "Állapot" gomb megnyomásával megjelenítheted az aktuális állapotot (éhség, szomjúság, boldogság).
 Automatikus csökkenés: Minden 10 percben automatikusan csökkennek az állat szükségletei.

Mentés és betöltés

A háziállatok adatainak mentésére és betöltésére a `pets_data.json` fájlt használja. A program futtatása közben a háziállatok neve és állapota folyamatosan frissül a fájlban, így a program újraindítása után is megmaradnak az adatok.

