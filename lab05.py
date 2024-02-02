# Inisialisasi database
database = []
while True:
    # Menampilkan menu ke pengguna
    print("\nMenu:")
    print("1. Tambahkan nilai ke Database")
    print("2. Tampilkan nilai dari Database")
    print("3. Update nilai pada Database")
    print("4. Hapus nilai dari Database")
    print("5. Keluar")

    # Minta input  pilihan dari pengguna

    choice = int(input("Pilih aksi (1/2/3/4/5): "))

    if choice == 1:                         # Tambahkan nilai ke Database
        nama = input("Masukkan nama mahasiswa: ").lower()
        cek_nama = False
        for data in database:
            if data[0] == nama:
                print("Nama sudah terdapat di dalam database")
                cek_nama = True
                break
        if cek_nama:
            continue
        nilai_lab = input("Masukkan nilai lab (0-100) atau ketik STOP untuk berhenti: ")
        while nilai_lab != "STOP":         # looping untuk mengambil nilai
            if nilai_lab.isdigit():
                nilai_lab = float(nilai_lab)
                if 0 <= nilai_lab <= 100:  # Periksa apakah nilai berada dalam rentang yang valid
                    duplicate = False
                    for data in database:
                        if data[0] == nama:
                            data[1].append(nilai_lab)
                            duplicate = True
                            break
                    if not duplicate:
                        database.append([nama, [nilai_lab]])
                else:
                    print("Input nilai tidak valid. Harap masukkan bilangan riil antara 0 dan 100.")
            else:                                   # exception untuk nilai tidak valid
                print("Input nilai tidak valid. Harap masukkan bilangan riil antara 0 dan 100.")
            nilai_lab = input("Masukkan nilai lab (0-100) atau ketik STOP untuk berhenti: ")
            if nilai_lab == "STOP":
                break
        print(f"Berhasil menambahkan {len(database[-1][1])} nilai untuk {nama} ke database")
    
    elif choice == 2:                               # Tampilkan nilai dari Database   
        nama = input("Masukkan nama mahasiswa: ").lower()
        found = False
        for data in database:                       # mencari di setiap list di dalam list database
            if data[0] == nama:
                lab_ke = int(input(f"Masukkan lab ke berapa yang ingin dilihat untuk {nama}: "))
                if 1 <= lab_ke <= len(data[1]):
                    print(f"Nilai Lab {lab_ke} {nama} adalah {data[1][lab_ke - 1]}")
                    found = True
                    break
                else:
                    print(f"Tidak ditemukan nilai untuk Lab ke-{lab_ke}.")
                    found = True
                    break

        if not found:                               # exception saat data tidak ditemukan
            print(f"Data untuk {nama} tidak ditemukan di database.")

    
    elif choice == 3:                                           # Update nilai pada Database
        nama = input("Masukkan nama mahasiswa: ").lower()
        lab_ke = int(input("Masukkan lab ke berapa yang ingin diperbarui: "))
        nilai_baru = input("Masukkan nilai lab baru (0-100): ")
        found = False
        for data in database:                                   # mencari di setiap list di dalam list database
            if data[0] == nama and len(data[1]) >= lab_ke:      
                if nilai_baru.isdigit():
                    nilai_baru = float(nilai_baru)
                    nilai_lama = data[1][lab_ke-1]
                    data[1][lab_ke-1] = nilai_baru              # mengganti nilai lama dengan baru
                    print(f"Berhasil mengupdate nilai Lab {lab_ke} {nama} dari {nilai_lama} menjadi {nilai_baru}")
                else:
                    print("Input nilai tidak valid. Harap masukkan bilangan riil antara 0 dan 100.")
                found = True
                break
        if not found:
            print("Data tidak ditemukan.")
    
    elif choice == 4:                                           # Hapus nilai dari Database
        nama = input("Masukkan nama mahasiswa: ").lower()
        lab_ke = int(input("Masukkan lab ke berapa yang ingin dihapus: "))
        found = False
        for data in database:
            if data[0] == nama and len(data[1]) >= lab_ke:
                nilai_hapus = data[1].pop(lab_ke-1)             # menghilangkan nilai lab di database dengan .pop()
                print(f"Berhasil menghapus nilai Lab {lab_ke} {nama} dari database")
                found = True
                break
        if not found:
            print("Data tidak ditemukan.")
    
    elif choice == 5:
        # Keluar dari program
        print("Terimakasih telah menggunakan Database Nilai Dek Depe")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih angka 1 sampai 5.")       # membuat exception agar pilihan pengguna valid
