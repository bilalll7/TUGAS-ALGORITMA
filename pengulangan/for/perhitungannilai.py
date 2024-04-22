daftar_nilai = [80,85,70,65,95]
total = 0
for nilai in daftar_nilai:
  total += nilai
rata_rata = total / len(daftar_nilai)
print("Total : {}".format(total))
print("Rata-rata : {}".format(rata_rata))