# 🌐 Panduan Upload ke GitHub

Panduan step-by-step untuk upload proyek ke GitHub dan membuat website dokumentasi.

---

## 📝 Prerequisites

- ✅ Akun GitHub (daftar di https://github.com jika belum punya)
- ✅ Git terinstall di Windows atau WSL

---

## 1️⃣ Install Git (Jika Belum Ada)

### Di Ubuntu WSL:
```bash
sudo apt update
sudo apt install git -y
```

### Di Windows:
Download dan install dari: https://git-scm.com/download/win

---

## 2️⃣ Konfigurasi Git

```bash
git config --global user.name "Nama Anda"
git config --global user.email "email@example.com"
```

---

## 3️⃣ Buat Repository di GitHub

1. Login ke https://github.com
2. Klik tombol **New** atau **+** (pojok kanan atas) → **New repository**
3. Isi form:
   - **Repository name**: `robotika-medis-buzzer-ros2`
   - **Description**: `Sistem Kendali Buzzer Berbasis ROS2 - Proyek Robotika Medis`
   - **Public** (agar bisa diakses dosen)
   - ✅ Centang **Add a README file** (atau jangan, karena kita sudah punya)
   - Pilih **License**: MIT License
4. Klik **Create repository**

---

## 4️⃣ Upload Project ke GitHub

### Option A: Via GitHub Web (Drag & Drop)

1. Buka repository yang baru dibuat
2. Klik **Add file** → **Upload files**
3. Drag & drop semua folder dan file dari `Tugas Robotika 2025`
4. Tambahkan commit message: `Initial commit - Proyek Robotika Medis`
5. Klik **Commit changes**

### Option B: Via Command Line (Recommended)

Di Windows PowerShell atau WSL, navigate ke folder proyek:

```bash
cd /mnt/c/Users/danen/Downloads/Tugas\ Robotika\ 2025
```

Atau di Windows PowerShell:
```powershell
cd "C:\Users\danen\Downloads\Tugas Robotika 2025"
```

Kemudian jalankan:

```bash
# 1. Initialize Git repository
git init

# 2. Add all files
git add .

# 3. Commit
git commit -m "Initial commit - Proyek Robotika Medis"

# 4. Set branch name
git branch -M main

# 5. Add remote (ganti USERNAME dan REPO)
git remote add origin https://github.com/USERNAME/robotika-medis-buzzer-ros2.git

# 6. Push to GitHub
git push -u origin main
```

**Jika diminta login:**
- Username: `username_github_anda`
- Password: Gunakan **Personal Access Token** (bukan password biasa)

### Cara Buat Personal Access Token:
1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token (classic)
4. Pilih scopes: `repo` (full control)
5. Generate dan copy token
6. Gunakan token sebagai password saat git push

---

## 5️⃣ Aktifkan GitHub Pages (Website)

Setelah push berhasil:

1. Buka repository di GitHub
2. Klik tab **Settings**
3. Scroll ke bagian **Pages** (sidebar kiri)
4. Di **Source**, pilih:
   - **Deploy from a branch**
   - **Branch**: `main`
   - **Folder**: `/ (root)`
5. Klik **Save**
6. Tunggu beberapa menit (1-5 menit)
7. Refresh halaman → akan muncul link website:
   ```
   https://username.github.io/robotika-medis-buzzer-ros2/
   ```

---

## 6️⃣ Verifikasi Website

Buka link GitHub Pages Anda. Seharusnya menampilkan isi dari `README.md`.

**Link yang bisa diberikan ke dosen:**
- **Repository**: `https://github.com/USERNAME/robotika-medis-buzzer-ros2`
- **Website**: `https://USERNAME.github.io/robotika-medis-buzzer-ros2/`
- **Dokumentasi**: `https://USERNAME.github.io/robotika-medis-buzzer-ros2/docs/`

---

## 7️⃣ Update Dokumentasi (Jika Ada Perubahan)

```bash
# 1. Edit file yang ingin diubah
# 2. Add changes
git add .

# 3. Commit dengan pesan yang jelas
git commit -m "Update: tambahkan screenshot hasil testing"

# 4. Push ke GitHub
git push
```

Website akan otomatis update dalam beberapa menit.

---

## 8️⃣ Tambahkan Badge ke README (Optional)

Edit `README.md`, tambahkan di bagian atas:

```markdown
![ROS2](https://img.shields.io/badge/ROS2-Jazzy-blue)
![Python](https://img.shields.io/badge/Python-3.10-green)
![Arduino](https://img.shields.io/badge/Arduino-Uno-teal)
![License](https://img.shields.io/badge/License-MIT-yellow)
```

---

## 9️⃣ Struktur URL GitHub Pages

Setelah aktif, URL dokumentasi Anda:

| File | URL |
|------|-----|
| README.md | `https://username.github.io/repo/` |
| docs/INSTALLATION.md | `https://username.github.io/repo/docs/INSTALLATION` |
| docs/QUICKSTART.md | `https://username.github.io/repo/docs/QUICKSTART` |
| docs/DIAGRAMS.md | `https://username.github.io/repo/docs/DIAGRAMS` |

---

## 🎨 Kustomisasi Website (Optional)

### Gunakan Jekyll Theme

1. Buat file `_config.yml` di root folder:

```yaml
theme: jekyll-theme-cayman
title: Proyek Robotika Medis
description: Sistem Kendali Buzzer Berbasis ROS2
```

2. Push ke GitHub:
```bash
git add _config.yml
git commit -m "Add Jekyll theme"
git push
```

### Theme Options:
- `jekyll-theme-cayman` (Recommended)
- `jekyll-theme-minimal`
- `jekyll-theme-slate`
- `jekyll-theme-architect`

Preview themes: https://pages.github.com/themes/

---

## 📤 Cara Submit ke Dosen

Kirimkan **2 link** berikut:

**Format email/chat:**
```
Assalamualaikum Prof/Pak,

Berikut dokumentasi proyek Robotika Medis saya:

📁 Repository GitHub:
https://github.com/USERNAME/robotika-medis-buzzer-ros2

🌐 Website Dokumentasi:
https://USERNAME.github.io/robotika-medis-buzzer-ros2/

Terima kasih.

Nama: Henry Ilviro
NIM: XXXXXXXX
```

---

## 🔧 Troubleshooting

### Problem: "remote: Repository not found"

**Solusi:**
- Cek URL remote dengan `git remote -v`
- Pastikan URL benar (username dan repo name)
- Update remote jika salah:
  ```bash
  git remote set-url origin https://github.com/USERNAME/REPO.git
  ```

### Problem: "Permission denied (publickey)"

**Solusi:**
Gunakan HTTPS instead of SSH, atau setup SSH key:
```bash
# Ganti dari SSH ke HTTPS
git remote set-url origin https://github.com/USERNAME/REPO.git
```

### Problem: GitHub Pages not showing website

**Solusi:**
1. Pastikan file `README.md` ada di root folder
2. Wait 5-10 minutes setelah setup
3. Hard refresh browser (Ctrl+Shift+R)
4. Check Settings → Pages → pastikan statusnya "Your site is live"

### Problem: "git: command not found"

**Solusi:**
```bash
sudo apt install git -y
```

---

## ✅ Checklist Upload Berhasil

- [ ] Repository berhasil dibuat di GitHub
- [ ] Semua file berhasil di-push
- [ ] GitHub Pages aktif
- [ ] Website bisa diakses (README.md tampil)
- [ ] Link repository siap dikirim ke dosen
- [ ] Link website siap dikirim ke dosen

---

## 🎯 Next Steps

Setelah upload selesai:
1. ✅ Screenshot website dan masukkan ke laporan (opsional)
2. ✅ Share link ke grup kelas (opsional)
3. ✅ Submit link ke dosen via email/LMS
4. ✅ Siap presentasi (buka website langsung saat presentasi)

---

**Selamat! Proyek Anda sudah online dan bisa diakses siapa saja! 🎉**
