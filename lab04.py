import sys

def print_headers():                                  # fungsi Print table headers
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

def print_table(filename):                            # fungsi print seluruh tabel yang sudah terurut
    with open(filename, "r") as f:
        print("\n")
        print_headers()
        data_sorted = []                              # membuat list data yang sudah disortir
        no = 1  
        for line in f:                                  
            columns = line.strip().split('\t')           # memisahkan setiap kata agar menjadi valuenya tersendiri
            if len(columns) >= 4:
                model = " ".join(columns[:len(columns) - 3])       # melihat apakah kolom yang didapat lebih dari 4 dan mengabungan nama model hp yang terpisah
                harga, layar, ram = columns[-3:]                   # men-asign kolom yang dipisahkan ke variabelnya masing-masing
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(no,model,harga,layar,ram))
                data_sorted.append((no, model, harga, layar, ram)) # memasukkan seluruh variabel kedalam list data_sorted
                no += 1
        print("\n")
        return data_sorted                              # mengembalikan value data_sorted

def search_function(filename, keyword):                 # fungsi print tabel yang sudah difilter keyword
    data = print_table(filename)                        # memanggil fungsi print_table untuk mengolah data_sorted dari fungsi sebelumnnya
    print_headers()
    filtered_data = []                                  # variabel baru untuk menyimpan data baru yang akan di filter menurut keyword
    no = 1                                              
    for line in data:
        if keyword.lower() in line[1].lower():                  # melihat apakah keyword ada di data
            print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(no,line[1],line[2],line[3],line[4] ))
            no += 1
            filtered_data.append(line)                  # memasukkan data yang memiliki keyword
        else:
            continue
    if not filtered_data:                               # mengeluarkan program saat tidak ada kata kunci di data
        print("Tidak ada smartphone yang dicari")
        sys.exit()
    return filtered_data                                # mengembalikan value filtered_data

def desc_stat(column):                                  # fungsi print keterangan minimum, maksimum, dan rata rata nilai kolom tertentu
    try:                                                
        data = search_function(file_path, key)          # memanggil fungsi search_function
        values = []                                     # membuat variabel baru untuk memasukkan data yang didapat
        for line in data:
            if line[column]:
                values.append(float(line[column]))      # memasukkan data didalam kolom tertentu kedalam variabel values
            else:
                print("Tidak ada data numerik dalam kolom")
        if values:                                      # print ukuran, minimum, maksimum, dan rata-rata data dari kolom
            print("Ukuran data dari hasil pencarian: {} x {}".format(len(values),2))
            print("Minimum: {:.2f}".format(min(values)))
            print("Maksimum: {:.2f}".format(max(values)))                   
            print("Rata-rata: {:.2f}".format(sum(values) / len(values)))
    except FileNotFoundError:                           # membuat exception saat file yang dimasukkan user tidak ada akan mengeluarkan program
        print("Maaf, file input tidak ada")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3]) + 1

desc_stat(column_num)                                        # memanggil fungsi agar tereksekusi