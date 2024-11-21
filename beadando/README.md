# Háziállat Menedzsment Alkalmazás

Ez az alkalmazás egy virtuális háziállat menedzsment rendszert valósít meg Python és Tkinter segítségével. A felhasználók különböző típusú háziállatokat hozhatnak létre, és interakcióba léphetnek velük (etetés, itatás, játék, alvás). Az alkalmazás figyeli a háziállatok állapotát, és folyamatosan frissíti azokat, miközben lehetőséget biztosít a felhasználók számára a háziállatok kiválasztására és kezelésére.

## Funkciók

- **Háziállat kiválasztás**: A felhasználó kiválaszthat egy háziállatot a listából, és megtekintheti annak aktuális állapotát (név, típus, egészség, boldogság, éhség, szomjúság).
- **Háziállatok létrehozása**: Az alkalmazás lehetőséget ad új háziállatok létrehozására, megadva azok nevét és típusát.
- **Interakciók a háziállatokkal**: 
  - **Etetés**: Csökkenti az éhséget.
  - **Itatás**: Csökkenti a szomjúságot.
  - **Játék**: Növeli a boldogságot.
  - **Alvás**: Helyreállítja az egészséget.
- **Automatikus statisztika frissítés**: Az alkalmazás folyamatosan csökkenti a háziállatok éhségét és szomjúságát, miközben növeli boldogságukat és egészségüket.
- **Állapot mentése**: A háziállatok adatai és állapota fájlba kerülnek mentésre, hogy az alkalmazás következő indításakor elérhetőek legyenek.

Felhasználói felület

    Háziállat kiválasztása: A bal oldalon található listában megjelennek a létrehozott háziállatok. Kattints a kívánt háziállatra, hogy megtekintsd annak adatait.
    Interakciók:
        Etetés: A háziállat éhségét csökkenti.
        Itatás: A háziállat szomjúságát csökkenti.
        Játék: A háziállat boldogságát növeli.
        Alvás: A háziállat egészségét helyreállítja.
    Új háziállat hozzáadása: A "Új háziállat létrehozása" gombra kattintva új háziállatot adhatsz hozzá a listához, ahol megadhatod annak nevét és típusát.

Idő alapú frissítés

Az alkalmazás minden másodpercben frissíti a háziállatok állapotát: csökkenti az éhséget és szomjúságot, miközben növeli a boldogságot és egészséget.
Modulok és Osztályok
pet.py

Ez a modul tartalmazza a háziállatokat reprezentáló osztályokat.
Pet

A Pet osztály a háziállatok alapvető tulajdonságait és viselkedését kezeli, mint például az éhség, szomjúság, boldogság és egészség.

Attribútumok:

    name (str): A háziállat neve.
    type (str): A háziállat típusa (pl. kutya, macska).
    hunger (int): A háziállat éhségi szintje (0-100).
    thirst (int): A háziállat szomjúsági szintje (0-100).
    happiness (int): A háziállat boldogsági szintje (0-100).
    health (int): A háziállat egészségi szintje (0-100).

Metódusok:

    feed(): Csökkenti az éhség szintjét.
    give_water(): Csökkenti a szomjúság szintjét.
    play(): Növeli a boldogság szintjét.
    sleep(): Helyreállítja az egészséget.

Dog és Cat

A Dog és Cat osztályok a Pet osztályból öröklődnek és testre szabják a kutyák és macskák specifikus viselkedését, például az etetés vagy a játékhoz szükséges egyéb paramétereket.
ui.py

Ez a modul felelős az alkalmazás grafikus felhasználói felületének (GUI) kezeléséért.
PetManagerApp

A PetManagerApp osztály az alkalmazás fő GUI-ját képviseli, és kezeli a felhasználói interakciókat.

Attribútumok:

    root: A Tkinter fő ablak objektuma.
    pet_list: A háziállatok listája, amelyet a felhasználó választhat.
    selected_pet: A jelenleg kiválasztott háziállat.

Metódusok:

    create_widgets(): Az összes szükséges GUI elem (gombok, címkék, listák) létrehozása.
    update_pet_info(): A kiválasztott háziállat állapotának frissítése a GUI-n.
    add_new_pet(): Új háziállat hozzáadása a listához.
    interact_with_pet(): A felhasználó által választott interakció végrehajtása (etetés, játék, stb.).

data_storage.py

Ez a modul felelős a háziállatok adatainak mentéséért és betöltéséért fájlokból.
DataStorage

A DataStorage osztály biztosítja a háziállatok adatainak fájlba írását és olvasását.

Metódusok:

    save_data(pets): A háziállatok adatainak mentése.
    load_data(): A háziállatok adatainak betöltése fájlból.

Fejlesztők

    Készítette: czeczó krisztián ádám