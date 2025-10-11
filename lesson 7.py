beratBadan= int(input("masukan berat badan:"))

if beratBadan>70:
    print("kategori: obesitas")
elif 50 <= beratBadan <= 70:
    print("kategori: ideal")
elif 28<= beratBadan <= 49:
    print("kategori: kurus")
else:
    print("kategori: kekurusan")