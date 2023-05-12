# mehmonlar = ['Aliy', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(mehmon)



# mehmonlar = ['Aliy', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar :
#     print(f"Hurmatli {mehmon} sizni ertaga nahorga oshga taklif qilib qolamiz")
#     print("Hurmat bilan falonchiyevlar oilasi")



# 'for' yordamida sonli ro'yxatlar bilan ishlash;

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")


# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati = [] # bo'sh ro'yxat yaratamiz
# for son in sonlar :
#     sonlar_kvadrati.append(son**2) # uning kv.ni sonlar_kvadrati ga yuklaymiz

# print(sonlar)
# print(sonlar_kvadrati)



# 'for' va 'input'

dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n + 1}-do'stingizning ismini kiriting: "))

print(dostlar)



# Home WoRK

# isimlar = ['Hasan', 'Husan', 'Qobil', 'Nodir', 'Iyso']
# for habar in isimlar :
#     print(f"Salom {habar}")

# print("Kod 5 marotaba takrorlandi")  



# toq_sonlar = list(range(11, 100, 2))
# for kub in toq_sonlar:
#     print(kub**3)


# kitoblar = []
# print("Eng sevimli kitoblariz?")
# for nomi in range(5):
#     kitoblar.append(input(f"{nomi+1}-kitobingizni kiriting: "))
    
# print(kitoblar)




# suhbatdosh = []
# input("Bugun necha kishi bilan suhbatlashdiz? ")
# for isim in range(3):
#     suhbatdosh.append(input(f"{isim +1}-suhbat qilgan odamingiz: "))

# print("suhbatlashilgan insonlar ro'yxati - ", suhbatdosh)
