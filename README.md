Praktikum 8

- Program ini bertujuan untuk mengelola data nilai mahasiswa menggunakan konsep class dan object,

- Pengertian Program

  Struktur Program
Program ini terdiri dari satu class bernama Mahasiswa, yang bertugas mengelola data mahasiswa seperti nama dan nilai mereka. Ada juga logika utama di bawah blok if name == "main" untuk menjalankan aplikasi secara interaktif.

Class Mahasiswa
Class ini berisi atribut dan metode sebagai berikut:

A. Atribut:

data: Sebuah dictionary (dict) untuk menyimpan data mahasiswa.
Key: Nama mahasiswa (str).
Value: Nilai mahasiswa (float).
B. Method:

init():
Konstruktor untuk menginisialisasi atribut data sebagai dictionary kosong.

tambah(nama, nilai):
Menambahkan data mahasiswa ke dalam atribut data. Jika mahasiswa sudah ada, nilainya akan diperbarui secara otomatis.

tampilkan():
Menampilkan semua data mahasiswa dalam format yang rapi. Jika tidak ada data, mencetak pesan "Tidak ada data mahasiswa."

hapus(nama):
Menghapus data mahasiswa berdasarkan nama. Jika nama tidak ditemukan, mencetak pesan "Data tidak ditemukan."

ubah(nama, nilai):
Mengubah nilai mahasiswa berdasarkan nama. Jika nama tidak ditemukan, mencetak pesan "Data tidak ditemukan."

Program Utama:
A) Menu Utama Menampilkan pilihan operasi 1. Tambah Data 2. Tampilkan Data 3. Hapus Data 4. Ubah Data 5. Keluar dari program.

B) Operasi
   - Tambah Data:
     > Meminta input nama dan nilai mahasiswa untuk ditambahkan. 
   - Tampilkan Data:
     > Menampilkan seluruh daftar mahasiswa dan nilai mereka.
   - Hapus Data:
     > Meminta input nama mahasiswa untuk menghapus data mereka.
   - Ubah Data:
     > Meminta input nama mahasiswa dan nilai baru untuk memperbarui data mereka.
   - Keluar:
     > Mengakhiri program.
C) Validasi Input: - Program memeriksa validitas input (misalnya, apakah nama ditemukan atau tidak) dan memberikan pesan yang sesuai.

Diagram Class:
+---------------------+ | Mahasiswa | +---------------------+ | - data: dict | +---------------------+ | + init() : None | | + tambah(nama: str, nilai: float) : None | | + tampilkan() : None | | + hapus(nama: str) : None | | + ubah(nama: str, nilai: float) : None | +---------------------+

diagram class
Struktur Program
Program ini terdiri dari satu class bernama Mahasiswa, yang bertugas mengelola data mahasiswa seperti nama dan nilai mereka. Ada juga logika utama di bawah blok if name == "main" untuk menjalankan aplikasi secara interaktif.

Class Mahasiswa
Class ini berisi atribut dan metode sebagai berikut:

A. Atribut:

data: Sebuah dictionary (dict) untuk menyimpan data mahasiswa.
Key: Nama mahasiswa (str).
Value: Nilai mahasiswa (float).
B. Method:

init():
Konstruktor untuk menginisialisasi atribut data sebagai dictionary kosong.

tambah(nama, nilai):
Menambahkan data mahasiswa ke dalam atribut data. Jika mahasiswa sudah ada, nilainya akan diperbarui secara otomatis.

tampilkan():
Menampilkan semua data mahasiswa dalam format yang rapi. Jika tidak ada data, mencetak pesan "Tidak ada data mahasiswa."

hapus(nama):
Menghapus data mahasiswa berdasarkan nama. Jika nama tidak ditemukan, mencetak pesan "Data tidak ditemukan."

ubah(nama, nilai):
Mengubah nilai mahasiswa berdasarkan nama. Jika nama tidak ditemukan, mencetak pesan "Data tidak ditemukan."

Program Utama:
A) Menu Utama Menampilkan pilihan operasi 1. Tambah Data 2. Tampilkan Data 3. Hapus Data 4. Ubah Data 5. Keluar dari program.

B) Operasi
   - Tambah Data:
     > Meminta input nama dan nilai mahasiswa untuk ditambahkan. 
   - Tampilkan Data:
     > Menampilkan seluruh daftar mahasiswa dan nilai mereka.
   - Hapus Data:
     > Meminta input nama mahasiswa untuk menghapus data mereka.
   - Ubah Data:
     > Meminta input nama mahasiswa dan nilai baru untuk memperbarui data mereka.
   - Keluar:
     > Mengakhiri program.
C) Validasi Input: - Program memeriksa validitas input (misalnya, apakah nama ditemukan atau tidak) dan memberikan pesan yang sesuai.

Diagram Class:
+---------------------+ | Mahasiswa | +---------------------+ | - data: dict | +---------------------+ | + init() : None | | + tambah(nama: str, nilai: float) : None | | + tampilkan() : None | | + hapus(nama: str) : None | | + ubah(nama: str, nilai: float) : None | +---------------------+


![image](https://github.com/user-attachments/assets/4c1b0d44-e6d4-4193-9ca2-82822f7c2104)

- Program
- ![Screenshot 2024-12-20 151320](https://github.com/user-attachments/assets/cd6fb1e4-b520-4dc9-a3cf-7f0172934645)
- ![Screenshot 2024-12-20 161132](https://github.com/user-attachments/assets/bae610ce-5c92-464c-9aa3-1316295e605a)

- Hasil Program
- ![Screenshot 2024-12-20 161612](https://github.com/user-attachments/assets/2865f8ec-eab0-4b6a-b92e-63ccbadc030a)
- ![Screenshot 2024-12-20 161627](https://github.com/user-attachments/assets/c38005bc-71ec-455a-89fa-bdf9781c9649)

- FlowChart
- ![image](https://github.com/user-attachments/assets/79f36f4b-f0d1-41c1-a868-30f7826ef3fd)





