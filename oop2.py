class Avto:
    def __init__(self, name, model, rang, karobka, yil):
        self.name = name
        self.model = model
        self.color = rang
        self.karobka = karobka
        self.year = yil
        self.kilometr = 0
        self.price = 0

    def get_info(self):
        x = (f"Nomi: {self.name.title()} Modeli: {self.model.title()}, Rangi: {self.color.title()}," 
            f"Karobka: {self.karobka.title()}, Yili: {self.year}, Kilometri: {self.kilometr}, Narhi: {self.price}$")
        return x
    
    def set_kilometr(self, kilometr):
         self.kilometr = kilometr
    
    def set_price(self,narh):
        self.price = narh
    

class Avto_Salon:
    def __init__(self, name, manzil):
        self.name = name
        self.adress = manzil
        self.sotuvdagi_avtolar = []
        self.sotuvdagi_avtolar_soni = 0

    def get_info_salon(self):
        return f"{self.adress.title()}dagi {self.name.title()} avtosaloni"
    
    def add_avto(self, avto):
        self.sotuvdagi_avtolar_soni += 1
        self.sotuvdagi_avtolar.append(avto)

    def get_name(self,):
        return self.name
    
    def get_avtos(self):
        return [avto.get_info() for avto in self.sotuvdagi_avtolar]
    
    def get_avtolar_soni(self):
        return self.sotuvdagi_avtolar_soni
    

    
avto1 = Avto("Jentra", "Dewo", "qora", "avtomat", 2023)
avto2 = Avto ("Kobalt", "chevrolet", "oq", "mexanika", 2023)

lux = Avto_Salon("Comfort", "Namangan shahar")

lux.add_avto(avto1)
lux.add_avto(avto2)

avto1.set_price(18000)
avto2.set_price(15000)


# print(lux.get_avtos())
print(lux.get_info_salon())