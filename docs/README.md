# Proyek Robotika Medis - Sistem Kendali Buzzer ROS2

Dokumentasi lengkap untuk tugas Robotika Medis.

## 📚 Navigasi Dokumentasi

- **[README.md](../README.md)** - Dokumentasi utama lengkap (UNTUK DOSEN)
- **[INSTALLATION.md](INSTALLATION.md)** - Panduan instalasi step-by-step
- **[QUICKSTART.md](QUICKSTART.md)** - Cara menjalankan sistem
- **[DIAGRAMS.md](DIAGRAMS.md)** - Visualisasi arsitektur sistem

## 📁 Struktur Proyek

```
Tugas Robotika 2025/
├── README.md                  # Dokumentasi lengkap
├── buzzer_keyboard/           # ROS2 Package
│   ├── buzzer_keyboard/
│   │   ├── __init__.py
│   │   ├── keyboard_publisher.py
│   │   └── buzzer_subscriber.py
│   ├── resource/
│   ├── test/
│   ├── package.xml
│   ├── setup.py
│   └── setup.cfg
├── arduino/                   # Kode Arduino
│   ├── buzzer_control.ino
│   └── README.md
└── docs/                      # Dokumentasi tambahan
    ├── INSTALLATION.md
    ├── QUICKSTART.md
    └── DIAGRAMS.md
```

## 🎯 Untuk Dosen

**Dokumentasi utama ada di [README.md](../README.md)** yang berisi:
1. ✅ Profil Anggota Kelompok
2. ✅ Pendahuluan/Pengenalan Proyek
3. ✅ Langkah-langkah Pembuatan Sistem (Hardware & Software)
4. ✅ Catatan Kendala dan Solusi
5. ✅ Kesimpulan

## 🚀 Quick Links

- [Panduan Instalasi Lengkap](INSTALLATION.md)
- [Cara Menjalankan Sistem](QUICKSTART.md)
- [Diagram Arsitektur](DIAGRAMS.md)
- [Source Code Publisher](../buzzer_keyboard/buzzer_keyboard/keyboard_publisher.py)
- [Source Code Subscriber](../buzzer_keyboard/buzzer_keyboard/buzzer_subscriber.py)
- [Kode Arduino](../arduino/buzzer_control.ino)

## 📋 Requirement Tugas

| No | Requirement | Status |
|----|-------------|--------|
| 1 | Minimal 2 node ROS2 (publisher & subscriber) | ✅ |
| 2 | Publisher menerima input dari keyboard | ✅ |
| 3 | Subscriber mengirim sinyal ke output device (buzzer) | ✅ |
| 4 | Dokumentasi online (GitHub/Website) | ✅ |
| 5 | Profil anggota kelompok | ✅ |
| 6 | Pendahuluan/pengenalan proyek | ✅ |
| 7 | Langkah-langkah pembuatan sistem | ✅ |
| 8 | Catatan kendala dan solusi | ✅ |

## 🏆 Teknologi yang Digunakan

- **ROS2 Jazzy** - Framework robotika
- **Ubuntu 24.04** - Sistem operasi (WSL)
- **Python 3** - Bahasa pemrograman
- **Arduino** - Microcontroller
- **Serial Communication** - Komunikasi hardware
- **Publisher-Subscriber Pattern** - Arsitektur sistem

## 📞 Kontak

**Nama**: Henry Ilviro  
**NIM**: XXXXXXXX  
**Program Studi**: Teknik Biomedis  
**Mata Kuliah**: Robotika Medis (BM25-41203)

---

**Tanggal Penyelesaian**: 19 Desember 2025
