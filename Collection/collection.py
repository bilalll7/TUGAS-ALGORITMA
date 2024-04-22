kelas = ({ 'nama'  : "IF-1",
           'siswa' : [{'nim':'10119001','nama':'Asep'},
                      {'nim':'10119002','nama':'Budi'},
                      {'nim':'10119003','nama':'Cecep'}
                     ]
        },
         { 'nama'  : "IF-2",
           'siswa' : [{'nim':'10119004','nama':'Dede'},
                      {'nim':'10119005','nama':'Erna'} ]
         }
        )
for k in kelas:
  print("Nama Kelas : ", k['nama'])
  print("Banyak Siswa : ", len(k['siswa']))
  print("Daftar Siswa : ")
  for s in k['siswa']:
   print(s["nim"], " - ", s["nama"])
  print("------------------------------")



  # catatan akhir

# • Jika anda ingin menjaga urutan pengisian data, maka gunakan list atau tuple
# • Jika anda ingin memastikan elemen-elemen dalam suatu collection bersifat unik
# dan urutan tidak dianggap penting, maka gunakanlah set
# • Jika anda ingin memastikan bahwa suatu data tidak boleh diubah setelah
# didefinisikan/dibuat, maka buatlah dalam bentuk tuple. 
# • Jika anda membutuhkan collection yang ingin diakses dengan menggunakan suatu
# key, maka gunakanlah dictionary,