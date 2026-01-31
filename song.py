import sys
import time

def jalanin_lirik():
    lirik = [
        ("Beginikah surga ", 0.10),
        ("Bayangkan ", 0.13),
        ("Bilaaa " ,0.1),
        ("Kau ajakku bicara ", 0.12),
        ("Ini semua bukan salahmu ", 0.1),
        ("Punya magis perekat yang sekuat itu ", 0.1),
        ("Dari lahir sudah begitu ", 0.1),
        ("Maafkan...", 0.16),
        ("Aku jatuh suka ", 0.16),
        
    ]
    
    delay = [0.1, 0.5, 1, 4.2, 2.5, 1.6, 2, 3, 0.2, ]
    print("\n == Jatuh Suka ==  ")
    time.sleep(0.1)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu :
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    

if __name__ == "__main__":
    jalanin_lirik()