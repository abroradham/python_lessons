import random as r

def son_top():
     while True:
       print ("Keling son topish o'yinini o'ynaymiz:")
       print("Sonlar oralig'ini kiriting")
  
       qabul = int(input("1.Son: "))
       qabul1 = int(input("2.Son: "))


       x = r.choice(range(qabul, qabul1))



       print(f"{qabul} dan {qabul1} gacha son o'yladim topa olasizmi?")
       a = []
       while True:
          y = int(input('>>>>> '))
          a.append(y)
          if y > x:
            print(f"Men o'ylagan son {y} dan kichkina")
          elif y<x:
            print(f"Men o'ylagan son {y} katta")
          else:
            print(f"To'g'ri. Siz {len(a)} ta urinishda topdingiz. Tabriklayman")
            break


       input(f"Siz {qabul} dan {qabul1} gacha son o'ylang, men topaman, o'yinni boshlash uchun istalgan tugmani bosing")
    
       q = []
       while True:
        if qabul != qabul1:
          c = r.choice(range(qabul, qabul1))
        else:
           c = qabul1
        z = input(f"Siz o'ylagan son {c}, to'g'ri bo'lsa (t), bosing"
                  f"{c} dan katta bo'lsa (+), {c} dan kichik bo'lsa (-)ni bosing:").lower()
        q.append(z)
        if z == "+":
           qabul = c +1
        elif z == "-":
          qabul1 = c - 1
        else :
          print(f"{len(q)} ta urinishda topdim")
          break
    
       if len(a) < len(q):
         print(f"Siz yutdingiz")
       else :
        print("Men yutdim")

       w = input("Yana O'ynashni istaysizmi(Y/N): ").lower()
       if w == "n":
          break
     
son_top()