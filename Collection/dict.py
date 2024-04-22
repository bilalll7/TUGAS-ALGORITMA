# ==========================================DICT=============================================================== #
# Dictionary (dict) adalah struktur data python yang mempunyai karakteristik
# sebagai berikut :
# Mutable → Elemen dictionary dapat dimodifikasi (tambah, edit, hapus) setelah objeknya
# dibuat.
# Not Allow Duplication → Tidak boleh memiliki elemen yang mempunyai key yang sama.
# Ordered → Urutan elemen sesuai urutan pengisiannya
# Setiap elemen dictionary harus berupa pasangan antara key dan value. 
# Key dan value dipisahkan dengan tanda titik 2 ( : )
# Pemisah antara elemen adalah tanda koma ( , )

#  Dictionary dibuat dengan menuliskan elemen-elemennya diapit dengan tanda kurung kurawal ( {} )
mhs1 = {'nama':'Asep', 'umur':20, 'kota':'Garut'}
print("Mhs1 : ", mhs1)
mhs2 = {
  "nama" : "Budi",
  "umur" : 17,
  "kota" : "Bandung"
}
print("Mhs2 : ", mhs2)

# MENGAKSES ELEMEN DICTIONARY
#  Untuk mengakses elemen dictionary dapat dilakukan dengan cara berikut :
#  Menggunakan tanda kurung siku. Key ditulis diantara kurung siku
#  Menggunakan function dict.get. Key ditulis sebagai parameter ke function tersebut
#  Nama key bersifat case-sensitive.
mhs = {'nama' : 'Budi',
       'umur' : 21,
       'kota' : 'Bandung'
}
print("Mhs : ", mhs)
print("Nama : ", mhs['nama'])
print("Umur : ", mhs['umur'])
print("Kota : ", mhs.get('kota')) #get

# PENELUSURAN ELEMEN DICTIONARY
for key in mhs:
  print(key)
print("----------------")
for key in mhs:
  print(key, '=>', mhs[key])

# MENAMBAH/MENGUPDATE ELEMEN DICTIONARY
  
mhs = {'nama' : 'Budi',
       'kota' : 'Bandung'
}
print("Mhs : ", mhs)
mhs['kelas'] = 'IF-1' # menambah
print("Mhs : ", mhs)
mhs['kelas'] = 'IF-2' # mengupdate
print("Mhs : ", mhs)
mhs.update({'nilai':86}) # menambah
print("Mhs : ", mhs)
mhs.update({'nilai':77,'nama':'Acep'})
print("Mhs : ", mhs)

# PENGHAPUSAN ELEMEN DICTIONARY
mhs = {'nama' : 'Budi',
'kota' : 'Bandung',
'nilai' : 77
}
print("Mhs : ", mhs)
dihapus = mhs.pop('kota')
print("Dihapus : ", dihapus)
print("Mhs : ", mhs)
del mhs['nilai']
print("Mhs : ", mhs)