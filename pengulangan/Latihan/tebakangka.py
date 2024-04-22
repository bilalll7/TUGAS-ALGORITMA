import random
level = 0
salah = 0
while salah < 5:
    level = level + 1
    rahasia = random.randint(1, level * 10)
    print(f"Level ke--{level}")
    tebakan = 0
    while salah < 5 and tebakan != rahasia:
        tebakan = int(input("Tebakan anda ? "))
        if tebakan == rahasia:
            print("Tebakan Benar")
            salah = 0
        elif tebakan < rahasia:
            print("Tebakan anda terlalu kecil")
            salah = salah + 1
        elif tebakan > rahasia:
            print("Tebakan anda terlalu besar")
            salah = salah + 1
        if salah == 5:
            print(f"Game Over. Angka rahasia : {rahasia}")