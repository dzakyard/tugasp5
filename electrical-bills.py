print("===== ELECTRICAL BILLING SYSTEM =====")

kwh = float(input("Masukkan kWh anda : ")) # menyimpan input kwh

# jika input tidak sesuai
if kwh <= 0:
    print("kwh tidak valid")
    
# jika kwh 1 - 100
elif kwh <= 100:
  tarif = kwh * 1000

# jika kwh 1-300
elif kwh <= 300:
  tarif = 100000 + (kwh - 100) * 1500

# jika kwh lebih dari 300
else:
  tarif = 400000 + (kwh - 300) * 2000

# jika tarif lebih dari 500.000
if tarif > 500000:
  total_tarif = tarif + ((5/100)* tarif)

# jika tarif kurang dari 500.000
else:
  total_tarif = tarif

print(f"bills anda adalah {total_tarif}, Mohon pilih metode pebayaran")

# tampilkan menu pembayaran
print("===== METODE PEMBAYARAN =====")
print("1. PLN Mobile")
print("2. Lainnya")
metode = input("Masukkan pilihan metode [1/2] : ") # menyimpan pilihan metode

# jika 1. PLN Mobile makan akan mendapat diskon
if metode == "1":
  total_bills_diskon = total_tarif - ((2/100) * total_tarif)
  print(f"Total Tagihan anda setelah diskon adalah {total_bills_diskon}")

# jika metode lainnya maka total tarif tetap sama
elif metode == "2":
  print(f"Total Tagihan anda adalah {total_tarif}")

# jika memilih selain 1 atau 2
else:
  print("Pilihan metode pembayaran tidak valid")