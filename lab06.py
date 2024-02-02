def cek_dict(data_mahasiswa, matkul_mahasiswa):                 # Function untuk cek nama, npm, dan matkul didalam dictionary dan mengembalikan index
    for n in range(len(dataset['nama'])):
        if data_mahasiswa in dataset['nama'][n] or data_mahasiswa in dataset['npm'][n]:
            for m in range(len(dataset['matkul'])):
                if matkul_mahasiswa in dataset['matkul'][m]: 
                    return n + m                                # mengembalikan indeks dimana data yang ook ditemukan
while True:                 
    with open("Lab6.txt", "r") as f:                            # buka file lab.txt
        line = f.read().split("\n")
        data_atas = [line[i]for i in range(0,len(line)- 1,4)]                       # membaca nama, npm, dan matkul mahasiswa
        list = [i.split(";") for i in data_atas]                                    # memisahkan nama, npm, dan matkul menjadi list tersendiri
    print("\nSelamat datang di program Plagiarism Checker!")
    print("="* 80)
    data_matkul = input("Masukkan nama mata kuliah yang ingin diperiksa: ")         # meminta matkul yang ingin di cek
    if data_matkul == "EXIT":                                                       
        print("Terima kasih telah menggunakan program Plagiarism Checker!")
        break
    elif data_matkul not in [matkul for matkul in [data[2] for data in list]]:      # melihat apakah matkul ada di dalam dictionary
        print(f"{data_matkul} tidak ditemukan.")                                    # dan mengulang input jika tidak ada
        continue
    data_pertama = input("Masukkan nama/NPM mahasiswa pertama: ")
    if data_pertama not in [nama for nama in [data[0] for data in list]] and data_pertama not in [npm for npm in [data[1] for data in list]]:
        print(f"informasi mahasiswa tidak ditemukan.")                              # cek apakah nama/ npm mahasiswa 1 di dictionary
        continue
    data_kedua = input("Masukkan nama/NPM mahasiswa kedua: ")
    if data_kedua not in [nama for nama in [data[0] for data in list]] and data_kedua not in [npm for npm in [data[1] for data in list]]:
        print(f"informasi mahasiswa tidak ditemukan.")                              # cek apakah nama/ npm mahasiswa 2 di dictionary
        continue
    dataset = {"nama": [siswa for siswa in [data[0] for data in list]],             # memasukkan semua file ke dalam dictionary
               "npm" : [npm for npm in [data[1] for data in list]], 
               "matkul" : [matkul for matkul in [data[2] for data in list]], 
               "isi": [isi for isi in [line[i].split(" ") for i in range(2,len(line)- 1,4)]]}
                # dictionary berisi seluruh data 
    set_isi_siswa_1 = set(dataset["isi"][cek_dict(data_pertama, data_matkul)])      # mengubah kata dalam isi tugas menjadi set dengan kata unik
    set_isi_siswa_2 = set(dataset["isi"][cek_dict(data_kedua, data_matkul)])     
    print(set_isi_siswa_1)   
    irisan = set_isi_siswa_1 & set_isi_siswa_2                                      # irisan kata yang terdapat di kedua isi tugas mahasiswa
    hasil = len(irisan)/len(set_isi_siswa_1) * 100                                  # cek persentase kemiripan 
    print(f"Tingkat kemiripan tugas {data_matkul} {dataset['nama'][cek_dict(data_pertama, data_matkul)]} dan {dataset['nama'][cek_dict(data_kedua, data_matkul)]} adalah {hasil:.2f}%")
    if hasil < 31:                                                                  # cek apakah terindikasi plagiat sesuai persentase kemiripan
        print(f"{dataset['nama'][cek_dict(data_pertama, data_matkul)]} dan {dataset['nama'][cek_dict(data_kedua, data_matkul)]} tidak terindikasi plagiarisme.")
    elif hasil >= 31 and hasil <= 70:  
        print(f"{dataset['nama'][cek_dict(data_pertama, data_matkul)]} dan {dataset['nama'][cek_dict(data_kedua, data_matkul)]} terindikasi plagiarisme ringan.")
    else:
        print(f"{dataset['nama'][cek_dict(data_pertama, data_matkul)]} dan {dataset['nama'][cek_dict(data_kedua, data_matkul)]} terindikasi plagiarisme.")