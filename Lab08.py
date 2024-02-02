# Mendefinisikan Class Hotel
class Hotel:
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guest = set()

    def booking(self, user, num_rooms):
        if user.money >= num_rooms * self.room_price and num_rooms > 0 and num_rooms <= self.available_room:
            # Memproses booking jika kondisi terpenuhi
            user.money -= num_rooms * self.room_price
            self.profit += num_rooms * self.room_price
            self.available_room -= num_rooms
            user.hotel_list.add(self.name)
            self.guest.add(user.name)
            return True
        return False

# # Mendefinisikan Class User
class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hotel_list = set()

    def topup(self, amount):
        if amount > 0:
            # memproses top up jika kondisi terpenuhi
            self.money += amount
            return True
        return False

# Men-inisialisasi List untuk menyimpan data hotel dan user
hotels = []
users = []

# meminta input jumlah hotel dan user
num_hotels = int(input("Banyak hotel: "))
num_users = int(input("Banyak user: "))

# Input informasi hotel
for i in range(num_hotels):
    name = input(f"Masukkan Nama hotel ke-{i+1}: ")
    available_room = int(input(f"Masukkan Jumlah kamar hotel ke-{i+1}: "))
    room_price = int(input(f"Masukan harga satu kamar hotel ke-{i+1}: "))
    hotels.append(Hotel(name, available_room, room_price))

# Input informasi user
for i in range(num_users):
    name = input(f"Masukkan Nama user ke-{i+1}: ")
    money = int(input(f"Saldo User ke-{i+1}: "))
    users.append(User(name, money))

# loop for input perintah
while True:
    perintah = int(input("Masukkan nomor perintah: "))

    # Command 1: Print list dari hotel dan user
    if perintah == 1:
        print("Daftar Hotel")
        a = 1
        for hotel in hotels:
            print(f"{a}.{hotel.name}")
            a += 1
        print("Daftar User")
        b = 1
        for user in users:
            print(f"{b}.{user.name}")
            b += 1

    # Command 2: Print keuntungan hotel tertentu
    elif perintah == 2:
        hotel_name = input("Masukkan nama hotel: ")
        found = False
        for hotel in hotels:
            if hotel.name == hotel_name:
                print(f"Hotel dengan nama {hotel_name} mempunyai profit sebesar {hotel.profit}")
                found = True
                break
        if not found:
            print("Hotel tidak ditemukan.")

    # Command 3: Print saldo user tertentu
    elif perintah == 3:
        user_name = input("Masukkan nama user: ")
        found = False
        for user in users:
            if user.name == user_name:
                print(f"User dengan nama {user_name} mempunyai saldo sebesar {user.money}")
                found = True
                break
        if not found:
            print("User tidak ditemukan.")

    # Command 4: Top-up saldo user tertentu
    elif perintah == 4:
        user_name = input("Masukkan nama user: ")
        found = False
        for user in users:
            if user.name == user_name:
                amount = int(input("Masukkan saldo yang akan ditambahkan: "))
                if user.topup(amount):
                    print(f"Top up berhasil. Saldo {user.name} sekarang: {user.money}")
                else:
                    print("Top up tidak valid.")
                found = True
                break
        if not found:
            print("User tidak ditemukan.")

    # Command 5: Booking kamar untuk user tertentu di hotel tertentu
    elif perintah == 5:
        user_name = input("Masukkan nama user: ")
        hotel_name = input("Masukkan nama hotel: ")
        found_user = False
        found_hotel = False
        for user in users:
            if user.name == user_name:
                found_user = True
                for hotel in hotels:
                    if hotel.name == hotel_name:
                        found_hotel = True
                        num_rooms = int(input("Masukkan jumlah kamar yang akan dipesan: "))
                        if hotel.booking(user, num_rooms):
                            print(f"User dengan nama {user.name} berhasil melakukan booking di hotel {hotel.name} dengan jumlah {num_rooms}!")
                        else:
                            print("Booking tidak berhasil!")
                        break
                break
        if not found_user:
            print("User tidak ditemukan.")
        elif not found_hotel:
            print("Hotel tidak ditemukan.")

    # Command 6: Print tamu di hotel tertentu
    elif perintah == 6:
        hotel_name = input("Masukkan nama hotel: ")
        found = False
        for hotel in hotels:
            if hotel.name == hotel_name:
                if hotel.guest:
                    print(f"{hotel_name} | {', '.join(hotel.guest)}")
                else:
                    print(f"Hotel {hotel_name} tidak memiliki pelanggan!")
                found = True
                break
        if not found:
            print("Hotel tidak ditemukan di sistem.")

    # Command 7: Print hotel yang telah di booking user tertentu
    elif perintah == 7:
        user_name = input("Masukkan nama user: ")
        found = False
        for user in users:
            if user.name == user_name:
                if user.hotel_list:
                    print(f"{user_name} | {', '.join(user.hotel_list)}")
                else:
                    print(f"User {user_name} tidak pernah melakukan booking!")
                found = True
                break

        if not found:
            print("User tidak ditemukan di sistem.")

    # Command 8: keluar dari program
    elif perintah == 8:
        print("Terima kasih sudah mengunjungi Paciloka!")
        break

    else:
        print("Perintah tidak valid. Silakan masukkan nomor perintah yang benar.")
