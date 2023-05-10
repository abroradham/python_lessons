

# HOME WORK

# buuyrtmalar = []
# n = 1
# ishora = True
# while ishora:
#   buyurtma = input(f"{n} - mahsulotni zakaz qiling: ")
#   buuyrtmalar.append(buyurtma)
#   print(f"Buyurtmangiz qabul qilindi")
#   sorov = input("Yana mahsulot zakaz qilishni istaysizmi? (ha/yo'q)")
#   if sorov == "yo'q":
#     ishora = False
#   n += 1

# print('Sizning buyurtmalaringiz quydagilar:')
# for a in buuyrtmalar:

#   print(f"{a.title()}")


# e_bozor = {}
# ishora = True
# while ishora:
#     mahsulot = input(' "e_bozor" uchun mahsulotni kiriting: ')
#     narh = input(f'{mahsulot.title()} ning narhini kiriting: ')
#     narh = float(narh)
#     e_bozor[mahsulot] = narh

#     sorov = input("Yana mahsulot kiritishni istaysizmi? (ha/yo'q)")
#     if sorov == "yo'q":
#         ishora = False

# print('Sizning mahsulotlaringiz quydagilar: ')
# for x,y in e_bozor.items():
#     print(f"{x.title()} - {y} so'm")


# e_bozor = {
#     "charger" : 30_000,
#     'naushnik' : 20_000,
#     'telefon chexol' : 8_000,
#     'klaviatura' : 150_000,
#     'mishka' : 50_000
# }

# buuyrtmalar = []
# n =1
# ishora = True
# while ishora:
#   buyurtma = input(f"{n} - mahsulotni zakaz qiling: ")
#   buuyrtmalar.append(buyurtma)
#   print(f"Buyurtmangiz qabul qilindi")
#   sorov = input("Yana mahsulot zakaz qilishni istaysizmi? (ha/yo'q)")
#   if sorov == "yo'q":
#     ishora = False
#   n += 1

# for a in buuyrtmalar:
#   if a in e_bozor:
#     print(f" {a.title()} ning narhi - {e_bozor[a]} so'm")
#   else:
#     print(f'Bizda {a.title} mavjud emas.')
