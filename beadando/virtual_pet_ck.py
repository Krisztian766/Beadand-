import json  # JSON fájlok kezelése

# Virtuális háziállat osztálya
class VirtualPetCK:
    # Az osztály inicializálása, itt adhatjuk meg a háziállat adatokat
    def __init__(self, name, type, health, happiness, hunger, thirst):
        self.name = name  # A háziállat neve
        self.type = type  # A háziállat típusa (pl. kutya, macska, stb.)
        self.health = health  # A háziállat egészségi állapota
        self.happiness = happiness  # A háziállat boldogsága
        self.hunger = hunger  # A háziállat éhsége
        self.thirst = thirst  # A háziállat szomjúsága

    # A háziállat etetése, növeli az éhséget
    def feed(self):
        self.hunger = max(self.hunger + 10, 0)  # Éhség csökkentése, de nem mehet negatív érték alá
    
    # A háziállat itatása, növeli a szomjúságot
    def water(self):
        self.thirst = max(self.thirst + 10, 0)  # Szomjúság csökkentése, de nem mehet negatív érték alá
    
    # A háziállat játszik, ami növeli a boldogságot és az egészséget
    def play(self):
        self.happiness = min(self.happiness + 10, 100)  # Boldogság növelése, de nem haladhatja meg a 100-at
        self.health = min(self.health + 5, 100)  # Egészség növelése, de nem haladhatja meg a 100-at
    
    # A háziállat pihen, ami javítja az egészségi állapotát
    def sleep(self):
        self.health = min(self.health + 10, 100)  # Pihenés hatására az egészség növekszik, de nem haladhatja meg a 100-at

    # Objektum létrehozása egy szótárból (json adatból)
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['type'], data['health'], data['happiness'], data['hunger'], data['thirst'])

    # Az objektum adatainak visszaadása szótár formájában (JSON-ba mentéshez)
    def to_dict(self):
        return {
            'name': self.name,  # A háziállat neve
            'type': self.type,  # A háziállat típusa
            'health': self.health,  # A háziállat egészsége
            'happiness': self.happiness,  # A háziállat boldogsága
            'hunger': self.hunger,  # A háziállat éhsége
            'thirst': self.thirst  # A háziállat szomjúsága
        }

# Háziállatok betöltése a JSON fájlból
def load_pets():
    try:
        # Megpróbáljuk megnyitni a 'pets_data.json' fájlt
        with open('pets_data.json', 'r') as file:
            pets_data = json.load(file)  # A fájl tartalmának betöltése JSON formátumban
            if not pets_data:
                return []  # Ha a fájl üres, akkor visszatérünk egy üres listával
            return [VirtualPetCK.from_dict(data) for data in pets_data]  # Visszatérünk a háziállatok listájával
    except (FileNotFoundError, json.JSONDecodeError):
        # Ha a fájl nem található vagy a fájl nem érvényes JSON, üres listát adunk vissza
        return []

# Háziállatok mentése a JSON fájlba
def save_pets(pets):
    with open('pets_data.json', 'w') as file:
        # A háziállatok adatainak mentése a fájlba JSON formátumban
        json.dump([pet.to_dict() for pet in pets], file, indent=4)
