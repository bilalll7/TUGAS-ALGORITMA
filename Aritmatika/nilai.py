nilai = int(input('Masukan nilai : '))

if nilai >= 40 and nilai <=100:
    print('Anda Lulus')
elif nilai < 0 or nilai >100:
    print('Masukan nilai 0 s/d 100 !!!')
else:
    print('Anda tidak lulus')
