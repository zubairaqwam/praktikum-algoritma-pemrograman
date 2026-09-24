# for 
angka = [1,2,3,4,5]

for i in angka:
    print(i)
    
# range   
angka2 = range(10)

for i in angka2:
    print(i)

angka3 = range(1,5)
for i in angka3:
    print(i)

# menggunakan string
data_str = "yuhuuuu"
for huruf in data_str:
    print(huruf)


# while
angka4 = 0 

while angka4 < 5:
    angka4 = angka4 + 1
    if(angka4 == 3):
        print(angka4)
print(f"Total perulagan: {angka4}")

# pass
while angka4 < 5:
    angka4 = angka4 + 1
    if(angka4 == 3):
        pass
print(angka4)

# Continue
while angka4 < 5:
    angka4 = angka4 + 1
    if(angka4 == 3):
        continue
    print(angka4)


#break

while angka4 < 5:
    angka4 += 1
    if angka4 == 3:
        break
    print(angka4)


#latihannn
#1. Program Menampilkan Bilangan Ganjil dan Genap (1 - 50)

for i in range(1, 51):
    if i % 2 != 0:
        print(f"Angka {i} adalah Bilangan Ganjil")
    else:
        print(f"Angka {i} adalah Bilangan Genap")

#2. Program menampilkan semua bilangan prima antara 1–100 dengan perulangan
for angka in range(2, 101):
    prima = True

    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break

    if prima:
        print(angka)