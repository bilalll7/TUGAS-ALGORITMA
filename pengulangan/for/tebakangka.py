import random
rahasia = random.randint(1,10)
tebakan = 0

while tebakan != rahasia:
  tebakan = int(input('Tebak Angka 1 s/d 10 : '))
  if tebakan == rahasia:
    print('Selamat Tebakan Anda Benar !')
  elif tebakan > rahasia:
    print('Tebakan terlalu besar')
  else:
    print('Tebakan terlalu kecil')