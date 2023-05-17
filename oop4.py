from uuid import uuid4
x = uuid4()


class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
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

    __num_talaba = 0
    def __init__(self,ism,familiya,passport,tyil,manzil, ):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
       
        self.bosqich = 1
        self.manzil = manzil
        self.__id = " "
        Talaba.__num_talaba += 1

    @classmethod
    def get_num_talaba(cls):
        return cls.__num_talaba


    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
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
    

talaba1_manzil = Manzil(44, "Sheroziy", "To'raqo'rg'on", "Namangan")
talaba1 = Talaba("Sardor", "Familiya", "FF21310020", 2003, talaba1_manzil,)

talaba2_manzil = Manzil(25, "Alisher Navoyi", "Namangan shahar", "Namangan",)
talaba2 = Talaba("Asror", "Ataxanov", "AA9074565", 2001, talaba2_manzil, )

talaba1.set_id("5778011d-9e7e-4f14-b832-d80fd5d443d4 ")
talaba2.set_id("58eb1bf1-feb7-4b3b-b101-aacddc81564e")

print(talaba2.get_id())
print(Talaba.get_num_talaba())




