# def foydalanuvchidan_sora(ism, familiya, yosh, manzil, email = '', tel_raqam = None):
#     malumotlar = {
#         'ism' : ism,
#         'familiya' : familiya,
#         'manzil' : manzil,
#         "email" : email,
#         'tel_raqam' : tel_raqam,
#         'yosh' : 2003 - yosh
#     }
#     return malumotlar
# malumotlar = []
# print('\nQuydagi malumotlarni kiriting:')

# while True: 
#    ism = input('\nIsmingiz: ')
#    familiya = input('\nFamiliyangiz: ')
#    yosh = int(input('\nyoshingiz: '))
#    manzil = input('\nManzilingiz: ')
#    email = input('\n"Email" adresingiz: ')
#    tel_raqam = int(input('\nTelefon raqamingiz: '))

#    malumotlar.append(foydalanuvchidan_sora(ism, familiya, yosh, manzil, email, tel_raqam))

#    javob = input('\nYana malumot kiritishni istaysizmi?(yes/no)')
#    if javob != "yes":
#        break

# print("\nbizda quyidagi malumotlar mavjud:")
# for n in malumotlar:
#     if n['email']:
#         adress = n['email']
#     else:
#         adress = 'Malumot kiritilmagan'
#     if n['tel_raqam']:
#         raqam = n['tel_raqam']
#     else:
#         raqam = 'Malumot kiritilmagan'

#     print(f"{n['ism'].title()} {n['familiya'].title()}, {n['yosh']} yoshda, " 
#           f"{n['manzil'].title()} da tug'ilgan, {adress}, {raqam}")




