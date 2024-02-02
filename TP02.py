# Nama: Ilham Ghani Adrin Sapta
# NPM : 2306201792

import os
import time
import sys

def search_keywords_in_section(section, kata_kunci_1, kata_kunci_2, operator, isi):     #membuat fungsi untuk mencari kata kunci di section tertentu
    if section == "all":                                                                #membaca seluruh section untuk mencari keyword
        isi = isi.replace("\n"," ")                                     
        if operator == 'OR':                                        #mencari sesuai operator
            return kata_kunci_1 in isi or kata_kunci_2 in isi               
        elif operator == 'AND':
            return kata_kunci_1 in isi and kata_kunci_2 in isi
        elif operator == 'ANDNOT':
            return kata_kunci_1 in isi and kata_kunci_2 not in isi
        elif operator is None:
            return kata_kunci_1 in isi
        
    elif section in bab:                                            #membaca section tertentu untuk mencari keyword
        isi_section = ""
        status = False
        lines = isi.split('\n')
        for line in lines:                                          #memasukkan isi section tertentu kedalam variabel isi_section untuk diperiksa kata kuncinya
            if line.strip() == f"<{section}>":
                status = True
                continue 
            elif line.strip() == f"</{section}>":
                status = False
                continue  
            if status:
                isi_section += line
        if operator == 'OR':                                        #memeriksa kata kunci 1 dan 2 dengan operator atau hanya kata kunci jika hanya terdapat 1 kata kunci
            return kata_kunci_1 in isi_section or kata_kunci_2 in isi_section
        elif operator == 'AND':
            return kata_kunci_1 in isi_section and kata_kunci_2 in isi_section
        elif operator == 'ANDNOT':
            return kata_kunci_1 in isi_section and kata_kunci_2 not in isi_section
        elif operator is None:
            return kata_kunci_1 in isi_section
    else:
        print("tidak ada section tersebut")
def extract_info_from_tag(putusan):                     # mengambil data dari header putusan untuk dimasukkan ke dictionary
    info_dict = {}
    tag_parts = putusan.strip("<>").split()
    for part in tag_parts:
        if '=' in part:                                 # memisah agar sisi kiri menjadi key dan kanan menjadi value dictionary
            key, value = part.split('=')
            info_dict[key] = value.strip('"')
    return info_dict

section = sys.argv[1].lower()                                           # mengambil argumen dari terminal menggunakan sys 
kata_kunci_1 = sys.argv[2].lower() if len(sys.argv) > 2 else None       # dan membuat exception untuk handle error atau no input
if kata_kunci_1 is None:
    print("Argumen program tidak benar")
    sys.exit(1)
operator = sys.argv[3].upper() if len(sys.argv) > 3 else None
if operator not in ('AND', 'OR', 'ANDNOT', None) :
    print("Operator harus berupa AND, OR, atau ANDNOT.")                # memeastikan operator valid
    sys.exit(1)
kata_kunci_2 = sys.argv[4].lower() if len(sys.argv) > 4 else None
hasil = []
bab = ["kepala_putusan", "identitas", "riwayat_penahanan", "riwayat_perkara", "riwayat_tuntutan", "riwayat_dakwaan", "fakta", "fakta_umum", "pertimbangan_hukum", "amar_putusan", "penutup", "all"]

start_time = time.time()                            # memulai timer

lokasi_folder = [f for f in os.listdir("C:\\Users\\ilham\\OneDrive\\Desktop\\Python\\indo-law-main\\dataset")]
for file in lokasi_folder:                          # looping untuk membaca seluruh file di folder
    lokasi_xml = os.path.join("C:\\Users\\ilham\\OneDrive\\Desktop\\Python\\indo-law-main\\dataset\\", file)
    try:
        with open(lokasi_xml, 'r', encoding='utf-8') as file_saat_ini:          # membuka file tertentu didalam looping
            putusan = file_saat_ini.readline()                                  # membaca baris pertama untuk mendapat header isi
            isi = file_saat_ini.read()                                          # membaca seluruh isi file
            info = extract_info_from_tag(putusan)                               # memanggil function info untuk mendapat dictionary berisi data untuk diprint
            if search_keywords_in_section(section, kata_kunci_1, kata_kunci_2, operator, isi):      # memanggil function untuk cek apakah keyword didalam file
                hasil.append((file, info))
    except FileNotFoundError:                                                   # membuat exception saat tidak ada file di folder
        print("Tidak ada file yang didukung")

end_time = time.time()                              # menghentikan timer
elapsed_time = end_time - start_time                # print waktu yang dibutuhkan program
print(f"{'File Name':<50}{'Provinsi':<15}{'Klasifikasi':<15}{'Sub-Klasifikasi':<30}{'Lembaga Peradilan':<20}")
for file_info in hasil:                             # mencari data didalam dictionary
    file_name, info = file_info
    provinsi = info.get("provinsi", "")             # mencari menggunakan kata kunci spesifik
    klasifikasi = info.get("klasifikasi", "")
    sub_klasifikasi = info.get("sub_klasifikasi", "")
    lembaga_peradilan = info.get("lembaga_peradilan", "")

    provinsi = provinsi[:15]                        
    klasifikasi = klasifikasi[:15]                  # membatasi jumlah kata yang diambil
    sub_klasifikasi = sub_klasifikasi[:30]
    lembaga_peradilan = lembaga_peradilan[:20]
    
    print(f"{file_name:<50}{provinsi:<15}{klasifikasi:<15}{sub_klasifikasi:<30}{lembaga_peradilan:<20}")  # print dengan right-justified

print(f"\nBanyaknya dokumen yang ditemukan: {len(hasil)}")
print(f"Total waktu pencarian: {elapsed_time:.2f} detik\n")

# Fitur tambahan
while True:                                         # looping agar program terus berjalan
    pilihan = input("Apa yang ingin kamu lakukan selanjutnya?\n1. Baca file di section tersebut\n2. Exit\n")
    if pilihan == '1':                              # meminta tindakan lanjutan dari user
        file_name_to_read = input("Masukkan nama file yang ingin Anda baca: ")
        i = 1                                       
        for section in bab:                         # menampilkan section yang tersedia
            print(f"{i}. {section}", )
            i += 1
        section_to_read = bab[int(input("Masukkan section yang ingin Anda baca: "))-1] # mendapatkan section dari input pengguna
        print("\n" + section_to_read + "\n")
        lokasi_xml = os.path.join("C:\\Users\\ilham\\OneDrive\\Desktop\\Python\\indo-law-main\\dataset\\", file_name_to_read)
        with open(lokasi_xml, 'r', encoding='utf-8') as file_saat_ini:
            isi = file_saat_ini.read()
            if section_to_read == "all":                                        # print seluruh section
                print(isi)
            else:
                lines = isi.split('\n')
                in_section = False
                for line in lines:                                              # print section tersebut saja
                    if line.strip() == f"<{section_to_read}>":
                        in_section = True
                    elif line.strip() == f"</{section_to_read}>":
                        in_section = False
                    elif in_section:
                        print(line)
    elif pilihan == '2':
        sys.exit(0)
    else:
        print("Pilihan tidak valid. Pilih 1 untuk membaca file di section atau 2 untuk keluar.")  # print section tersebut
    print("\n")

# Nama: Ilham Ghani Adrin Sapta
# NPM : 2306201792