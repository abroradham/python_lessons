# # Task 1

 def katta_son_qaytar(a, b, c):
     if a>b and a>c:
         return a
     elif a<b and b>c:
         return b
     else:
         return c


# a = int(input('Son: '))
# b = int(input('Son: '))
# c = int(input('Son: '))

# katta_son_qaytar(a, b, c)




# # Task 2

# def katta_harf_qaytar(a):
#     c = []
#     for i in a:
#         c.append(i.title())
#     return c
# s = ['assalom aleykum', 'men kasalman', 'sen tuzikmisan']

# katta_harf_qaytar(s)






# # Task 3

# e = []
# while True:
#     d = int(input('Son: '))
#     e.append(d)
#     a = input("Yana son qo'shishni istaysizmi?(Y/N)").upper()
#     if a == 'Y':
#         continue
#     else:
#         break


# def juft_son_qaytar(a):
#     b = []
#     for n in a:
#         if n%2 == 0:
#            b.append(n)
#     return b 

# print(juft_son_qaytar(e))




#  Task 4

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
   

def fibonaccidami(a):
    if a in fibonacci(a):
       return f"{a} is a Fibonacci number."
    else:
       return f"{a} is not a Fibonacci number."
 
 

