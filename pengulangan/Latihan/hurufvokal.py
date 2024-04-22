kalimat = input("Kalimat : ")
banyak = 0
hurufvokal = ""
for huruf in kalimat:
    if huruf.upper() in ['A','E','I','O','U']:
        banyak = banyak + 1
        hurufvokal = hurufvokal + huruf
print(f"Huruf vokal ada {banyak} ({hurufvokal})")