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

## Instalasi

1. Clone atau download project ini
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Penggunaan

1. Jalankan aplikasi:
   ```bash
   python image_upscaler.py
   ```

2. **Pilih Faktor Skala**: Pilih faktor pembesaran dari dropdown (1.25x - 2x)

3. **Pilih Gambar**:
   - **Single**: Klik "Pilih 1 Gambar" untuk memilih satu file
   - **Batch**: Klik "Pilih Multiple Gambar (Batch)" untuk memilih beberapa file sekaligus
   - **Clear**: Klik "Clear Selection" untuk menghapus pilihan

4. **Pilih Folder Output**: Klik "Browse" untuk memilih folder tempat menyimpan hasil

5. **Mulai Proses**: Klik "Mulai Upscale" untuk memulai proses

6. **Monitor Progress**: Lihat progress bar dan status untuk tracking proses

## Format File yang Didukung

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## Output

File hasil akan disimpan dengan format nama:
```
[nama_asli]_upscaled_[faktor]x.[ekstensi]
```

Contoh: `foto.jpg` dengan faktor 2x akan menjadi `foto_upscaled_2.0x.jpg`

## Fitur Teknis

- **Threading**: Proses upscale berjalan di background thread untuk menjaga responsivitas GUI
- **Error Handling**: Validasi input dan penanganan error yang komprehensif
- **Progress Tracking**: Real-time progress update untuk batch processing
- **Quality Optimization**: Menggunakan LANCZOS resampling untuk hasil terbaik
- **Memory Efficient**: Optimasi penggunaan memory untuk file besar

## Struktur Project

```
Upscale/
├── image_upscaler.py    # File aplikasi utama
├── requirements.txt     # Dependencies
└── README.md           # Dokumentasi
```

## Troubleshooting

### Error "Pilih minimal 1 gambar"
- Pastikan sudah memilih file gambar sebelum memulai proses

### Error "Pilih folder output"
- Pastikan sudah memilih folder untuk menyimpan hasil

### Error "Folder output tidak ditemukan"
- Pastikan folder yang dipilih masih ada dan dapat diakses

### Aplikasi tidak responsif
- Tunggu hingga proses selesai, terutama untuk batch processing file besar

### Kualitas hasil kurang baik
- Coba gunakan faktor skala yang lebih kecil
- Pastikan gambar input memiliki resolusi yang cukup

## Limitasi

- Faktor skala maksimum 2x untuk menjaga kualitas
- Tidak support format RAW
- Performa tergantung pada ukuran file dan spesifikasi komputer

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