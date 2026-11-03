# Kumpulan data numbers
data_angka = [1, 5, 2, 3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup", "adit", "siti"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "bakwan", 2, "cireng", "ucup", True, "adit", False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0, 10, 2)  # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop (list comprehension)
list_for = [i ** 2 for i in range(0, 10)]
print(list_for)

# membuat list dengan for dan if
list_for_if = [i for i in range(0, 10) if i != 5]
print(list_for_if)

list_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(list_for_if)


# index  0        1       2
# index -3       -2      -1
data = ["Ucup", "Adit", "Dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
data.insert(1, "Asep")   # data.insert(posisi, item)
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Ririn")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["Luffy", "Zoro", "Nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data (index 2 menjadi jarwo)
data[2] = "jarwo"
print(f"data rubah = \n{data}")

# menghapus data
data.remove("Ucup")
print(f"data hapus = \n{data}")

# menghapus data paling belakang
data.pop()
print(f"data akhir = \n{data}")

# slicing
nama = ["Ucup", "Adit", "Dudung", "Asep", "Ririn"]
print(nama[1:3])
print(nama[:2])
print(nama[-2:])
print(nama[::-1])


data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
print(f"data angka = \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data
data = ["Rendi", "Iqbal", "Gana", "Khairil"]
print(f"data = {data}")

index_Iqbal = data.index("Iqbal")
index_Gana = data.index("Gana")
print(f"index si Iqbal = {index_Iqbal}")
print(f"index si Gana = {index_Gana}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")


data_0 = [1, 2]
data_1 = [3, 4]
data_list_biasa = [1, 2, 3, 4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, 6, 7]
print(f"list 2D = {list_2D}")

# contoh penggunaan
peserta_0 = ["Rendi", 25, "Laki-laki"]
peserta_1 = ["Joni", 10, "Laki-laki"]
peserta_2 = ["Eka", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")



#LATIAHAN PRAKTKUM
# 1.manipulasi list
kendaraan = ["motor", "mobil", "sepeda", "bus"]

# a. Tambahkan 'truk' di akhir list
kendaraan.append("truk")
print(f"kendaraan ditambahkan {kendaraan}")

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, "becak")
print(f"kendaraan ditambahkan lagi {kendaraan}")

# c. Hapus data paling belakang
kendaraan.pop() 
print(f"kendaraan dihapus {kendaraan}")

# d. Ubah 'sepeda' menjadi 'skuter'
kendaraan[kendaraan.index('sepeda')] = 'skuter'
print(f" ubah sepeda    : {kendaraan}")

# e. Tampilkan jumlah total data
panjang_data = len(kendaraan)
print(f"panjang data kendaraan {panjang_data}\n")

# 2. Operasi pada list
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Indeks skor 100
print(f"a. Skor 100 ada di index ke-{angka.index(100)}")

# b. Jumlah siswa dengan skor 75
print(f"b. Jumlah siswa dengan skor 75 = {angka.count(75)}")

# c. Urutkan dari terkecil ke terbesar
angka.sort()
print(f"c. Setelah sort    : {angka}")

# d. Balikkan urutan
angka.reverse()
print(f"d. Setelah reverse : {angka}")

# 3. Menggabungkan list
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

menu_utama.extend(menu_tambahan)
print(f"Menu gabungan: {menu_utama}")

data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# 4. Nested List
# a. Harga Pensil
print(f"a. Harga Pensil = {data_barang[1][1]}")

# b. Menampilkan seluruh data dengan perulangan
print("b. Daftar barang:")
for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")