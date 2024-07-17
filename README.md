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

## Persiapan Lingkungan Pengembangan

Sebelum menjalankan aplikasi, pastikan Anda telah mengatur lingkungan virtual Python. Ikuti langkah-langkah berikut:

1. Buka terminal atau command prompt.

2. Navigasi ke direktori proyek:
   ```
   cd path/ke/direktori/proyek
   ```

3. Buat lingkungan virtual:
   ```
   python -m venv env
   ```

4. Aktifkan lingkungan virtual:
   - Untuk Windows:
     ```
     env\Scripts\activate
     ```
   - Untuk macOS dan Linux:
     ```
     source env/bin/activate
     ```

5. Setelah lingkungan virtual aktif, install dependensi yang diperlukan:
   ```
   pip install -r requirements.txt
   ```

Sekarang lingkungan pengembangan Anda siap untuk menjalankan aplikasi.