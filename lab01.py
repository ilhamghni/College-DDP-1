#Kode ini mengambi input dari user tentang pesan Zog untuk di konversi ke ASCII
pesan_zog_hex = str(input("Masukkan pesan Zog: "))  
pesan_terjemah = bytearray.fromhex(pesan_zog_hex).decode()

#Kode ini mengambi input dari user tentang clue password Zog untuk di konversi ke bentuk biner
nomor_pertama = int(input("Masukkan nomor pertama Zog: "))
nomor_kedua = int(input("Masukkan nomor kedua Zog: "))

#nomor yang didapat akan di kali satu sama lain lalu dikali 13, lalu dikonversi ke biner
password_terjemah = bin(nomor_pertama * nomor_kedua * 13)

#Kode ini memberikan user hasil terjemahan pesan dan password rahasia Zog yang telah di terjemahkan
print("Hasil terjemahan pesan adalah:", pesan_terjemah)
print("Password adalah: ", password_terjemah )
print(f"Pesan: \"{pesan_terjemah}\" telah diterima dengan password: \"{password_terjemah}\"")