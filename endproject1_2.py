print("pilih menu \n 1. ax + b = c \n 2. ax - b = c \n 3. a + bx = c \n 4. a - bx = c ")
pil = int(input("masukan menu yg diinginkan:"))

angka1 = int(input("masukan angka 1: "))
angka2 = int(input("masukan angka 2: "))
angka3 = int(input("masukan angka 3: "))

if pil == 1:
    print(f"{angka1} x + {angka2} = {angka3}")
    cara1 = (angka3 - angka2) / angka1
    print("hasil nilai x adalah" , cara1)
elif pil == 2:
    print(f"{angka1} x - {angka2} = {angka3} ")
    cara2 = (angka3 + angka2) / angka1
    print("hasil nilai x adalah" , cara2)
elif pil == 3:
    print(f"{angka1} + {angka2} x = {angka3}")
    cara3 = (angka3 - angka1) / angka2
    print("hasil nilai x adala" , cara3)
elif pil == 4:
    print(f"{angka1} - {angka2} x = {angka3}")
    cara4 = (angka3 - angka1) / (-angka2)
    print("hasil nilai x adalah" , cara4)
else:
    print(" inputkan menu 1-4 saja")