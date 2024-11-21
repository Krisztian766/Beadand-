import tkinter as tk  # A Tkinter GUI modul importálása
from tkinter import simpledialog  # A beépített simpledialog importálása, hogy egyszerű kérdéseket tegyünk fel
from virtual_pet_ck import load_pets, save_pets, VirtualPetCK  # A háziállat kezeléséhez szükséges funkciók és osztályok importálása
import time  # Az idő kezeléséhez szükséges modul importálása (pl. késleltetésekhez)

# Háziállatok betöltése a fájlból
pets = load_pets()

# GUI beállítások (ablak)
root = tk.Tk()  # Az alap Tkinter ablak létrehozása
root.title("Háziállatok alkalmazás")  # Az ablak címének beállítása

# Kiválasztott háziállat
pet = None  # A kiválasztott háziállat kezdetben 'None'

# Háziállat kiválasztása a listából
def select_pet():
    try:
        selected_pet_name = pet_listbox.get(tk.ACTIVE)  # Az aktívan kiválasztott háziállat neve a listából
        if not selected_pet_name:
            raise ValueError("Nincs kiválasztott háziállat!")  # Ha nincs kiválasztva, hibaüzenet
        global pet
        pet = next(p for p in pets if p.name == selected_pet_name)  # A kiválasztott háziállat keresése
        update_status()  # A kijelző frissítése
    except StopIteration:
        status_label.config(text="Kiválasztott háziállat nem található!")  # Ha nem található, hibaüzenet
    except ValueError as e:
        status_label.config(text=str(e))  # Ha nincs kiválasztott háziállat, hibaüzenet

# Információk frissítése a kijelzőn
def update_status():
    if pet:
        # A háziállat adatai frissülnek a képernyőn
        status_label.config(
            text=f"Név: {pet.name}\nTípus: {pet.type}\nEgészség: {pet.health}\nBoldogság: {pet.happiness}\nÉhség: {pet.hunger}\nSzomjúság: {pet.thirst}")
    else:
        status_label.config(text="Nincs kiválasztott háziállat")  # Ha nincs kiválasztott háziállat, üzenet

# Műveletek végrehajtása a háziállaton
def feed():
    if pet:
        pet.feed()  # A háziállat etetése
        update_status()  # A státusz frissítése
        save_pets(pets)  # A módosítások mentése a fájlba

def water():
    if pet:
        pet.water()  # A háziállat itatása
        update_status()  # A státusz frissítése
        save_pets(pets)  # A módosítások mentése a fájlba

def play():
    if pet:
        pet.play()  # Játék végrehajtása
        update_status()  # A státusz frissítése
        save_pets(pets)  # A módosítások mentése a fájlba

def sleep():
    if pet:
        pet.sleep()  # A háziállat alvása
        update_status()  # A státusz frissítése
        save_pets(pets)  # A módosítások mentése a fájlba

# Új háziállat létrehozása
def create_new_pet():
    name = simpledialog.askstring("Új háziállat neve", "Add meg az új háziállat nevét:")  # A felhasználó nevét kéri
    if not name:
        return  # Ha nincs név, nem történik semmi
    
    type = simpledialog.askstring("Új háziállat típusa", "Add meg az új háziállat típusát:")  # A felhasználó típust kér
    if not type:
        return  # Ha nincs típus, nem történik semmi
    
    # Új háziállat létrehozása alapértelmezett statisztikákkal
    new_pet = VirtualPetCK(name, type, health=100, happiness=100, hunger=0, thirst=0)
    pets.append(new_pet)  # Az új háziállat hozzáadása a listához
    save_pets(pets)  # Az új háziállat mentése
    pet_listbox.insert(tk.END, new_pet.name)  # Az új háziállat neve hozzáadása a listához
    status_label.config(text=f"Új háziállat létrehozva: {new_pet.name}")  # Kijelzi a létrehozott háziállat nevét

# Idő alapú értékcsökkenés (automatikusan csökkenti az értékeket)
def decrease_values():
    if pet:
        # Az éhség és szomjúság nő, a boldogság és egészség csökken
        pet.hunger += 10
        pet.thirst += 10
        pet.happiness -= 10
        pet.health -= 10
        
        # Biztosítjuk, hogy az értékek ne lépjék túl a megengedett határokat
        pet.hunger = min(pet.hunger, 100)  # Az éhség maximális értéke 100
        pet.thirst = min(pet.thirst, 100)  # A szomjúság maximális értéke 100
        pet.happiness = max(pet.happiness, 0)  # A boldogság minimális értéke 0
        pet.health = max(pet.health, 0)  # Az egészség minimális értéke 0
        
        update_status()  # A státusz frissítése
        save_pets(pets)  # Az adatok mentése

    # Új értékcsökkenés 1 másodpercenként
    root.after(1000, decrease_values)  # Újabb értékcsökkentés 1 másodperc múlva

# GUI elemek (felhasználói felület)
pet_listbox = tk.Listbox(root)  # A háziállatok listája
pet_listbox.pack()  # A lista hozzáadása az ablakhoz

# A betöltött háziállatok listájának megjelenítése
for p in pets:
    pet_listbox.insert(tk.END, p.name)  # Minden háziállat nevét hozzáadjuk a listához

# Gombok hozzáadása a GUI-hoz, amelyek különböző műveleteket végeznek
select_button = tk.Button(root, text="Kiválasztás", command=select_pet)  # Háziállat kiválasztása
select_button.pack()

feed_button = tk.Button(root, text="Etetés", command=feed)  # Etetés
feed_button.pack()

water_button = tk.Button(root, text="Itatás", command=water)  # Itatás
water_button.pack()

play_button = tk.Button(root, text="Játék", command=play)  # Játék
play_button.pack()

sleep_button = tk.Button(root, text="Alvás", command=sleep)  # Alvás
sleep_button.pack()

create_button = tk.Button(root, text="Új háziállat létrehozása", command=create_new_pet)  # Új háziállat létrehozása
create_button.pack()

status_label = tk.Label(root, text="Nincs kiválasztott háziállat")  # Státusz kijelző
status_label.pack()

# Elindítjuk az idő alapú értékcsökkenést
decrease_values()  # Az értékek folyamatos csökkentése

root.mainloop()  # A GUI fő ciklusa
