class User:
    def __init__(self, username, ism, familiya, email, telefon_raqam):
        
        self.username = username
        self.name = ism
        self.surname = familiya
        self.email = email
        self.phone_number = telefon_raqam

    def get_name(self):
        return self.name
    
    def get_username(self):
        return self.username
    
    def get_surname(self):
        return self.surname
    
    def get_emai(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_info(self):
        return f"""Foydalanuvchi: {self.username} \n Ismi: {self.name.title()} {self.surname.title()},  Email: {self.email}, Telefon raqami: {self.phone_number}"""


user1 = User("abroradham", "Abror", "Nematjanov", "abrornematjanov1@gmail.com", +998913450551)
user2 = User("sardor_adhamovich", "Sardor", "nematjanov", "sardoradhamovich@gmail.com", +998882541212)



print(user1.get_info())