nama = 'Cecep Gorbachev'

def tulisNama():
  print(nama)

def tulisNamaBerulang(n):
  for i in range(1, n + 1):
    print(f'{i}. Nama Saya {nama}')

def jumlahDeret(n):
  jumlah = 0
  for i in range(1,n+1):
    jumlah = jumlah + i
  return jumlah

def besarBunga(awal,persenBunga,waktu):
  return awal * (1 + persenBunga/100) ** waktu

# program utama
tulisNama()
tulisNamaBerulang(10)

totalDeret = jumlahDeret(10)
print(f'Total Deret 1 s/d 10 : {totalDeret}')
print(f'test,{nama}')
print(f'Nama Saya adalah {nama}')