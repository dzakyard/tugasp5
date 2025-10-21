# Variabel nama, nim, password, tanggal lahir dan alamat.
# nim untuk validasi login
nama = "Oktavian Dzaky Ardhani"
nim = "5250411207"
tanggal_lahir = "30 Februari 2000"
alamat = "Ceko"

password = "123"

def login(nim_input, password):                     # function login mencocokan input nim dan password dengan global variabel nim dan password
    return nim_input == nim and password == password 

def tampilkanProfil():                              # function untuk menampilkan profil pengguna sesuai data nama, nim, dll
    print(f"Nama : {nama}")
    print(f"NIM : {nim}")
    print(f"Tanggal Lahir : {tanggal_lahir}")
    print(f"Alamat : {alamat}")

def hitungRataRata(tugas_pertama, tugas_kedua, tugas_ketiga):                           # menghitung rata rata sesuai rumus
    rata_rata = (0.25 * tugas_pertama) + (0.25 * tugas_kedua) + (0.5 * tugas_ketiga)
    return rata_rata


# menampilkan bagian login
print("===== LOGIN MAHASISWA =====")
nim_input = input("Masukkan NIM anda : ")
password = input("Masukkan password anda : ")
cek_login = login(nim_input, password)


# jika login True masuk dashboard
if cek_login == True:
    print("===== DAHSBOARD MAHASISWA =====")
    print("1. Lihat Profil Pengguna\n2. Hitung Nilai Rata-rata tugas\n3. Logout")
    pilihan = input("Pilih menu [1-3] : ")
    
    # jika pilihan 1 tampilkan profil
    if pilihan == "1":
        print("===== PROFIL PENGGUNA =====")
        tampilkanProfil()

    # jika pilihan 2 input nilai lalu akan dihitung
    elif pilihan == "2":
        print("===== HITUNG NILAI RATA-RATA TUGAS")
        tugas_pertama = float(input("Masukkan nilai tugas pertama [1-100] : "))
        tugas_kedua = float(input("Masukkan nilai tugas kedua [1-100] : "))
        tugas_ketiga = float(input("Masukkan nilai tugas tigas [1-100] : "))
        
        nilai = hitungRataRata(tugas_pertama, tugas_kedua, tugas_ketiga)
        print(f"Nilai rata rata kamu adalah {nilai}")

    # jika pilihan 3 pesan terimakasih
    elif pilihan == "3":
        print("Terimakasih sudah berkunjung!")

    # jika pilihan selain 1-3
    else:
        print("Pilihan tidak valid")

# login False
else:
    print("NIM dan password salah")
