# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
  
#     return malumotlar

# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

# print(avto1, avto2)


# def kopaytir(*sonlar):
#     x = 1
#     for n in sonlar:
#         x *= n
        
#     return x


# print(kopaytir(2, 3, 5, 8))



# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar


# malumotlar = []
# while True: 
#     malumotlar.append(avto_info(kompaniya = input('Kampaniyasi: ').upper(), model = input('Modeli: ').title(), rang = input('Rangi? ').title(), yil = int(input('Yili: '))))
    
#     sorov = input('Yana malumot kirirtishni istaysizmi?(yes/no) ')
#     if sorov != 'yes':
#         break
# print(malumotlar)



import random as r
a = ['paper', 'sissors', 'stone']
x = r.choice(a)
y = r.choice(a)


print (x, y,)
