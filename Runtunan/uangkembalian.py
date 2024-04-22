print('-' * 20)
print('Aplikasi Menghitung Uang Kembalian')
print('-' * 20)

total_bayar = int(input('Total Yang harus dibayar : '))
bayar = int(input('Besar Bayar              : '))

kembalian = bayar - total_bayar

print(f'Kembalian  : Rp. {kembalian}')
lembar50k = kembalian // 50000
print(f'Rp. 50.000 : {lembar50k} lembar')

kembalian = kembalian % 50000
lembar20k = kembalian // 20000
print(f'Rp. 20.000 : {lembar20k} lembar')

kembalian = kembalian % 20000
lembar10k = kembalian // 10000
print(f'Rp. 10.000 : {lembar10k} lembar')

kembalian = kembalian % 10000
lembar5k = kembalian // 5000
print(f'Rp. 5.000  : {lembar5k} lembar')

kembalian = kembalian % 5000
lembar2k = kembalian // 2000
print(f'Rp. 2.000  : {lembar2k} lembar')

kembalian = kembalian % 2000
lembar1k = kembalian // 1000
print(f'Rp. 1.000  : {lembar1k} lembar')