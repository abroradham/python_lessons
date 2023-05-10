# def yosh_hisobla(t_yil, joriy_yil):
#     """Tug'ilgan yil va Joriy yilni foydalanuvchidan olib,
#        uning yoshini hisoblaydigan funksya """
#     print(f"Siz {joriy_yil - t_yil} yoshda siz")

# tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# j_yil = int(input("Joriy yilni kiriting: "))

# yosh_hisobla(tugilgan_yil, j_yil)




# def hisobla(son):
#     """Foydalanuvchidan son olib 
#        uning kvadirati va kubini hisoblaydigan funksya"""
#     print(f"{son} ning kvadrati - {son**2}")
#     print(f"{son} ning kubi - {son ** 3}")

# a = int(input("Son kiriting: "))
# hisobla(a)




# def hisobla(son):
#     """Foydalanuvchidan son olib, 
#        u son juft yoki to'q ekanligini tekshiruvchi funksya"""
#     if son%2 == 0:
#         print(f"{son} - juft son")
#     else:
#         print(f"{son} - to'q son")

# a = int(input("Son kiriting: "))
# hisobla(a)




# def solishtir(son1, son2):
#     """Foydalanuvchidan son olib
#        qay biri kata ekanligini aniqlovchi funksya"""
#     if son1 > son2:
#         print(son1, '>', son2)
#     elif son2 > son1:
#         print(son2, '>', son1)
#     else:
#         print(f"{son1} = {son2}")

# x = int(input("Son kiriting:"))
# y = int(input("Son kiriting: "))

# solishtir(x,y)




# def bolinish_alomatlari(son):
#     """Foudalanuvchidan son olib, 2 dan 10 gacha qaysi qoldiqsiz bo'linadigan sonlarni aniqlaydigan funksya"""
#     for n in range(2, 11):
#         if son%n == 0 :
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
 

# x = int(input("Son kiriting: "))
# bolinish_alomatlari(x)