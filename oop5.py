from typing import Any
from uuid import uuid4

x = uuid4()

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism.title()
        self.familiya = familiya.title()
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    
    def __repr__(self):
        return f"Talaba: {self.ism.title()} {self.familiya.title()}, Passport - {self.passport}, id - {self.idraqam}"
    
    def __lt__(self, y):
        return self.bosqich<y.bosqich
    
    def __eq__(self, a):
        return self.bosqich == a.bosqich

    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def set_bosqich(self, x):
        self.bosqich += x
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
talaba1_manzil = Manzil(20, "Elobot", "Namangan", "Namangan")
talaba1 = Talaba("Sardor", "Olimov", "FF2340098", 2000, "455a821e-d491-4fe4-ad72-b3df9aa861fc", talaba1_manzil )

talaba2_manzil = Manzil(12, "G'uncha", "Namangan", "Namangan")
talaba2 = Talaba("Axror", "Shamshiyev", "FC7890098", 1998, "91842ebd-b9ea-44f8-88f3-afad29fa4667", talaba2_manzil )
talaba2.set_bosqich(3)

talaba3_manzil = Manzil(3, "Nuriddin", "Namangan", "Namangan")
talaba3 = Talaba("Hoshim", "Axmedov", "AC2345606", 2001, "b972524b-83b9-4a52-ab2c-1d08f4434ffb", talaba3_manzil)


class Fan():
    def __init__(self, nama):
        self.namme = nama
        self.talabalar = []


    def add_student(self, *students):
       for student in students:
         if isinstance(student, Talaba):
            self.talabalar.append(student)
         else:
            print(f"AvtoSalon ga {type(student)} qo`shib bo`lmaydi")


    def __getitem__(self, index):
        return self.talabalar[index]
    
    def __setitem__(self, index, value):
        if isinstance(value, Talaba):
            self.talabalar[index] = value
        else:
            print(f"AvtoSalon ga {type(value)} qo`shib bo`lmaydi")

    def __len__(self):
        return len(self.talabalar)
    
    def __add__(self, talaba):
        if isinstance(talaba, Talaba):
            self.talabalar.append(talaba)
        else:
            print(f"AvtoSalon ga {type(talaba)} qo`shib bo`lmaydi")

    def __sub__(self, talaba):
       if talaba in self.talabalar:
        self.talabalar.remove(talaba)
       else:
         print("Bunday obyekt mavjud emas")

    def __call__(self, *param):
        if param:
            for talaba in param:
                self.talabalar.append(param)
        else:
            return [ talaba for talaba in self.talabalar]

          
    

fan1 = Fan("Matematika")
fan1.add_student(talaba1)
fan1 + talaba2
fan1 + talaba3
