import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.dict_hotel = {'hotel1': [10, 250000, 'kode_hotel_1'], 'hotel2': [12, 500000, 'kode_hotel_2'], 'hotel3': [10, 7500000, 'kode_hotel_3'], 
                        'hotel4': [1, 1000000, 'kode_hotel_4'], 'hotel5': [10, 900000, 'kode_hotel_5'], 'hotel6': [10, 6000000, 'kode_hotel_6']}
        self.username_var = tk.StringVar()
        self.hotel_var = tk.StringVar()
        self.room_var = tk.StringVar()

        # tambahkan title dan ukuran windows
        self.homepage()
        self.master.title("Paciloka App")
        self.master.geometry("500x1000")

        self.img = tk.PhotoImage(file='ornamen.png')
    
    # Create a Canvas widget and display the image using grids
        self.canvas = tk.Canvas(self.master, width=500, height=200)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.canvas.grid(row=0, column=0)


    # tambahkan label, field, dan button yang dibutuhkan
    def homepage(self):
        row = 1

        # Tampilkan informasi awal
        tk.Label(self.master, text="Informasi Hotel", font=('montserrat', 24, 'bold')).grid(row=row, column=0, columnspan=2, pady=10)
        row += 1

        for nama_hotel, info in self.dict_hotel.items():
            available_rooms, room_price, hotel_code = info
            hotel_info = f"Nama Hotel: {nama_hotel}\nJumlah Kamar Tersedia: {available_rooms}\nHarga per Kamar: {room_price}"
            tk.Message(self.master, text=hotel_info, font=('roboto', 9), anchor="w").grid(row=row, column=0, columnspan=2, sticky="w")
            row += 1

        # Tambahkan label dan field untuk input user
        tk.Label(self.master, text="Nama Pengguna:", font=('montserrat',12, 'bold')).grid(row=row, column=0, sticky="w")
        row += 1
        tk.Entry(self.master, textvariable=self.username_var).grid(row=row, column=0, sticky="w")
        row += 1

        tk.Label(self.master, text="Nama Hotel:", font=('montserrat',12, 'bold')).grid(row=row, column=0, sticky="w")
        row += 1
        tk.Entry(self.master, textvariable=self.hotel_var).grid(row=row, column=0, sticky="w")
        row += 1

        tk.Label(self.master, text="Jumlah Kamar:", font=('montserrat',12, 'bold')).grid(row=row, column=0, sticky="w")
        row += 1
        tk.Entry(self.master, textvariable=self.room_var).grid(row=row, column=0, sticky="w")
        row += 2

        # Tombol Pesan Kamar dan exit program
        tk.Button(self.master, text="Pesan Kamar", font=('montserrat',12, 'bold'), command=self.booking).grid(row=row, column=0, columnspan=2, pady=10)
        row += 1
        tk.Button(self.master, text="Exit", font=('montserrat',12, 'bold'), command=self.master.destroy).grid(row=row, column=0, columnspan=2, pady=10)

    # tambahkan logic untuk validasi proses booking
    def booking(self):
        username = self.username_var.get()
        nama_hotel = self.hotel_var.get()
        jumlah_kamar = self.room_var.get()

        if not (username and len(username) >= 3):
            self.show_error("Nama pengguna tidak valid. Minimal 3 huruf.")
            return

        if not nama_hotel:
            self.show_error("Nama hotel tidak boleh kosong.")
            return
        
        try:
            jumlah_kamar = int(jumlah_kamar)
        except ValueError:
            self.show_error("Jumlah kamar harus berupa bilangan bulat.")
            return

        
        if jumlah_kamar <= 0:
            self.show_error("Jumlah kamar harus lebih dari 0.")
            return

        if nama_hotel not in self.dict_hotel:
            self.show_error(f"maaf, nama hotel {nama_hotel} tidak tersedia di sistem")
            return

        available_rooms, room_price, hotel_code = self.dict_hotel[nama_hotel]

        if jumlah_kamar > available_rooms:
            self.show_error(f"maaf, tidak bisa memesan kamar sebanyak {jumlah_kamar} di hotel {nama_hotel}.")
            return
        
        # memperbarui dictionary hotel
        total_cost = jumlah_kamar * room_price
        remaining_rooms = available_rooms - jumlah_kamar
        self.dict_hotel[nama_hotel][0] = remaining_rooms

        # mengosongkan variabel
        self.username_var.set("")
        self.hotel_var.set("")
        self.room_var.set(0)

        # Tampilkan pop-up pesan hasil booking
        ticket_number = f"{hotel_code}/{remaining_rooms}/{username[:3].upper()}"
        result_message = f"Booking berhasil!\npesanan untuk {username} di Hotel {nama_hotel}\nsebanyak {jumlah_kamar} kamar\nTotal Biaya: {total_cost}\nNomor Tiket: {ticket_number}"
        messagebox.showinfo("Pesan Booking", result_message)
        self.master.after(10, self.homepage)
        
    def show_error(self, message):
        messagebox.showerror("Error", message)
    
# main program
if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    
    # Load a simple GIF image (replace 'your_image.gif' with the actual filename)
    root.mainloop()