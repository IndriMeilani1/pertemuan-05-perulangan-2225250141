print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi n harus lebih dari 0
while n <= 0:
    print("Banyak suku harus lebih dari 0!")
    n = int(input("Masukkan banyak suku n lagi: "))

# Menampilkan suku dan menghitung total
total = 0

for i in range(1, n + 1):
    suku = a + (i - 1) * d
    print(f"Suku ke-{i} = {suku}")
    total += suku

print(f"Total jumlah deret = {total}")
