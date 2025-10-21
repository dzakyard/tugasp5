# Menampilkan menu
print("===== TESTING =====")
print("Pilih cuaca saat ini")
print("1. Cerah")
print("2. Hujan")
print("3. Berawan")

cuaca = input("Masukkan pilihan [1-3] : ")  # pilihan disimpan dalam variable cuaca

# jika cerah
if cuaca == "1":
   waktu = float(input("Masukkan waktu anda (menit) : "))
   if waktu <= 0:
       print("Waktu tidak valid")
   elif waktu <= 30:
       print("Naik Bus")
   else:
       print("Jalan")

# jika hujan
elif cuaca == "2":
   print("Naik Bus")

# jika berawan
elif cuaca == "3":
   lapar = input("Apa kamu lapar? [ya/tidak] : ").lower()
   if lapar == "ya":
      print("Jalan")
   elif lapar == "tidak":
      print("Naik Bus")
   else:
      print("Pilihan tidak valid")

# jika pilihan selain 1-3
else:
   print("Pilihan tidak valid")
   
   
   
   
   
   
   
   