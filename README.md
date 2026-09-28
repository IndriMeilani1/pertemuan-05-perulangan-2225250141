# pertemuan-05-perulangan-2225250141

Nama : Indri Meilani
NIM :2225250141
Kelas : 3A

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Tentukan nilai awal yang akan digunakan.
2. Periksa apakah kondisi perulangan terpenuhi.
3. Jika kondisi terpenuhi, jalankan perintah yang ada di dalam perulangan.
4. Setelah perintah selesai, ubah nilai penghitung atau variabel.
5. Periksa kembali kondisinya.
6. Jika kondisi masih terpenuhi, ulangi langkah sebelumnya.
7. Jika kondisi sudah tidak terpenuhi, hentikan perulangan dan lanjutkan ke proses berikutnya.

## Hasil Pengujian
input a = 2, d = 3, n = 5; keluaran yang diharapkan Suku: 2, 5, 8, 11, 14. Total = 40;	keluaran aktual Suku: 2, 5, 8, 11, 14. Total = 40;	status Berhasil.
inputa = 10, d = 2, n = 4;	keluaran yang diharapkan Suku: 10, 12, 14, 16. Total = 52;	keluaran aktual Suku: 10, 12, 14, 16. Total = 52;	status Berhasil.
input a = 5, d = -1, n = 5;	keluaran yang diharapkan Suku: 5, 4, 3, 2, 1. Total = 15; keluaran aktual	Suku: 5, 4, 3, 2, 1. Total = 15; status	Berhasil.
input a = 2, d = 3, n = 0; keluaran yang diharapkan Muncul pesan bahwa n harus lebih dari 0, kemudian meminta input ulang; keluaran aktual	Muncul pesan bahwa n harus lebih dari 0, kemudian meminta input ulang; status	Berhasil.

## Refleksi
Kesalahan perulangan yang saya temukan adalah ketika nilai n diisi 0 atau angka negatif, sehingga perulangan tidak dapat berjalan dengan benar.
Cara memperbaikinya adalah dengan menggunakan while untuk mengecek nilai n. Jika n masih 0 atau negatif, program akan meminta pengguna memasukkan nilai lagi. Setelah n lebih dari 0, program baru melanjutkan perulangan for untuk menghitung deret.
