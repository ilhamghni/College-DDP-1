# Membuat kamus kosong untuk menyimpan hubungan antara orang tua dan anak
hubungan = {}

# Fungsi untuk menambahkan anak ke daftar keturunan dari orang tua tertentu
def keturunan(parent,child):
    if parent not in hubungan:
        hubungan[parent] = []
    hubungan[parent].append(child)
    
# Fungsi untuk memeriksa apakah seorang anak adalah keturunan dari orang tua tertentu
def cek_keturunan(parent, child):
    if parent not in hubungan:
        return False
    if child in hubungan[parent]:
        return True
    for descendant in hubungan[parent]:
        if cek_keturunan(descendant, child):
            return True
    return False

# Fungsi untuk mencetak keturunan dari orang tua tertentu 
def cetak_keturunan(parent, keturunan_ke=0):
    if parent in hubungan:
        print("  " * keturunan_ke + "- " + parent)
        for child in hubungan[parent]:
            cetak_keturunan(child, keturunan_ke + 1)

# Fungsi untuk mencari jarak generasi antara orang tua dan anak
def jarak_generasi(parent,child,jarak = 0):
    if parent == child:
        return jarak
    if parent not in hubungan:
        return -1
    for descendant in hubungan[parent]:
        result = jarak_generasi(descendant, child, jarak + 1)
        if result:
            return result
    return -1

# Loop input untuk mendapatkan hubungan orang tua-anak sampai input adalah "SELESAI"
while True:
    parent_child = str(input("Masukkan data relasi: "))
    if parent_child == "SELESAI":
        break
    parent, child = parent_child.split()
    keturunan(parent,child)

# Loop menu utama untuk interaksi pengguna
while True:
    print("=" * 50)
    print("Selamat Datang di Relation Finder! Pilihan yang tersedia")
    print("1. CEK_KETURUNAN \n2. CETAK_KETURUNAN \n3. JARAK_GENERASI \n4. EXIT")
    pilihan = int(input("Masukkan pilihan:  "))
    if pilihan == 1:
        parent = input("Masukkan nama parent: ")
        child = input("Masukkan nama child: ")
        if cek_keturunan(parent,child):
            print(f"{child} merupakan keturunan dari {parent}")
        else:
            print(f"{child} bukan merupakan keturunan dari {parent}")
    elif pilihan == 2:
        parent = input("Masukkan nama parent: ")
        cetak_keturunan(parent)
    elif pilihan == 3:
        parent = input("Masukkan nama parent: ")
        child = input("Masukkan nama child: ")
        jarak = jarak_generasi(parent, child)
        if jarak != -1:
            print(f"{parent} memiliki hubungan dengan {child} sejauh {jarak}")
        else:
            print(f"Tidak ada hubungan antara {parent} dan {child}")
    elif pilihan == 4:
        print("Terima kasih telah menggunakan Relation Finder!")
        break
    else:
        print("Perintah tidak valid. Silakan coba lagi.")