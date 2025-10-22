def cerah(waktu):
  if waktu > 30:
    print("Anda Bisa Jalan")
  elif waktu <= 30:
    print("Naik Bus")
  else:
    print("Waktu tidak valid")

def hujan():
  print("Naik Bus")

def berawan(lapar):
   if lapar == "ya":
      print("Jalan")
   elif lapar == "tidak":
      print("Naik Bus")
   else:
      print("Pilihan tidak valid")

print("===== TESTING =====")
print("Pilih cuaca saat ini")
print("1. Cerah")
print("2. Hujan")
print("3. Berawan")

cuaca = input("Masukkan pilihan [1-3] : ")

if cuaca == "1":
   waktu = float(input("Masukkan waktu anda (menit) : "))
   cerah(waktu)

elif cuaca == "2":
   hujan()

elif cuaca == "3":
   lapar = input("Apa kamu lapar? [ya/tidak] : ").lower()
   berawan(lapar)

else:
   print("Pilihan tidak valid")