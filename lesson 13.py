hari_kerja= ("senin", "selasa", "rabu", "kamis", "jumat")

hari= input("masukan hari:")
if hari in hari_kerja:
    print(f"{hari} hari ini adalah hari kerja")
    
else:
    print(f"{hari} hari ini adalah hari libur")
    

print(len(hari))