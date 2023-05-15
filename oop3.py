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
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam},"
        return info
    
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
    
    def yozilgan_fanlar(self):
        return [fan.get_fan_info() for fan in self.fanlar]

    def fan_remove(self, fan):
         if fan in self.fanlar:
           self.fanlar.remove(fan)
           return "Fan muvaffaqiyatli o'chirildi."
         else:
           return "Siz bu fanga yozdirilmagansiz."
 
     


    

class Fan ():
    def __init__(self, name):
        self.name = name

    def get_fan_info(self):
        return self.name
    
    def yozilgan_fanlar(self):
        return [fan.get_fan_info() for fan in self.fanlar]



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

matematika = Fan("Matematika")
ingliz_tili = Fan("Ingliz Tili")
fizika  = Fan("Fizika")
biology = Fan("Biology")
chemstry = Fan("Chemstry")

talaba1_manzil = Manzil(44, "Sheroziy", "Honobod", "Namangan")

talaba1 = Talaba("Sherzod", "Ataxanov", "FF1234567,", 2003, "001234F", talaba1_manzil)

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(ingliz_tili)


print(talaba1.yozilgan_fanlar())


