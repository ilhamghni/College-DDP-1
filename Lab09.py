from random import randint

class Person:
    def __init__(self, name, payment, stamina):
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0

    @property
    def name(self):
        return self.__name

    @property
    def payment(self):
        return self.__payment

    @property
    def stamina(self):
        return self.__stamina

    @property
    def total_work(self):
        return self.__total_work

    @stamina.setter
    def stamina(self, value):
        self.__stamina = value

    @total_work.setter

    def total_work(self, value):
        self.__total_work = value

    def is_available(self, cost_stamina):
        return self.stamina >= cost_stamina

    def pay_day(self):
        self.__payday = self.__payment * self.__total_work
        return self.__payday

    def work(self, cost_stamina):
        self.stamina -= cost_stamina
        self.total_work += 1

    def __str__(self):
        class_name = "Manager" if isinstance(self, Manager) else "Worker"
        name = self.name
        total_work = self.total_work
        stamina = self.stamina
        payment = self.payment

        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payment:20}"


class Manager(Person):
    def __init__(self, name, payment, stamina):
        super().__init__(name, payment, stamina)
        self.__list_worker = []

    @property
    def list_worker(self):
        return self.__list_worker

    def hire_worker(self, name):
        if name not in [worker.name for worker in self.__list_worker]:
            worker = Worker(name)
            self.__list_worker.append(worker)
            super().work(10)
            return True
        else:
            return False

    def fire_worker(self, name):
        for worker in self.__list_worker:
            if name == worker.name:
                self.__list_worker.remove(worker)
                super().work(10)
                print("Berhasi memecat {}".format(name))
                return True
        print("Nama tidak ditemukan")

    def give_work(self, name, bonus, cost_stamina):
        for worker in self.__list_worker:
            if worker.name == name:
                if worker.is_available(cost_stamina):
                    worker.work(bonus, cost_stamina)
                    super().work(10)
                    return
                else:
                    print("Stamina tidak mencukupi")
                    return
        print("Nama tidak ditemukan")


class Worker(Person):
    def __init__(self, name):
        super().__init__(name, 5000, 100)
        self.__bonus = 0

    def work(self, bonus, cost_stamina):
        if super().is_available(cost_stamina):
            super().work(cost_stamina)
            self.__bonus += bonus

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, new_bonus):
        self.__bonus = new_bonus


def print_employee_status(manager):
    print("Daftar Pegawai:")
    print("Manager             | {:<20} | Total kerja: {:>20} | Stamina: {:>20} | Gaji: {:>20}".format(
        manager.name, manager.total_work, manager.stamina, manager.pay_day()))
    for worker in manager.list_worker:
        print("Worker              | {:<20} | Total kerja: {:>20} | Stamina: {:>20} | Gaji: {:>20}".format(
            worker.name, worker.total_work, worker.stamina, worker.pay_day() + worker.bonus))

def main():
    name = input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    manager = Manager(name, payment, stamina)

    while manager.is_available(1):
        print("""
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """)
        action = int(input("Masukkan pilihan: "))

        if action == 1:
            print_employee_status(manager)
        
        elif action == 2:
            name = input("Tugas akan diberikan kepada: ")
            bonus = int(input("Bonus pekerjaan: "))
            cost_stamina = int(input("Beban stamina: "))
            print("Hasil cek ketersediaan pegawai:")
            if name in [worker.name for worker in manager.list_worker]:
                worker = next(worker for worker in manager.list_worker if worker.name == name)
                if worker.is_available(cost_stamina):
                    manager.give_work(name, bonus, cost_stamina)
                    print("Pegawai dapat menerima pekerjaan")
                    print("="*30)
                    print("Berhasil memberi pekerjaan kepada {}".format(name))
                else:
                    print("Pegawai tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup. ")
            else:
                print("Nama tidak ditemukan")


        elif action == 3:
            name = input("Masukkan nama pegawai baru: ")
            if manager.hire_worker(name):
                print("Berhasil menambahkan pegawai baru")
            else:
                print("Sudah ada!")


        elif action == 4:
            name = input("Masukkan nama pegawai yang ingin dipecat: ")
            manager.fire_worker(name)

        elif action == 5:
            print("""
----------------------------------------
Berhenti mengawasi hotel, sampai jumpa !
----------------------------------------""")
            return

    print("""
----------------------------------------
Stamina manajer sudah habis, sampai jumpa !
----------------------------------------""")

if __name__ == "__main__":
    main()