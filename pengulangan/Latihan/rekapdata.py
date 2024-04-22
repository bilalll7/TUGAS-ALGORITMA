total = 0
banyakdata = 0
data = 0
while data >= 0:
    banyakdata += 1
    print(f' Masukan Data Ke- {banyakdata} : ', end="")
    data=int(input())
    if data >= 0:
        total = total + data
print('-' * 40)
banyakdata = banyakdata - 1
print(f'total : {total}')
print(f'banyak data : {banyakdata}')
rata_rata = total / banyakdata
print(f'rata-rata : {rata_rata}')