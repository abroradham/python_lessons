# car_0 = {'model' : 'ferrari', 'rangi' : 'qizil' }
# print(car_0['model'])
# print(car_0['rangi'])



# talaba_0 = {'ism' : 'murod olimov', 'yosh' : 20, 't_yil' : 2000}

# # print(f"{talaba_0['ism'].title()},\
# #  {talaba_0['t_yil']} - yilda tug'ilgan,\
# #  {talaba_0['yosh']} yoshda")

# talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
# talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika'

# print(talaba_0)



# BO'SH LUG'AT

# talaba_1 = {}
# talaba_1['ism'] = 'qobil rosulov'
# talaba_1['yosh'] = 20
# talaba_1['kurs'] = 3

# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} - kurs")

# talaba_1['kurs'] = 4 # kursni 4 ga o'zgartiramiz




# KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH

# talaba_0 = {'ism' : 'murod olimov', 'yosh' : 20, 't_yil' : 2000}
# print(talaba_0)
# del talaba_0['yosh'] # 'yosh' degan kalit so'z (va qiymat)ni o'chiramiz
# print(talaba_0)




# LUG'ATNI QATORLARGA BO'LIB YOZISH

# telefonlar = {
#     'ali'  : 'iphone x',
#     'vali' : 'galaxy s9',
#     'olim' : 'mi 10 pro',
#     'orif' : 'nokia 3310' 
#     }

# print(telefonlar)

# phone = telefonlar.get('hasan', 'Bunday ims majud emas')
# print(phine)



# HOME WORK

# 1

# otam = {'ism' : 'adham', 'familiya' : 'Mamadjanov', 'yosh' : 50 }
# onam = {'ism' : 'nasiba', 'familiya' : 'qoriyeva', 'yosh' : 43}
# akam = {'ism' : 'sardor', 'familiya' : 'nematjanov', 'yosh' : 23}

# print(f"Otam {otam['ism'].title()} {otam['familiya'].title()} {otam['yosh']} - yosh")
# print(f"Onam {onam['ism'].title()} {onam['familiya'].title()} {onam['yosh']} - yosh")
# print(f"Akam {akam['ism'].title()} {akam['familiya'].title()} {akam['yosh']} - yosh")




# 2
# taomlar = {
#     'otam' : 'kabob',
#     'onam' : 'sho\'rva',
#     'akam' : "KFC",
#     'singlim' : 'lavash',
#     'men' : 'baliq'
# }

# print(f"Otam {taomlar['otam']} ni yahshi ko'radi")
# print(f"Onam {taomlar['onam']} ni yahshi ko'radi")
# print(f"Akam {taomlar['akam']} ni yahshi ko'radi")



# 3
python = {
    "integer": "butun son",
    "float" : "o\'nlik son",
    'string': "matn",
    'input': 'so\'rov noma',
    'if': 'agar',
    'else': 'aks holda',
    'elif': 'yoki',
    'or': 'yoki',
    'and': 'va',
    }

kalit = input('Biror bir so\'z kiriting:').lower()
print(python.get(kalit, 'Bunday so\'zmavjud emas'))

kalit = input('Biror bir so\'z kiriting:').lower()
tarjima = python.get(kalit)

if tarjima == None:
    print('Bunday so\'z mavjud emas')
else:
    print(f"{kalit.title()} so'zi {tarjima} dep tarjima qilinadi")