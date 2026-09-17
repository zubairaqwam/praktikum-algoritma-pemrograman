# pertemuan ke 4
# not (membalikkan nilai)
a = True
b = not a
print(b)

# or (benar jika salah satu benar)
a = False
b = True
c = a or b
print(c)

# and (akan bernilai benar jika keduanya True)
a = True
b = False
c = a and b
print(c)

# xor ( benar jika kedua nilai berbeda)
a = True
b = False
c = a ^ b
print(c)

latihan logika Komparasi
#+++++++3--------10+++++++
angka = int(input("Masukan angka : "))
IsKurangDari = angka < 3
IsLebihDari = angka > 10
hasil = IsKurangDari or IsLebihDari
print(hasil)

latihan logika Komparasi
#+++++++3--------10+++++++
angka = int(input("Masukan angka : "))
IsKurangDari = angka > 3
IsLebihDari = angka < 10
hasil = IsKurangDari and IsLebihDari
print(hasil)

# if-else
nama = input("Masukkan Nama :")
if nama == "paijo":
    print("hai paijo, si keren!")
else:
    print("ah kamu bukan paijo, kamu gak keren")

# ELIF = else if statement
nama = input("Masukkan Nama:")
if nama == "dhani":
    print("hai kece parahh!!!")
elif nama == "hanip":
    print("hai sok asik!!!")
elif nama == "farid":
    print("hai baperan!!!")
else:
    print("sorry ga kenal!!!")


# TUGAS PRAKTIKUM
# LATIHAN

# meminta usia dari pengguna
usia = int(input("Masukkan usia anda: "))

# kondisi pertama: usia 0-12 tahun masuk kategori Anak-anak
if usia <= 12:
    print("Kategori usia: Anak-anak")

# jika kondisi pertama tidak terpenuhi, periksa kondisi kedua: 13-17 tahun
elif usia <= 17:
    print("Kategori usia: Remaja")

# jika dua kondisi di atas tidak terpenuhi, periksa kondisi ketiga: 18-59 tahun
elif usia <= 59:
    print("Kategori usia: Dewasa")

# usia lansia
else:
    print("Kategori usia: Lansia")