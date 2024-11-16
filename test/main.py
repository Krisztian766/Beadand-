import tkinter as tk
import json
import time

class VirtualPetCK:
    def __init__(self, name="Pet", hunger=50, thirst=50, happiness=50):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst
        self.happiness = happiness

    def feed(self):
        self.hunger = max(0, self.hunger - 10)

    def give_water(self):
        self.thirst = max(0, self.thirst - 10)

    def play(self):
        self.happiness = min(100, self.happiness + 10)

    def get_status(self):
        return f"{self.name} - Éhség: {self.hunger}, Szomjúság: {self.thirst}, Boldogság: {self.happiness}"

    def to_dict(self):
        """Átalakítja az állatot szótárrá a JSON fájl mentéséhez"""
        return {
            "name": self.name,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "happiness": self.happiness
        }

    @classmethod
    def from_dict(cls, data):
        """Szótárból háziállat objektumot készít"""
        return cls(name=data['name'], hunger=data['hunger'], thirst=data['thirst'], happiness=data['happiness'])

def save_pets(pets):
    """Elmenti a háziállatok listáját a JSON fájlba"""
    with open('pets_data.json', 'w') as file:
        json.dump([pet.to_dict() for pet in pets], file)

def load_pets():
    """Betölti a háziállatok listáját a JSON fájlból"""
    try:
        with open('pets_data.json', 'r') as file:
            pets_data = json.load(file)
            return [VirtualPetCK.from_dict(data) for data in pets_data]
    except FileNotFoundError:
        return []

def feed_pet():
    pet.feed()
    update_status()

def give_water_pet():
    pet.give_water()
    update_status()

def play_pet():
    pet.play()
    update_status()

def show_status():
    status_label.config(text=pet.get_status())

def update_status():
    status_label.config(text=pet.get_status())
    save_pets(pets)  # Frissíti a fájlt minden alkalommal
    check_if_pet_is_dead()  # Ellenőrizzük, hogy meghalt-e az állat

def check_if_pet_is_dead():
    """Ellenőrzi, hogy az állat meghalt-e"""
    if pet.hunger == 0 and pet.thirst == 0 and pet.happiness == 0:
        status_label.config(text=f"{pet.name} meghalt.")
        feed_button.config(state=tk.DISABLED)  # Az összes gombot letiltjuk
        water_button.config(state=tk.DISABLED)
        play_button.config(state=tk.DISABLED)
        status_button.config(state=tk.DISABLED)

def on_closing():
    root.quit()

def change_pet():
    """Új háziállat létrehozása vagy váltása"""
    new_name = name_entry.get()
    if new_name:  # Csak akkor váltunk, ha a név nem üres
        global pet
        pet = VirtualPetCK(name=new_name)
        pets.append(pet)
        save_pets(pets)
        update_status()  # Frissítjük az állapotot

def select_pet():
    """Háziállat kiválasztása a meglévő állatok közül"""
    selected_pet_name = pet_listbox.get(tk.ACTIVE)
    global pet
    pet = next(p for p in pets if p.name == selected_pet_name)
    update_status()

def auto_decrease_status():
    """Automatikusan csökkenti az állat paramétereit 10 percenként"""
    if 'pet' in globals() and pet:  # Ellenőrizzük, hogy a pet változó létezik és nem None
        pet.hunger = min(100, pet.hunger + 5)
        pet.thirst = min(100, pet.thirst + 5)
        pet.happiness = max(0, pet.happiness - 5)
        update_status()
    root.after(600000, auto_decrease_status)  # 10 perc múlva újra hívja

# Tkinter alkalmazás inicializálása
root = tk.Tk()
root.title("Virtuális háziállat")
root.geometry("400x600")

# Háziállatok betöltése
pets = load_pets()

# Listbox a meglévő háziállatok kiválasztásához
pet_listbox = tk.Listbox(root)
for p in pets:
    pet_listbox.insert(tk.END, p.name)
pet_listbox.pack(pady=10)

# Háziállat kiválasztása gomb
select_button = tk.Button(root, text="Háziállat kiválasztása", command=select_pet)
select_button.pack(pady=5)

# Háziállat nevét módosító mező
name_label = tk.Label(root, text="Új háziállat neve:")
name_label.pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Háziállat váltása gomb
change_button = tk.Button(root, text="Háziállat váltása", command=change_pet)
change_button.pack(pady=5)

# Állapot szöveg megjelenítése
status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(pady=10)

# Gombok létrehozása
feed_button = tk.Button(root, text="Etetés", command=feed_pet)
feed_button.pack()

water_button = tk.Button(root, text="Ivás", command=give_water_pet)
water_button.pack()

play_button = tk.Button(root, text="Játék", command=play_pet)
play_button.pack()

status_button = tk.Button(root, text="Állapot", command=show_status)
status_button.pack()

# Alkalmazás bezárása
root.protocol("WM_DELETE_WINDOW", on_closing)

# Ha nincs még kiválasztott állat, akkor hozzunk létre egy alapértelmezett háziállatot
pet = pets[0] if pets else VirtualPetCK(name="Alap háziállat")

# Automatikus állapotfrissítés indítása (10 percenként)
auto_decrease_status()

# Fő ciklus indítása
root.mainloop()
