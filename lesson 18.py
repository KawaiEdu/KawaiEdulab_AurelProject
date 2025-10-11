def kalkulator():
    try:
        angka1 = float(input("masukkan angka pertama: "))
        angka2 = float(input("masukkan angka kedua: "))
        operasi = input("masukkan operasi (+,-,*,/): ")

        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == "/":
            hasil = angka1 / angka2
        else:
            print("Operasi tidak valid!")
            return
        print(f"Hasil:{hasil}")
    except ValueError:
        print("Input harus angka!")
    except ZeroDivisionError:
        print("Tidak bisa dibagi dengan nol!")

while True: 
    print("\n kalkulator sederhana")
    kalkulator()
    lagi = input("apakah anda ingin menghitung lagi? (ya/tidak:)")
    if lagi.lower()!= "ya" :
        print("Terimakasih! Sampai jumpa.")
        break
    