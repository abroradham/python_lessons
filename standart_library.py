import datetime as dt

# bugun = dt.datetime.now()
# x = bugun + dt.timedelta(weeks=2)
# a = []
# for i in range(10):
#     y = x + dt.timedelta(i)
#     a.append(y.date())

# date_strings = [date.strftime('%Y-%m-%d') for date in a]


# print(date_strings)


# hozir = dt.date.today()
# tsana = dt.date(2022, 11, 12)
# farq = hozir - tsana

# print(int(farq.days/30))

# def hisobla(tsana):
#     hozir = dt.date.today()
#     farq = hozir - tsana
#     return int(farq.days/30)

# a = int(input('Yil: '))
# b = int(input('Oy: '))
# c = int(input('Kun: '))

# tsana = dt.date(a, b, c)

# print(f"Tug'ilgan kuningizdan {hisobla(tsana)} oy o'tibti")


import re


# a = input('Telefon: ')
# andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# if re.match(andoza, a):
#     print(True)
# else:
#     print(False)



import re

def aniqla(a):
     andoza = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
     x = re.findall(andoza, a)
     return x

b = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

print(aniqla(b))



