# ==========================================TUPLE=============================================================== #

# Tuple adalah struktur data python yang mempunyai karakteristik sebagai berikut :
# Immutable → Datanya tidak bisa dimodifikasi (tambah, update, hapus) setelah objeknya
# dibuat
# Ordered → Urutan data sesuai dengan urutan pengisiannya.
# Allow Duplication → Datanya boleh ada yang sama
# Tuple tidak bisa diedit elemennya, tetapi tuple bisa diganti/replace.

t1 = ()
print(t1)
t2 = (5, ) # tuple 1 data
print(t2)
t3 = (5, 7, 8, 6, 7)
print(t3)
t3 = (6, 3, 5) # Replace
print(t3)

data = (5, 9, 7, 8, 7, 2)
print("Data ke- 0 : ", data[0])
print("Data ke- 1 : ", data[1])
print("Data ke- 2 : ", data[2])
print("Data ke- 3 : ", data[3])
print("Data ke- 3 : ", data[4])
print("Data ke- 3 : ", data[5])

# Menelusuri Tuple
for i in range(len(data)):
  print("Data ke- ", i, " = ", data[i])
for k in data:
  print(k)

# Memodifikasi elemen tuple
data = (6, 3, 7)
print(data)

# Jika tuple di modifikasi akan error
# data[1] = 99
# print(data)