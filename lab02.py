def border():                                   #Fungsi untuk garis border
    print("===" * 15)

def validasi_id(id):                            #fungsi untuk menambah setiap digit pada id yang diberikan user
    total = 0
    for digit in id:
        total += int(digit)
    return total == 23

def check_id():                                 #fungsi untuk memeriksa apakah id membership valid dengan percobaan max 3 kali
    global percobaan 
    global max_percobaan 
    percobaan = 0
    max_percobaan = 3
    while percobaan < max_percobaan:
        id = input("Masukkan ID membership (5 digit): ")
        if len(id) != 5 or not id.isdigit():
            print("ID tidak valid. Harap masukkan 5 digit angka.")
            continue
        if validasi_id(id):
            print("Login Member berhasil, Selamat datang!")
            break
        else:
            print("ID anda salah!.")
            percobaan += 1
    if percobaan == max_percobaan:
        print("Anda telah mencoba memasukkan ID yang tidak valid sebanyak 3 kali. Kembali ke menu utama.")
        
katalog = {                                     #ini menyimpan katalog buku yang tersedia didalam dictionary dengan harganya
        "x-man": 7000,
        "doraemoh": 5500,
        "nartoh": 4000,
        }

while True:                                     #while loop akan membuat Program terus mengulang hingga diperintah berhenti oleh user
    print("Selamat Datang di Toko Buku Place Anak Chill")
    border()
    print("1. Pinjam buku\n2. Keluar")
    border()
    menu = int(input("Apa yang ingin anda lakukan: "))
    
    if menu == 1:                                #akan meelanjutkan program jika user memasukkan input "1"
        nama = input("Masukkan nama anda: ")
        saldo = int(input("Masukkan saldo anda (Rp): "))
        member = input("Apakah anda member? [Y/N]: ")
        
        if member == "Y":
            check_id()
            if percobaan == max_percobaan:
                continue
        elif member == "N":
            print("Login Non-Member berhasil, Selamat datang!")

        while True:                               #Loop untuk menampilkan katalog dan menu secara menerus jika input dari user tidak sesuai dengan katalog
            border()
            print ("Katalog Buku Place Anak Chill")
            border()
            print("X-Man (Rp 7.000/hari)\nDoraemoh (Rp 5.500/hari)\nNartoh (Rp 4.000/hari)")
            border()
            print("Exit")
            border()
    
            buku = (input("Buku yang dipilih: ")).lower()       #mengubah input menjadi lower case agar menjadi case insensitive
            
            if buku == "exit":
                break
            
            elif buku in katalog:
                durasi = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                
                if member == "Y":
                    harga = katalog[buku] * durasi * 0.8        #memberi diskon sebanyak 20% bagi pelanggan Membership dan menampilkan detil peminjaman
                    if harga <= saldo:
                        saldo -= harga
                        print(f"Berhasil meminjam buku {buku} selama {durasi} hari. Saldo anda saat ini Rp{saldo}")
                    else:
                        print(f"Tidak berhasil meminjam buku {buku}! Saldo anda kurang Rp", harga - saldo)
                
                elif member == "N":
                    harga = katalog[buku] * durasi
                    if harga <= saldo:
                        saldo -= harga
                        print(f"Berhasil meminjam buku {buku} selama {durasi} hari. Saldo anda saat ini Rp{saldo}")
                    else:
                        print(f"Tidak berhasil meminjam buku {buku}! Saldo anda kurang Rp", harga - saldo)
            
            else:
                print("Buku tidak ditemukan dalam katalog. Silakan coba lagi.")
    
    elif menu == 2:                                             #akan memberhentikan program jika user memasukkan input "2"
        print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill")
        break
