import json  

class VirtualPetCK:
    def __init__(self, nev, ehség=50, szomjuság=50, boldogság=50):
        """A háziállat osztály inicializálása"""
        self.nev = nev
        self.ehség = ehség
        self.szomjuság = szomjuság
        self.boldogság = boldogság

    def feed(self):
        """A háziállat etetése"""
        if self.ehség < 100:
            self.ehség += 10
        self.boldogság += 5
        return f"{self.nev} most evett, éhsége {self.ehség}, boldogsága {self.boldogság}"

    def give_water(self):
        """A háziállat itatása"""
        if self.szomjuság < 100:
            self.szomjuság += 10
        self.boldogság += 3
        return f"{self.nev} most ivott, szomjúsága {self.szomjuság}, boldogsága {self.boldogság}"

    def play(self):
        """A háziállattal való játék"""
        self.boldogság += 20
        self.ehség -= 5
        self.szomjuság -= 5
        return f"{self.nev} most játszott, boldogsága {self.boldogság}, éhsége {self.ehség}, szomjúsága {self.szomjuság}"

    def get_status(self):
        """A háziállat állapotának lekérése"""
        return f"{self.nev} állapota: Éhség: {self.ehség}, Szomjúság: {self.szomjuság}, Boldogság: {self.boldogság}"

    def save_to_file(self):
        """Az állapot elmentése fájlba"""
        with open('pet_data.json', 'w') as file:
            
            data = {
                'nev': self.nev,
                'ehseg': self.ehség,
                'szomjusag': self.szomjuság,
                'boldogsag': self.boldogság
            }
            json.dump(data, file)

    @classmethod
    def load_from_file(cls):
        """Az állapot betöltése fájlból"""
        try:
            with open('pet_data.json', 'r') as file:
                data = json.load(file)
                if 'name' in data:
                    data['nev'] = data.pop('name')
                return cls(**data)
        except FileNotFoundError:
            return None
