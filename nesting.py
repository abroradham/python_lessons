# car0 = {
#     'model' : 'lacetti',
#     "rang" : 'oq',
#     'yil' : 2018,
#     'narh' : 13000,
#     'km' : 50000,
#     'korobka' : 'avtomat'
#     }

# car1 = {
#     'model' : 'nexia 3',
#     "rang" : 'qora',
#     'yil' : 2015,
#     'narh' : 9000,
#     'km' : 89000,
#     'korobka' : 'mexanika'
#     }


# car2 = {
#     'model' : 'gentra',
#     "rang" : 'qizil',
#     'yil' : 2019,
#     'narh' : 15000,
#     'km' : 20000,
#     'korobka' : 'mexanika'
#     }

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']} - yil, {car['narh']}$")
    
# print(cars[0])
# print(cars[0]['narh'])

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")





# malibus = []
# for n in range(10):
#     new_cars = {
#         'model' : 'malibu',
#         'rang' : None, # rang noaniq
#         'yil' : 2023,
#         'narh' : None, # narh belgilanmagan
#         'km' : 0,
#         'karobka' : 'avto'
#     }
#     malibus.append(new_cars) #yangi lug'atni ro'yxatga qo'shamiz

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'

# for malibu in malibus[3 : 6]:
#     malibu['rang'] = 'qora'

# for malibu in malibus[6 :]:
#     malibu['rang'] = 'qora'
#     malibu['karobka'] = 'mexanika'

# for malibu in malibus:
#     if malibu['karobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 35000

# print(malibus)



# LIG'AT ICHIDA RO'YXAT

# dastuchilar = {
#     'ali' : ['python', 'c++'],
#     'vali' : ['html', 'css', 'js'],
#     'hasan' : ['php', 'sql'],
#     'husan' : ['python', 'php'],
#     'maryam' : ['c++', 'c#']
# }

# for ism, tillar in dastuchilar.items():
#     print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
    
#     for til in tillar:
#         print(f'{til.upper()} ', end='')




# LUG'AT ICHIDAGI LUG'AT

# hamkasblar = {
#     'ali' : {'familiya' : 'valiyev',
#              'tyil' : 1995,
#              'malumot' : 'oliy',
#              'tillar' : ['python', 'c++']},
#     'vali' : {'familiya' : 'aliyev',
#               'tyil' : 2001,
#               'malumot' : 'o\'rta-maxsus',
#               'tillar' : ['html', 'css', 'js']},
#     'hasan' : {'familiya' : 'husanov',
#                'tyil' : 1999,
#                'malumot' : 'maxsus',
#                'tillar' : ['python' , 'php']}
# }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']} - yilda tug'ilgan. "
#           f"Malumoti: {info['malumot']}. \n"
#           'Quydagi dasturlash tillarini biladi:')
#     for til in info['tillar']:
#         print(til.upper())



#  HOME WORK

# shaxs1 = {
#     'ism' : 'Abu Abdulloh Muhammad ibn Ismoil',
#     'tyil' : 810,
#     'tshahar' : 'Buxoro',
#     'umri' : 60
# }

# shaxs2 = {
#     'ism' : 'Abdulla Qodiriy',
#     'tyil' : 1894,
#     'tshahar' : 'Toshkent',
#     'umri' : 44
# }

# shaxs3 = {
#     'ism' : 'Erkin Vohidov',
#     'tyil' : 1936,
#     'tshahar' : "Farg'ona",
#     'umri' : 80,
# }

# shaxs4 = {
#     'ism' : 'Alisher Navoiy',
#     'tyil' : 1441,
#     'tshahar' : 'Xirot',
#     'umri' : 60
# }

# shaxslar =  [shaxs1, shaxs2, shaxs3, shaxs4]

# for shaxs in shaxslar:
#     print(f"{shaxs['ism'].title()} {shaxs['tyil']}-yilda "
#           f"{shaxs['tshahar'].title()}da tavallud topgan. "
#           f"{shaxs['umri']} yil umr ko'rgan.")

# shaxs1['asarlar'] = ['Al - Jome\' as-sahih', 'Al-adab al-mufrad', 'At-tarix al-kabir', 'At-tarix as-sag\'ir']
# shaxs2['asarlar'] = ['O\'tkan kunlar', 'Mehrobdan Chayon', 'Obid ketmon']
# shaxs3['asarlar'] = ['Tong nafasi', 'Qo\'shiqlarim sizga', 'O\'zbegim', 'Qiziquvchan Matmusa']
# shaxs4['asarlar'] = ['Xamsa', 'Lison ut-tayir', 'MAnhub Al-Qulub', 'Munojat']


# for shaxs in shaxslar:
#     print(f"\n{shaxs['ism'].title()} ning mashxur asarlari:")

#     for asar in shaxs['asarlar']:
#         print(asar)




# kinolar_statistikasi = {
#     'Samandar' : ['spiderman', 'betman', 'home alone'],
#     'Ravshan' : ['mafiya', 'qochqin', 'zerkla'],
#     'Kamron' : ['love', 'together', 'discussion']
# }

# for a, b in kinolar_statistikasi.items():
#     print(f"\n{a.title()}ning sevimlik kinolari")

#     for kino in b:
#         print(f'{kino.title()} ',)







# davlatlar = {
#     'O\'zbekiston' : {'poytaxt' : 'Tashkent',
#                       'Hududi' : 448978,
#                       'Aholisi' : 33000000,
#                       'Pul birligi' : 'so\'m'},

#     'Rossiya' : {'poytaxt' : 'Maskva',
#                  'Hududi' : 17098246,
#                  'Aholisi' : 144000000,
#                  'Pul birligi' : 'rubl'},

#     'Aqsh' : {'poytaxt' : 'Washington',
#               'Hududi' : 9631418,
#               'Aholisi' : 327000000,
#               'Pul birligi' : 'dollor'},

#     'Malaziya' : {'poytaxt' : 'Kuala-Lumpur',
#                   'Hududi' : 329750,
#                   'Aholisi' : 25000000,
#                   'Pul birligi' : 'rinngit'}
# }

# # for n, malumot in davlatlar.items():
# #     print (f"\n{n}ning poytaxti {malumot['poytaxt']}"
# #            f"\nHududi: {malumot['Hududi']} kv.km"
# #            f"\nAholisi: {malumot['Aholisi']}"
# #            f"\nPul birligi: {malumot['Pul birligi']}")
    
# sorov = input('Davlat nomini kiriting:').capitalize()
# if sorov in davlatlar:
#     a = davlatlar[sorov]
    
#     print (f"\n{sorov}ning poytaxti {a['poytaxt']}"
#            f"\nHududi: {a['Hududi']} kv.km"
#            f"\nAholisi: {a['Aholisi']}"
#            f"\nPul birligi: {a['Pul birligi']}")
# else:
#     print(f'Bizda bu davlat haqida malumot yoq!')