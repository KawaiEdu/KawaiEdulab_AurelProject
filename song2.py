import sys
import time

def jalanin_lirik():
    lirik = [
        ("All i ask is", 0.25),
        ("If this is my last night with youuuu ", 0.14),
        ("Hold me like a more than just a friend.." ,0.13),
        ("Give me a memory i can use", 0.12),
        ("Take me by the hand while we do ", 0.1),
        ("Whats lover do ", 0.1),
        ("It matters how this end", 0.10),
        ("'Cause what if I never love again ", 0.13),
        
    ]
    
    delay = [1, 2.4, 2, 4.2, 1.9, 1.5, 2, 3, 0.2, ]
    print("\n == All I Ask ==  ")
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