while True:
    print("tampilkan bahasa ucapan selamat ulang tahun:")
    print("1. bahasa china")
    print("2. bahasa jepang") 
    print("3. bahasa korea")
    print("4. bahasa inggris")
    print("5. bahasa indonesia")
    print("6. keluar")
    pilihan = int(input("masukan nomor pilihan anda:"))
    nama = input("siapa nama anda:")
    
    if pilihan == 1:
        ucapan = 1
        while ucapan <= 5:
            print("生日快乐", nama, ucapan)
            ucapan += 1
    elif pilihan == 2:
        for i in range(5):
            print("お誕生日おめでとう",nama)
    elif pilihan == 3:
        for i in range(1,6):
            print("생일 축하해요", nama)
    elif pilihan == 4:
        ucapan = 1
        while ucapan <= 5:
            print("happy birthday", nama, ucapan)
            ucapan += 1
    elif pilihan == 5:
        ucapan = 1
        while ucapan <= 5:
            print("selamat ulang tahun", nama, ucapan)
            ucapan += 1
    elif pilihan == 6:
        print("terimakasih", nama)
        break
    else:
        print("pilihan tidak ditemukan") 
    
            
 