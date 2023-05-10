# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar: # avtolar ichidagi har bir avto uchun ... 
#     if avto == 'bmw': # ... agar avto bmw ga teng bo'lsa
#         print(avto.upper()) # avto nomini hamma hariflarini katta bilan yoz
#     else: # aks holda ....
#         print(avto.title()) # avto nomini faqat birinchi harifini katta bilan yoz



# Matinlarni solishtirish

# isim = 'Aliy'
# print(isim == 'Aliy')
# print(isim =='aliy')
# print(isim.lower() == 'aliy')



# Qiymatlarni teng emasligini tekshirish

# ism = input('Ismingiz nima?\n >>>') #Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'aliy': # Agar ism aliy bo'lmasa
#    print(f"Uzr, {ism.title()} biz Aliyni kutyapmoiz") # Quydagi habar chiqadi
# else:
#    print('Salom Aliy')



# Sonlarni solishtirish

# javob = float(input("""12*6 nechiga teng? 
# >>>>"""))
# if javob !=72:
#     print("Javob xato!")



# yosh = int(input("""Yoshingiz nechida?
# >>>>"""))
# if yosh >= 18:  # yosh 18 dan katta yoki neng bo'lsa
#     print('Xush kelibsiz')
# else : # aks holda
#     print('Kirish mumkin emas!')



# login = input('Yangi login kiriting: ')
# if len(login)<=5: # login uzunligini tekshiramiz
#     print("Login 5 harfda ko'proq bo'lishi shart")



# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2023 - yil < 18: # foydalanuvchining yoshini hisoblaymiz
#     print(f"Yoshingiz {2023-yil}da ekan")
#     print('Kirish mumkin emas!')
# else :
#     print("Xush kelibsiz")




# Bir Qator "if" "else"

# yosh = int(input("Yoshingiz nechida?\n >>>>"))
# if yosh>=65: print("Siz COVID-19 risk gruhida ekansiz")


# x, y = 25, 50 # x = 25, y = 50
# print('x>y') if x>y else print('x<y')



# Home Work

# 1

# cars = ['tayota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())


# 2

# ism = input('Login ismingizni kiriting: ')
# if ism.lower == 'admin':
#     print(f"Hush kelibsiz, {ism.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {ism.title()}")


# 3

# son = int(input("Istalhgan sonni kiriting: "))
# if son > 0 :
#     print("Musbat son!")
# else:
#     print("Manfiy son!")


# 4

# import math # Matematik amallar bajarish

# son = int(input('istalgan son kiriting: '))
# if son > 0:
#     print(math.sqrt(son)) # math.sqrt() -- son ildizini topib beradi
# else:
#     print('Musbat son kiriting')