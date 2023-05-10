# tralaba_0 = {
#     'ism' : 'alijon',
#     'familiya' : 'shamshiyev',
#     'yosh' : 22,
#     'fakultet' : 'matematika',
#     'kurs' : 4
# }
# print(tralaba_0.items())

# for n, m in tralaba_0.items():
#     print(f"Key: {n}")
#     print(f"Value: {m}")


# Keyni o'zini chiqarish uchun

# for n in tralaba_0:
#     print(f"Key: {n}")




# telefonlar = {
#     'ali' : 'iphone x',
#     'vali' : 'galaxy s9',
#     'hasan' : 'me 10pro',
#     'anvar' : 'nokia 3310'
# }

# for n, m in telefonlar.items():
#     print(f"{n.title()}ning telefoni {m}")



# keys() METODI

# mahsulotlar = {
#     'olma' : 10000,
#     'anor' : 20000,
#     'uzum' : 40000,
#     'anjir' : 25000,
#     'shaftoli' : 30000
# }

# print(mahsulotlar.keys())

# print('Do\'konimmizdagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())




# mahsulotlar = {
#     'olma' : 10000,
#     'anor' : 20000,
#     'uzum' : 40000,
#     'anjir' : 25000,
#     'shaftoli' : 30000
# }
# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}so'm")




# mahsulotlar = {
#     'olma' : 10000,
#     'anor' : 20000,
#     'uzum' : 40000,
#     'anjir' : 25000,
#     'shaftoli' : 30000
# }

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for n in bozorlik:
#     if n not in mahsulotlar:
#         print(f"Iltimos do'konga {n}ni ham olib keling ")

# sorted() METODI
# print("Do'konimizgagi mahsulotlar")
# for n in sorted(mahsulotlar):
#     print(n.title())




# .values() METODI

# telefonlar = {
#     'ali' : 'iphone x',
#     'vali' : 'galaxy s9',
#     'hasan' : 'me 10pro',
#     'anvar' : 'nokia 3310'
# }

# print(telefonlar.values())

# print("Foydalanuvxhilar quydagi telefonlarni ishlatishadi")
# for tel in telefonlar.values():
#     print(tel)


# set()  FUNKSIYASI

# telefonlar = {
#     'ali' : 'iphone x',
#     'vali' : 'galaxy s9',
#     'hasan' : 'me 10pro',
#     'anvar' : 'nokia 3310',
#     'jamol' : 'iphone x',
#     'sardor' : 'galaxy A30',
#     'ravshan' : 'iphone x',
#     'ibrohim' : 'me 10pro'
# }

# print('Foydalanuvchilar quydagi telefonlarni ishlatishadi')
# for tel in set(telefonlar.values()):
#     print(tel)


# HOME WORK

# lugat = {
#     'boolean' : 'mantiqiy qiymat',
#     'float' : 'o\'nlik son',
#     'integer' : 'butun son',
#     'string' : 'matn',
#     'for' : 'biror amalni qayta-qayta bajarish tsikli',
#     'if' : 'shartlarni tekshirish operatori'
# }

# soz = input("Istalgan so'z kiriting:")
# a = lugat.get(soz.lower(), "Bunday soz dasturda mavjud emas!")
# print(a)


# for n, m in sorted(lugat.items()):
#     print(f"{n} - {m}")
    





# davlatlar = {
#     'O\'zbekiston' : 'tashkent',
#     'Rassiya' :      'maskva',
#     'Aqsh' :         'washington D.C',
#     'Ispaniya' :     'madrid',
#     'Fransiya' :     'parij',
#     'Suriya' :       'damashq',
#     'Misr' :         'qoxira'
# }  


# # print("Dunyo Davlatlari:    Davlatlarning poytaxti")
# # for davlat, poytaxt in sorted(davlatlar.items()):
# #     print(f"{davlat.title()}                       {poytaxt.title()}")

# a = input("Qaysi davlatni poutaxtini bilishni istaysiz:").capitalize()
# b = davlatlar.get(a, "Bizda bunday malumot yoq")
# print(b)



# menu = {
#     'manti' : 7000,
#     "sho'rva" : 15000,
#     "qotirma" : 14000,
#     'lag\'mon' : 12000,
#     "qozon kabob" : 17000,
#     'osh' : 15000
# }

# zakaz = []
# for n in range(3):
#     zakaz.append(input(f"{n + 1} - zakaz:").lower())

# for a in zakaz:    
#     if a in menu:
#         print(f"{a} - {menu[a]}so'm")
#     else:
#         print(f"{a} bizning menuda mavjud emas") 