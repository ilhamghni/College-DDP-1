while True:
        print("\nSelamat datang! Masukkan dua nama file yang berisi daftar Makanan yang kamu miliki.")
        file_input =   str(input("Masukkan nama file input daftar makanan : "))
        file_output =  str(input("Masukkan nama file output : "))
        try:
            with open(file_input, "r"):
                break
        except FileNotFoundError:                    # memeriksa apakah ada file bernama tertentu dan mengembalikan pesan jika tidak ada
            print("Maaf, file input tidak ada")
while True:
    print("\nApa yang ingin kamu lakukan?")
    print("===" * 10)
    print("1. Tampilkan daftar makanan pertama")
    print("2. Tampilkan daftar makanan kedua")
    print("3. Tampilkan gabungan makanan dari dua daftar")
    print("4. Tampilkan makanan yang sama dari dua daftar")
    print("5. Keluar")
    print("===" * 10)
    aksi = int(input("Masukkan aksi yang ingin dilakukan: "))

    with open(file_input,"r") as f1:            # membuka file hanya untuk baris pertama
        baris = (f1.readlines()[0])
        output_aksi_1 = baris.strip().lower()
        f1.close()
    with open(file_input,"r") as f2:            # membuka file hanya untuk baris kedua
        baris = (f2.readlines()[1])
        output_aksi_2 = baris.strip().lower()
        f2.close()
    with open(file_input,"r") as f3:            # membuka file untuk menyimpan semua baris di file kedalam satu "set"
        baris1 = (f3.readline())
        baris2 = (f3.readline())
        makanan_saja_1 = baris1.replace("Daftar Makanan 1: ","")        # menghilangkan "daftar makanan" sehingga menyisakan hanya nama makanan
        makanan_saja_2 = baris2.replace("Daftar Makanan 2: ","")
        gabungan_makanan = makanan_saja_1.strip().lower() + "," + makanan_saja_2.strip().lower() + ","
        # Inisialisasi variabel untuk menyimpan semua makanan
        makanan_semuanya = ""
        # Inisialisasi variabel untuk menyimpan makanan yang sudah dicek
        makanan_dicek = ""
        # Loop untuk mencari makanan yang muncul lebih dari sekali

        for karakter in gabungan_makanan:
            if karakter == ",":
                if makanan_dicek in gabungan_makanan:
                    if makanan_dicek not in makanan_semuanya:
                        makanan_semuanya += makanan_dicek + ","
                makanan_last = makanan_dicek
                makanan_dicek = ""
            else:
                makanan_dicek += karakter
        # Menghilangkan koma terakhir
        if makanan_semuanya.endswith(","):
            makanan_semuanya = makanan_semuanya[:-1]
        f3.close()
        if makanan_semuanya:
            output_aksi_3 = makanan_semuanya

    with open(file_input,"r") as f4:        # membuka file untuk pengecekan nama yang sama
        baris1 = (f4.readline())
        baris2 = (f4.readline())
        makanan_saja_1 = baris1.replace("Daftar Makanan 1: ","")        # menghilangkan "daftar makanan" sehingga menyisakan hanya nama makanan
        makanan_saja_2 = baris2.replace("Daftar Makanan 2: ","")
        gabungan_makanan = makanan_saja_1.strip().lower() + "," + makanan_saja_2.strip().lower() + ","
        makanan_berulang = ""

        # Inisialisasi string untuk menyimpan nama makanan yang sudah dicek
        makanan_dicek = ""

        # Loop untuk mencari makanan yang muncul lebih dari sekali
        for karakter in gabungan_makanan:
            if karakter == ",":
                if gabungan_makanan.count(makanan_dicek) > 1 and makanan_dicek not in makanan_berulang:
                    makanan_berulang += makanan_dicek + ","
                makanan_dicek = ""
            else:
                makanan_dicek += karakter

        # Menghilangkan koma terakhir
        if makanan_berulang.endswith(","):
            makanan_berulang = makanan_berulang[:-1]

        # Mencetak nama makanan yang muncul lebih dari sekali dan kosong saat tidak ada
        if makanan_berulang:
            output_aksi_4 = makanan_berulang
        else:
            output_aksi_4 = " "

        f4.close()
    print("")
    if aksi == 1:                   # Memproses aksi yang dimasukkan user
        print(output_aksi_1)
        with open(file_output, "a") as output:
            # Menulis teks ke dalam file output
            output.write(f"{output_aksi_1}\n\n")
    elif aksi == 2:
        print(output_aksi_2)
        with open(file_output, "a") as output:
            output.write(f"{output_aksi_2}\n\n")
    elif aksi == 3:
        print(f"Gabungan makanan favorit dari kedua daftar: \n{output_aksi_3}")
        with open(file_output, "a") as output:
            output.write(f"Gabungan makanan favorit dari kedua daftar: \n{output_aksi_3}\n\n")
    elif aksi == 4:
        if output_aksi_4 == " ":
            print("tidak ada makanan yang sama didalam data")
        else:
            print(f"makanan yang sama dari dua daftar: \n{output_aksi_4}")
            with open(file_output, "a") as output:
                output.write(f"Makanan yang sama dari dua daftar: \n{output_aksi_4}\n\n")
        
    elif aksi == 5:
        print("Terima kasih telah menggunakan program ini! Semua keluaran telah disimpan pada file out1.txt")
        break
    else:
        print("Aksi invalid, anda akan dikeluarkan dari program")
        break
