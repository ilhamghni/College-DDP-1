# Nama: Ilham Ghani Adrin Sapta
# NPM: 2306201792
# Kolaborator: Imam Fajri   NPM =  2306165566

import matplotlib.pyplot as plt

# function untuk cek data type suatu object
def get_type(a_str):
    try:
        int(a_str)
        return "int"
    except:
        try:
            float(a_str)
            return "float"
        except:
            return "str"

# function untuk membaca file csv dan memisahkan tiap data menjadi data tabular 3-tuple
def read_csv(file_name, delimiter=','):
    data = []
    data_cek = []
    jenis_data = []
    data_body = []                          # mendeklarasi variabel baru untuk menyimpan data sebelum dan yang akan diolah 
    with open(file_name, "r") as f:
        lines = f.readlines()
        for i in lines:
            data.append(i.strip("\n").split(delimiter))
        data.pop(0)
        header = lines[0].strip().split(delimiter)
        for i in range(len(data[0])):
            data_sementara = []
            for j in range(len(data)):
                hasil = data[j][i]
                data_sementara.append(hasil)
            data_cek.append(data_sementara)
        
        for baris in data_cek:
            tipe_data = 'int'
            for var in baris:
                if get_type(var) == "float":
                    tipe_data = "float"
                if get_type(var) == "str":
                    tipe_data = "str"
                    break
            jenis_data.append(tipe_data)    # meng-assign jenis data setelah menggunakan function get_type

    # for loop untuk cek tipe data dan mengassign tipe yang benar kepada list 3-tuple
    for i in range(len(data_cek[0])):
        data_sementara = []
        for j in range(len(data_cek)):
            if jenis_data[j] == "str":
                hasil = str(data_cek[j][i])
            elif jenis_data[j] == "int":
                hasil = int(data_cek[j][i])
            elif jenis_data[j] == "float":
                hasil = float(data_cek[j][i])
            data_sementara.append(hasil)
        data_body.append(data_sementara)
    return data_body,header,jenis_data             

# memberikan list 3-tuple dari dataframe
def to_list(dataframe):
    return dataframe[0]

# memberikan header dari dataframe
def get_column_names(dataframe):
    return dataframe[1]

# memberikan jenis tipe kolum dari dataframe
def get_column_types(dataframe):
    return dataframe[2]

# funtion untuk print data dengan format tertentu
def head(dataframe, top_n=8):
    cols = get_column_names(dataframe)
    out_str = ""
    out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
    out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
    for row in to_list(dataframe)[:top_n]:
        out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
    return out_str

# funtion untuk print informasi jumlah baris data dan kolom beserta tipenya
def info(dataframe):
    total_rows = len(dataframe[0])

    header = ["Kolom", "Tipe"]
    header_str = header[0].ljust(15) + header[1].ljust(15)
    line = "-" * 30

    column_info = []
    for i in range(len(dataframe[1])):
        col = dataframe[1][i]
        dtype = dataframe[2][i]
        column_info.append(col.ljust(15) + dtype.ljust(15))

    column_info_str = "\n".join(column_info)

    result = f"Total Baris = {total_rows} baris\n\n{header_str}\n{line}\n{column_info_str}"

    return result

# function untuk cek apakah input memenuhi kondisi
def satisfy_cond(value1, condition, value2):
    if condition == "<":
        return value1 < value2
    elif condition == "<=":
        return value1 <= value2
    elif condition == ">":
        return value1 > value2
    elif condition == ">=":
        return value1 >= value2
    elif condition == "!=":
        return value1 != value2
    elif condition == "==":
        return value1 == value2
    else:
        raise Exception(f"Operator {condition} tidak dikenal.")
    
# function untuk memilih kolom tertentu dengan kondisi yang harus dipenuhi
def select_rows(dataframe, col_name, condition, value):
    body, header, type = dataframe
    # Penanganan exception jika kolom tidak ditemukan
    try:
        index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    selected_rows = []
    #for loop dengan function satisfy_cond untuk cek apakah memenuhi kondisi
    for row in body:
        if satisfy_cond(row[index], condition, value):
            selected_rows.append(row)
    return(selected_rows, header, type)

# function untuk memilih kolom tertentu dengan kondisi yang harus dipenuhi
def select_cols(dataframe, selected_cols):
    body, header, type = dataframe
    if not selected_cols:
        raise Exception("Parameter selected_cols tidak boleh kosong.")

    col_indices = []
    for col in selected_cols:
        try:
            col_index = header.index(col)
            col_indices.append(col_index)
        except ValueError:
            raise Exception(f"Kolom {col} tidak ditemukan.")

    selected_data = []
    for row in body:
        selected_row = [row[i] for i in col_indices]
        selected_data.append(selected_row)
    header_baru = []
    # Membuat string output dengan format yang sama seperti fungsi head
    for head in header:
        if head in selected_cols:
            header_baru.append(head)
            
    return (selected_data, header_baru, type)

# function untuk cek frekuensi munculnya kolom tertentu
def count(dataframe, col_name):
    dict = {}
    # Penanganan exception jika kolom tidak ditemukan
    list = to_list(dataframe)
    header = get_column_names(dataframe)
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    
    # Penanganan exception jika tipe data kolom bukan string
    try:
        col_index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} harus bertipe string.")
    
    # Penanganan exception jika tabel kosong
    if len(list) <= 1:
        raise Exception("Tabel kosong.")
    
    # Menggunakan set untuk menghitung frequency count
    unique_values = set(row[col_index] for row in list)
    result = [list[i][col_index] for i in range(len(list))]
    dict = {value: result.count(value) for value in unique_values}
    
    return dict

#funcion untuk mengembalikan rata-rata kolom suatu data
def mean_col(dataframe, col_name):
    list = to_list(dataframe)
    header = get_column_names(dataframe)
    # Penanganan exception jika kolom tidak ditemukan
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    # Penanganan exception jika tipe data kolom bukan string
    try:
        col_index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} harus bertipe string.")
    # Penanganan exception jika tabel kosong
    if len(dataframe) <= 1:
        raise Exception("Tabel kosong.")

    values = [float(row[col_index]) for row in list]
    mean_value = sum(values) / len(values)
    
    return mean_value

# function tambahan untuk mengembalikan median kolom suatu data
def median_col(dataframe, col_name):
    list = to_list(dataframe)
    header = get_column_names(dataframe)
    # Penanganan exception jika kolom tidak ditemukan
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    # Penanganan exception jika tipe data kolom bukan string
    try:
        col_index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} harus bertipe string.")
    # Penanganan exception jika tabel kosong
    if len(dataframe) <= 1:
        raise Exception("Tabel kosong.")
    
    values = [float(row[col_index]) for row in list]

    n = len(values)
    sorted_lst = sorted(values)
    # melihat apakah jumlah data genap atau ganjil dan mendapat median
    if n % 2 == 0:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        median_value = (mid1 + mid2) / 2
    else:
        median_value = sorted_lst[n // 2]
    return median_value

# function tambahan untuk mengembalikan nilai maksimum kolom suatu data
def max_val(dataframe, col_name):
    list = to_list(dataframe)
    header = get_column_names(dataframe)
    # Penanganan exception jika kolom tidak ditemukan
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    # Penanganan exception jika tipe data kolom bukan string
    try:
        col_index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} harus bertipe string.")
    # Penanganan exception jika tabel kosong
    if len(dataframe) <= 1:
        raise Exception("Tabel kosong.")
    
    max_val = max([float(row[col_index]) for row in list])
    return max_val

# function tambahan untuk mengembalikan nilai minimum kolom suatu data
def min_val(dataframe, col_name):
    list = to_list(dataframe)
    header = get_column_names(dataframe)
    # Penanganan exception jika kolom tidak ditemukan
    if col_name not in header:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    # Penanganan exception jika tipe data kolom bukan string
    try:
        col_index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} harus bertipe string.")
    # Penanganan exception jika tabel kosong
    if len(dataframe) <= 1:
        raise Exception("Tabel kosong.")
    
    min_val = min([float(row[col_index]) for row in list])
    return min_val

# function tambahan untuk menampilkan grafik
def show_scatter_plot(x, y, x_label, y_label):
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# function untuk mendefinisikan bentuk grafik tersebut dengan 2 kolom
def scatter(dataframe, kolom_x, kolom_y):
    data_list = to_list(dataframe)
    header = get_column_names(dataframe)
    #penanganan exception jika kolom index tidak ada
    try:
        indeks_kolom_x = header.index(kolom_x)
    except ValueError:
        raise Exception(f"Kolom {kolom_x} tidak ditemukan.")

    try:
        indeks_kolom_y = header.index(kolom_y)
    except ValueError:
        raise Exception(f"Kolom {kolom_y} tidak ditemukan.")

    x_values = [baris[indeks_kolom_x] for baris in data_list]
    y_values = [baris[indeks_kolom_y] for baris in data_list]

    show_scatter_plot(x_values, y_values, kolom_x, kolom_y)

# function tambahan untuk menampilkan grafik 3d dengan input 3 kolom berbeda
def scatter_3d(dataframe, kolom_x, kolom_y, kolom_z):
    data_list = to_list(dataframe)
    header = get_column_names(dataframe)
    #penanganan exception jika kolom index tidak ada
    try:
        indeks_kolom_x = header.index(kolom_x)
    except ValueError:
        raise Exception(f"Kolom {kolom_x} tidak ditemukan.")
    try:
        indeks_kolom_y = header.index(kolom_y)
    except ValueError:
        raise Exception(f"Kolom {kolom_y} tidak ditemukan.")
    try:
        indeks_kolom_z = header.index(kolom_z)
    except ValueError:
        raise Exception(f"Kolom {kolom_z} tidak ditemukan.")

    x_values = [row[indeks_kolom_x] for row in data_list]
    y_values = [row[indeks_kolom_y] for row in data_list]
    z_values = [row[indeks_kolom_z] for row in data_list]
    # menampilkan grafik scatter 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_values, y_values, z_values)

    plt.show()

# Contoh penggunaan:
if __name__ == "__main__":
    dataframe = read_csv("C:\\Users\\ilham\\OneDrive\\Desktop\\Python\\TP03-20231113\\abalone.csv")

    print(head(dataframe, top_n=10))

    print(info(dataframe))

    new_dataframe = select_rows(dataframe,"Length", ">", 0.49 )
    print(head(new_dataframe, top_n=10))
    new_dataframe = select_rows(select_rows(dataframe, "Length", ">", 0.49), "Sex", "==", "M")
    print(head(new_dataframe, top_n= 5))
    new_dataframe = select_cols(dataframe, ["Sex", "Length",\
                                            "Diameter", "Rings"])
    print(head(new_dataframe, top_n = 5))

    print(mean_col(dataframe, "Length"))

    print(count(dataframe, "Sex"))

    print(mean_col(dataframe, "Height"))

    print(median_col(dataframe, "Viscera_weight"))

    print(max_val(dataframe, "Viscera_weight"))

    print(min_val(dataframe, "Viscera_weight"))

    scatter(dataframe, "Height", "Diameter")

    scatter_3d(dataframe, "Height", "Diameter", "Length")