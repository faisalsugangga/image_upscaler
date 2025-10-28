# Image Upscaler - Aplikasi Python GUI

Aplikasi sederhana untuk melakukan upscale gambar dengan GUI interaktif menggunakan Python dan Tkinter.

## Fitur

- ✅ GUI yang user-friendly dengan Tkinter
- ✅ Upscale gambar tunggal atau batch processing
- ✅ Pilihan faktor skala: 1.25x, 1.5x, 1.75x, 2x (maksimum)
- ✅ Progress bar untuk tracking proses batch
- ✅ Validasi file gambar dan error handling
- ✅ Support multiple format: JPG, JPEG, PNG, BMP, TIFF, WebP
- ✅ Kualitas tinggi dengan algoritma LANCZOS resampling

## Requirements

- Python 3.7+
- Pillow (PIL)
- Tkinter (biasanya sudah terinstall dengan Python)
- NumPy

## Instalasi (Untuk Developer)

Langkah ini diperlukan jika Anda ingin menjalankan aplikasi dari *source code*.

1.  Clone atau download project ini.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Cara Penggunaan

### 1. Untuk Pengguna (File .exe)
Jika Anda memiliki file `upscaler.exe`, Anda tidak perlu menginstal apa pun.

1.  Cukup jalankan file `upscaler.exe` dengan melakukan *double-click*.
2.  **Pilih Faktor Skala**: Pilih faktor pembesaran dari dropdown (1.25x - 2x).
3.  **Pilih Gambar**: Klik tombol untuk memilih satu atau beberapa file gambar.
4.  **Pilih Folder Output**: Tentukan di mana hasil gambar akan disimpan.
5.  **Mulai Proses**: Klik "Mulai Upscale" untuk memulai.

### 2. Untuk Developer (Dari Source Code)
1.  Pastikan semua *requirements* sudah terinstal.
2.  Jalankan aplikasi melalui terminal:
    ```bash
    python upscaler.py
    ```
3.  Ikuti langkah-langkah yang muncul di antarmuka aplikasi.

## Membuat Versi Portabel (.exe)

Anda dapat mengubah aplikasi ini menjadi satu file `.exe` agar bisa dijalankan di komputer Windows lain tanpa perlu instalasi Python.

1.  **Instal PyInstaller dan Dependensi**:
    Pastikan Anda berada di direktori proyek dan telah menginstal semua dependensi.
    ```bash
    # Instal PyInstaller
    pip install pyinstaller

    # Instal dependensi proyek
    pip install -r requirements.txt
    ```

2.  **Jalankan Perintah PyInstaller**:
    Gunakan perintah berikut di terminal (Command Prompt atau PowerShell) untuk memulai proses.
    ```bash
    pyinstaller --onefile --windowed upscaler.py
    ```
    - `--onefile`: Mengemas semuanya ke dalam satu file `.exe`.
    - `--windowed`: Mencegah munculnya jendela konsol saat aplikasi dijalankan.

3.  **Temukan File .exe**:
    Setelah proses selesai, file `upscaler.exe` Anda akan berada di dalam folder `dist`.

## Format File yang Didukung

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## Output

File hasil akan disimpan dengan format nama:
`[nama_asli]_upscaled_[faktor]x.[ekstensi]`

Contoh: `foto.jpg` dengan faktor 2x akan menjadi `foto_upscaled_2.0x.jpg`

## Fitur Teknis

- **Threading**: Proses upscale berjalan di background thread untuk menjaga responsivitas GUI.
- **Error Handling**: Validasi input dan penanganan error yang komprehensif.
- **Progress Tracking**: Real-time progress update untuk batch processing.
- **Quality Optimization**: Menggunakan LANCZOS resampling untuk hasil terbaik.
- **Memory Efficient**: Optimasi penggunaan memory untuk file besar.

## Troubleshooting

### Error "Pilih minimal 1 gambar"
- Pastikan sudah memilih file gambar sebelum memulai proses.

### Error "Pilih folder output"
- Pastikan sudah memilih folder untuk menyimpan hasil.

### Error "Folder output tidak ditemukan"
- Pastikan folder yang dipilih masih ada dan dapat diakses.

### Aplikasi tidak responsif
- Tunggu hingga proses selesai, terutama untuk batch processing file besar.

## Limitasi

- Faktor skala maksimum 2x untuk menjaga kualitas.
- Tidak support format RAW.
- Performa tergantung pada ukuran file dan spesifikasi komputer.

## Pengembangan Selanjutnya

- [ ] Support AI-based upscaling
- [ ] Batch resize dengan dimensi custom
- [ ] Preview hasil sebelum save
- [ ] Watermark removal
- [ ] Format conversion

## Lisensi

MIT License - Bebas digunakan untuk keperluan pribadi dan komersial.

---

**Dibuat dengan ❤️ menggunakan Python & Tkinter**