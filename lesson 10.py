tambah = lambda a, b: a + b
kurang = lambda a, b: a - b
kali = lambda a, b: a * b
bagi = lambda a, b: a / b 

print("Selamat datang di Kalkulator Lambda!")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
operasi = input("Pilih operasi (+, -, *, /): ")

if operasi == '+':
 print("Hasil: ", tambah(a, b))
elif operasi == '-':
 print("Hasil: ", kurang(a, b))
elif operasi == '*':
 print("Hasil: ", kali(a, b))
elif operasi == '/':
 print("Hasil: ", bagi(a, b))
else:
 print("Operasi tidak valid!")