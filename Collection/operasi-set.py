# ==========================================OPERASI SET=============================================================== #

# Operasi-operasi khusus dalam set (himpunan)

# Union (penggabungan)
# Intersection (irisan)
# Difference (perbedaan)
# Symmetric Difference

a = {1, 2, 3, 4, 5} #jeruk
b = {4, 5, 6, 7, 8} #anggur
print("Himpunan A: ", a)
print("Himpunan B: ", b)

# Contoh operasi-operasi pada set :

union = a.union(b) # union = a | b
print("Union : ", union)
intersect = a.intersection(b) # intersect = a & b
print("intersect : ", intersect)
diff = a.difference(b) # diff = a - b
print("Difference : ", diff)
syndiff=a.symmetric_difference(b) # syndiff = a ^ b
print("Symmetric Diff : ",syndiff)