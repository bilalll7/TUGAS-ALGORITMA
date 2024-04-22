import random
level = 0
gameover = False
while not gameover:
    level = level + 1
    print('Level',level,"[1..",level * 10,']')
    rahasia = random.randint(1, level * 10)

    tebakan = 0
    salah = 0
    while salah <5 and tebakan != rahasia:
        tebakan = int(input('Tebakan Anda : '))
        if tebakan == rahasia:
            print('Tebakan Anda Benar.')
            salah = 0
        elif tebakan < rahasia: 
            print('Tebakan Anda Terlalu Kecil.')
            salah = salah + 1
        elif tebakan > rahasia:
            print('Tebakan Anda Terlalu besar.')
            salah = salah + 1
    if salah == 5:
        print('Game Over. Anda Sudah salah sebanyak 5 kali')
        gameover = True
        