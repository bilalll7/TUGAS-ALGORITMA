# ==========================================LIST=============================================================== #

# data = []
# print(data)
data = [4,5,6,5,7,8]
print(data)
# Menelusuri Data
print("Data ke - 0 : ", data[0])
print("Data ke - 1 : ", data[1])
print("Data ke - 2 : ", data[2])
print("Data ke - 3 : ", data[3])
print("Data ke - 4 : ", data[4])
print("Data ke - 5 : ", data[5])

# Mengubah data/Elemen
data[2] = 99
print(data)

data = [4,5,6,5,7,8]
# Cara ke 1 menggunakan index
for i in range(len(data)):
  print("Data ke-", i, " = ", data[i])
# Cara ke 2
for k in data:
  print(k)


# Menambah elemen list
data = [2]
print(data)
data = data + [1,4] #penggabungan list
print(data)
data.append(5)
print(data)
data.insert(0,2) #sisip 2 di index 0
print(data)
data.extend([8, 9, 7])
print(data)

# Menghapus Elemen list
data = [5, 7, 5, 3, 2, 6, 8]
print(data)
data.remove(7)
print(data)
data.remove(5)
print(data)
dihapus = data.pop(1) # hapus index 1
print("Dihapus : ", dihapus)
print(data)
del data[2] # hapus index 2
print(data)