suhu = int(input("masukan suhu (C):"))

if suhu <10:
    print("kategori: cuaca dingin")
    print("saran memakai pakaian tebal dan minum kopi hangat")
elif suhu <25:
    print("kategori: cuaca sejuk")
    print("saran jalan jalan keluar dan makan ramen")
elif suhu <35:
    print("kategori: cuaca hangat")
    print("saran memakai baju berbahan tipis")
else:
    print("kategori: cuaca panas")
    print("saran minum es teler dan ngemall")