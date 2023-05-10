# ism = input("Ismingiz nima?")
# savol = f"Salom {ism.title()}. Yoshingiz nechida?"
# yosh = input(savol)
# yosh = int(yosh)


# son = 1                    # son ga 1 qiymatini beramiz
# while son<=5:              # toki son 5 dan kichik ekan... 
#     print(son, end=' ')    # son ni konsolga chiqaramiz,
#     son += 1               # songa 1 ni qo'shamiz




# while va input()

# print(f"\nKiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = f"\nIstalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ' '
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print(f"\nDastur to'xtadi!")




# ishora (flag)


# print(f"\nKiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = f"\nIstalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print(f"\nDastur to'xtadi!")





# break OPERATORI

# print(f"\nKiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = f"\nIstalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print(f"\nDastur to'xtadi!")







# continue OPERATORI

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:    
#         continue     # agar son 5 teng bo'lsa uni tashlab o'tib ket
#     else:
#         print(f"{son} kvadrati {son**2} ga teng")




# son = 0
# while son <= 10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son, end=' ')




# HOME WORK

# sorov = "Yoqtirgan kitoblarizzi kiriting:"
# qiymat = ' '
# while qiymat != 'stop':
#     qiymat = input(sorov)
#     if qiymat == 'stop':
#         break
#     else: 
#         print(qiymat.title())






# while True:
#     a = "Ismingizni kiriting:"
#     f = input(a)
#     if f == 'exit' or f == 'quit':
#         break 
#     c = input(f"Salom {f.title()}, yoshingizni kiriting:")
#     if c == 'exit' or c == 'quit':
#         break
#     d = int(c)

#     if d <=7:
#         print('Bilet narhi 2000 so\'m')
#     elif d<=18:
#         print('Bilet narhi 3000 so\'m')
#     elif d<=65:
#         print('Bilet narhi 10000 so\'m')
#     else:
#         print('Siz uchun kirish bepul')
    
    
# print("Dastur to'htatildi")






