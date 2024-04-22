# ==========================================SET=============================================================== #

# Set = himpunan.
# Set adalah struktur data python yang mempunyai karakteristik sebagai berikut :
# Mutable → Elemennya bisa ditambah atau dihapus, tapi tidak bisa diedit setelah objeknya dibuat
# Unordered → Urutan data bisa tidak sesuai dengan urutan pengisiannya.
# Not Allow Duplication → Datanya unik (tidak boleh ada yang sama)

s1 = set({}) # set kosong
print(s1)
print(type(s1))
s2 = {5, 1, 3, 5, 2, 0}
print(s2)
s3 = {'A','B','B','a','C'}
print(s3)

# Menelusuri elemen menggunakan set
# Penelusuran dilakukan dengan mengunjungi elemen satu per satu dari elemen pertama sampai elemen terakhir
# Elemen set tidak bisa diakses menggunakan index.
data = {5, 9, 7, 8, 7}
for i in data:
  print(i)

# Penambahan Elemen set
anggota = set({}) # set kosong
print(anggota)
anggota.add("ade")
print(anggota)
anggota.add("budi")
print(anggota)
anggota.update(["cepi","erni","budi"])
print(anggota)

# PENGHAPUSAN ELEMEN SET
data = { 2, 3, 9, 4, 6, 5}
print(data)
data.remove(9)
#data.remove(99) #error
print(data)
data.discard(6)
data.discard(66) #tidak error
print(data)
dihapus = data.pop() #index 1
print("Dihapus ", dihapus)
print(data)