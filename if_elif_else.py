# yosh = int(input("Yoshingiz nechida? "))
# if yosh<=4 :
#     print('Sizga kikrish bepul')
# elif yosh<=12 :
#     print("Sizga kirish 5000 so'm")
# else :
#     print("Sizga kirish 10000 so'm")


# Yuqoridagi kodni qisqacha ko'rinishi
#         ||
#         \/

# yosh = int(input("Yoshingiz nechida? "))
# if yosh<=4 :
#     price = 0
# elif yosh<=12 :
#     price = 5000
# else :
#     price = 10000

# print(f"Sizga kirish {price} so'm")


# BIR NECHA "elif" LAR QATNASHGAN KOD
#            ||
#            \/


# yosh = int(input("Yoshingiz nechida? "))
# if yosh<=4 :
#     price = 0
# elif yosh<=12 :
#     price = 5000
# elif yosh >=65 :
#     price = 8000
# else :
#     price = 10000

# print(f"Sizga kirish {price} so'm")



# "or" OPERATORI

# kun = input('Bugun nima kun? >>>>>')
# if kun.lower() == 'shanba' or kun.lower() =='yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni')



# "and" OPERATORI

# kun = input('Bugun nima kun? ')
# harorat = float(input('Havo harorati qanday? '))
# if kun.lower() == 'yakshanba' and harorat >=30:
#     print('Bugun cho\'milishga boramiz!')
# elif kun.lower() == 'yakshanba' and harorat <=30:
#     print("Bugun uyda o'tiramiz!")
# else:
#     print('Bugun ishga boramiz')



# BIR NECHA SHARTLARNI KETMA-KET YOZISH

# kun = input('Bugun nima kun? ')
# harorat = float(input('Havo harorati qanday? '))
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >=30:
#     print('Bugun cho\'milishga boramiz!')
# elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat <=30:
#     print("Bugun uyda o'tiramiz!")
# else:
#     print('Bugun ishga boramiz')




#  BOOLEAN MALUMOTLAR TURI

# narh = 15000 # mijoz 15000 so'mga taom oldi
# choy = True # mijoz choy ham oldi//  True = 1
# salat = True # mijoz salat olmadi//  False = 0

# if choy and salat : # agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat : # agar mojiz choy yoki salat olgan bo'lsa
#    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

# print(f"jami haridingiz {narh} so'm")




# SHARTLARNI KETMA-KET TEKSHIRISH

# narh = 15000 # mijoz 15000 so'mga ovqat oldi
# choy = 1   # True
# salat = 0  # False 
# non = 1    # True
# kompot = 1 # True
# assort = 0 # False
# # Quydagi har bir shart alohida tekshiriladi va bir - biriga bo'liq emas
# if choy:  # agar choy olsa
#     print('Mijoz choy oldi')
#     narh = narh + 30000
# else:
#     print('Mijoz choy olmadi')
# if salat: # agar salat olsa
#     print('Mijoz salat oldi')
#     narh = narh + 5000
# else:
#     print('Mijoz salat olmadi')
# if non :
#     print('Mijoz non oldi')
#     narh = narh + 2000
# else:
#     print('Mijoz non olmadi')
# if kompot:
#     print('Mijoz kompot oldi')
#     narh = narh + 5000
# else:
#     print('Mijoz kompot olmadi')
# if assort:
#     print('Mijoz kompot oldi')
#     narh = narh + 15000
# else:
#     print('Mijoz assort olmadi')

# print(f"Jami {narh} so'm")





# RO'YXAT TARKIBINI TEKSHIRISH "in" OPERATORI

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# print('manti' in menu ) # menuda manti bormi?
# print('osh' in menu)    # menuda osh bormi


# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('nima ovqat yeysiz? >>>> ')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bida bunday ovqat yoq.')



# "not in" OPERATORI YORDAMIDA RO'XATTA NIMA YOQ EKANLIGINI TEKSHIRISHIMMIZ MUMKIN

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# print('manti' not in menu)  # menuda manti yoqmi?
# print('osh' not in menu)    # menuda osh yoqmi?




# IKKI RO'YXATNI SOLISHTITRISH

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor.")
#     else:
#         print(f"Kechirasiz, menuda {taom} yoq")




# RO'YXAT BO'SH EMAS EKANLIGINI TEKSHIRISH

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi

#     for taom in  buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor.")
#         else:
#             print(f"Kechirasiz, menuda {taom} yoq")

# else:  # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")
