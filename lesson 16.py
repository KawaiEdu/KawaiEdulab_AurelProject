kartun_favorit_aurel = set()

while True:
    nama_kartun_favorit_aurel = input("masukan nama kartun(ketik 'selesai' untuk berhenti:)")
    if nama_kartun_favorit_aurel.lower() == "selesai" :
        break
    kartun_favorit_aurel.add(nama_kartun_favorit_aurel)

kartun_favorit_kak_nesy = {"doraemon" , "upin ipin" , "dragon ball", "frozen"}
kartun_favorit_kak_aqil = {"tom & jery" , "micky mouse" , "donald duck", "frozen"}


sama = kartun_favorit_kak_nesy & kartun_favorit_kak_aqil & kartun_favorit_aurel
print("kartun yang sama disukai:",sama)

beda1 = kartun_favorit_kak_nesy.difference(kartun_favorit_aurel)
beda2 = kartun_favorit_kak_aqil.difference(kartun_favorit_aurel)
beda3 = kartun_favorit_aurel.difference(kartun_favorit_kak_nesy)
beda4 = kartun_favorit_aurel.difference(kartun_favorit_kak_aqil)
print("kartun yang hanya disukai kak nesy tapi tidak disukai aurel:", beda1)
print("kartun yang hanya disukai kak aqil tapi tidak disukai aurel:", beda2)
print("kartun yang hanya disukai aurel tapi tidak disukai kak nesy:", beda3)
print("kartun yang hanya disukai aurel tapi tidak disukai kak aqil:", beda4)