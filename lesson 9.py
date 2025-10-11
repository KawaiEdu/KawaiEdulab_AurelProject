def kurang(angka1,angka2):
    return angka1 - angka2
def tambah(angka1,angka2):
    return angka1 + angka2
def kali(angka1,angka2):
    return angka1 * angka2
def bagi(angka1,angka2):
    return angka1 / angka2

angka1 = int(input("masukan angka1:"))
angka2 = int(input("masukan angka2:"))

print("pilih menu \n 1. angka1 - angka2 \n 2. angka1 + angka2 \n 3. angka1 * angka2 \n 4. angka1 / angka2")
pil= int(input("masukan menu yg diinginkan: "))

if pil == 1:
    hasil = kurang(angka1 , angka2)
    print(hasil)
    print("pilihan kurang")

elif pil == 2: 
    hasil = tambah(angka1 , angka2)
    print(hasil)
    print("pilihan tambah")

elif pil == 3: 
    hasil = kali(angka1 , angka2)
    print(hasil)
    print("pilihan kali")

elif pil == 4:
    hasil = bagi(angka1 , angka2)
    print(hasil)
    print("pilihan bagi")
    
else :
    print("1234")



