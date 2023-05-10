# .sort() --- ro'yxatni alifbo ketmaketlikta tartiblash metodi

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)



# .sort(reverse=True) ---- Ro'yxqatni teskari tartibda saqlash argumenti

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)



# print(sorted()) ------ asl ro'yxat ichidagi elementlarning ketmaketligini buzmagan holda ro'yxatni tartiblash funksiyasi

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print ("Sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)



# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))



# Ro'yxatni aylantirish: .reverse()

# fruits = ['pear', 'banana', 'aple', 'watermelon', 'lemon']
# fruits.reverse()
# print(fruits)

# Ro'yxatni uzunligini bilish: len()

# fruits = ['pear', 'banana', 'aple', 'watermelon', 'lemon']
# print("Elementlar soni:", len(fruits))



# range() funktsiyasi

# Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimmiz mumkin
# list() funktsiyasi yordamida esa bu orsliqni ro'yxat shaklida saqlab olamiz:

# sonlar = list(range(0,10))
# print(sonlar)




# range() yordamida qadamni ham berishimmiz mumkin:

# juft_sonlar = list(range(0, 20, 2))
# toq_sonlar = list(range(1,20,2))
# print("Juft sonlar: ", juft_sonlar)
# print("Toq_sonlar: ", toq_sonlar)




# min() --- ro'yxatdagi eng kichig sonni topish
# max() --- ro'yxatdagi eng katta sonni topish
# sum() --- ro'yxatdagi sonlarni yig'indisi

# narhlar = [12000, 15000, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max (narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh - ", arzon)
# print("Eng qimmat narh - ", qimmat)
# print("Jami - ", jami)



# Ro'yxatni kesish

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0 : 3]  # 0 - indexidan boshlab 3 ta element ajratib olamiz
# print(my_cars)

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(cars[ : 4]) # Ro'yxat boshidan 4 gacha kesadi (0, 1, 2, 3)
# print(cars[2 : ]) # 2-elementdan boshlab ro'yxatni oxirigacha kesib oladi



# [:] --- ro'yxatni to'liq ko'chirib oladi

# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar[:] # ro'yxatni to'liq ko'chirib oldi
# sonlar2.append(6)
# sonlar2.append(7)
# print('Bu "sonlar" royxati: ', sonlar)
# print('Bu "sonlar2" ' "ro'yxati", sonlar2)




# TUPLES - O'zgarmas ro'yxat
# Tuple elon qilishlikda "[]" o'rniga "()" ishlatiladi

# tomonlar = (20, 30, 50.2)
# print(tomonlar)

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])




# Tuplega o'zgartirish kiritish uchun "tuple"ni "list"ga o'zgartirvolamiz

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# toys = list(toys)
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqeen'
# toys = tuple(toys)
# print(toys)



# HOMEWORK

# davlatlar = ['Uzbekistan', 'Turkiya', 'Angliya', 'Saudia', 'Italia', 'Siriya']
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)



# juft_sonlar = list(range(120, 1200, 2))
# juft_sonlar = sum(juft_sonlar)
# print(juft_sonlar)
# a = max(juft_sonlar)
# b = min(juft_sonlar)
# print(a - b)

# print(len(juft_sonlar))

# print(juft_sonlar[ : 21])
# print(juft_sonlar[270 :291])
# print(juft_sonlar[520 : 541])
