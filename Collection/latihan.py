mhs = [
  {
        "nim"     : 10119001,
        "nama"    : "Asep",
        "nohp"    : "0812345678",
        "bahasa"  :{
          "pascal", 
          "php", 
          "javascript"
          }
  },
  {
        "nim"     : 10120001,
        "nama"    : "Supriatna",
        "nohp"    : "0815782343",
        "bahasa"  :{
          "php", 
          "javascript", 
          "python"
          }
  },
  {
        "nim"     : 10120002,
        "nama"    : "Irmayanti",
        "nohp"    : "0812226786",
        "bahasa"  :{
          "python", 
          "pascal", 
          "php",
          "java"
          }
  },
  {
        "nim"     : 10120003,
        "nama"    : "Susi",
        "nohp"    : "0856123223",
        "bahasa"  :{
          "python", 
          "c++", 
          "java"
          }
  },
        
        ]
print(mhs)

banyakKemampuan = []
for m in mhs:
  banyakKemampuan.append(len(m["bahasa"]))
print(banyakKemampuan)
for m in banyakKemampuan:
  for i in mhs:
    print(i)
  
