class Mahasiswa:
    def __init__(self):
        """Inisialisasi daftar mahasiswa sebagai atribut privat"""
        self.__data_mahasiswa = []

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa"""
        if self.__find_by_name(nama):
            print(f"Data mahasiswa dengan nama {nama} sudah ada.\n")
            return
        self.__data_mahasiswa.append({"nama": nama, "nilai": nilai})
        print(f"Data mahasiswa {nama} berhasil ditambahkan.\n")

    def tampilkan(self):
        """Menampilkan semua data mahasiswa"""
        if not self.__data_mahasiswa:
            print("Tidak ada data mahasiswa.\n")
        else:
            print("Daftar Nilai Mahasiswa:")
            for i, mhs in enumerate(self.__data_mahasiswa, start=1):
                print(f"{i}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")
            print()

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama"""
        mahasiswa = self.__find_by_name(nama)
        if mahasiswa:
            self.__data_mahasiswa.remove(mahasiswa)
            print(f"Data mahasiswa {nama} berhasil dihapus.\n")
        else:
            print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.\n")

    def ubah(self, nama, nilai_baru):
        """Mengubah data mahasiswa berdasarkan nama"""
        mahasiswa = self.__find_by_name(nama)
        if mahasiswa:
            mahasiswa["nilai"] = nilai_baru
            print(f"Data mahasiswa {nama} berhasil diubah.\n")
        else:
            print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.\n")

    def __find_by_name(self, nama):
        """Mencari mahasiswa berdasarkan nama"""
        for mhs in self.__data_mahasiswa:
            if mhs["nama"].lower() == nama.lower():
                return mhs
        return None


class Menu:
    def __init__(self):
        """Inisialisasi objek Mahasiswa"""
        self.mahasiswa = Mahasiswa()

    def tampilkan_menu(self):
        """Menampilkan menu utama"""
        while True:
            print("Menu:")
            print("1. Tambah Data")
            print("2. Tampilkan Data")
            print("3. Hapus Data")
            print("4. Ubah Data")
            print("5. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.__menu_tambah()
            elif pilihan == "2":
                self.mahasiswa.tampilkan()
            elif pilihan == "3":
                self.__menu_hapus()
            elif pilihan == "4":
                self.__menu_ubah()
            elif pilihan == "5":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.\n")

    def __menu_tambah(self):
        """Menu untuk menambahkan data mahasiswa"""
        nama = input("Masukkan nama mahasiswa: ")
        nilai = input("Masukkan nilai mahasiswa: ")
        self.mahasiswa.tambah(nama, nilai)

    def __menu_hapus(self):
        """Menu untuk menghapus data mahasiswa"""
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        self.mahasiswa.hapus(nama)

    def __menu_ubah(self):
        """Menu untuk mengubah data mahasiswa"""
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        nilai_baru = input("Masukkan nilai baru: ")
        self.mahasiswa.ubah(nama, nilai_baru)


# Program Utama
if __name__ == "__main__":
    menu = Menu()
    menu.tampilkan_menu()
