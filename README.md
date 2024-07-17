# Aplikasi Perhitungan Pilkada

## Deskripsi
Aplikasi ini digunakan untuk perhitungan suara dalam Pilkada.

## Fitur
- Manajemen pengguna dan peran
- Manajemen wilayah (provinsi, kabupaten/kota, kecamatan, kelurahan/desa, TPS)
- Konversi gambar ke teks
- Laporan dalam format CSV dan PDF
- Grafik real-time
- Pengujian dan debugging
- Optimasi performa dan keamanan

## Instalasi
1. Clone repositori ini
2. Install dependencies: `pip install -r requirements.txt`
3. Inisialisasi database: `flask db init`, `flask db migrate`, `flask db upgrade`
4. Jalankan aplikasi: `flask run`

## Penggunaan
- Buka `http://localhost:5000` di browser Anda
- Daftar sebagai pengguna baru
- Login dan mulai menggunakan aplikasi

## Pengujian
- Jalankan pengujian: `pytest`

## Deployment
- Konfigurasi server dan database
- Deploy aplikasi menggunakan WSGI server seperti Gunicorn
