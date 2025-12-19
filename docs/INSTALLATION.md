# 🚀 Panduan Instalasi Lengkap

## Sistem Kendali Buzzer Berbasis ROS2

Panduan step-by-step instalasi dan setup sistem dari awal.

---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Instalasi WSL dan Ubuntu](#instalasi-wsl-dan-ubuntu)
3. [Instalasi ROS2 Jazzy](#instalasi-ros2-jazzy)
4. [Setup Workspace ROS2](#setup-workspace-ros2)
5. [Instalasi Package](#instalasi-package)
6. [Setup Arduino](#setup-arduino)
7. [Setup USB pada WSL](#setup-usb-pada-wsl)
8. [Testing](#testing)
9. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Hardware
- ✅ Komputer dengan Windows 11 (atau Windows 10 versi 2004 ke atas)
- ✅ Arduino Uno/Nano/Mega
- ✅ Buzzer (active atau passive)
- ✅ Kabel jumper
- ✅ Kabel USB untuk Arduino
- ✅ Minimal 20GB storage kosong
- ✅ Minimal 8GB RAM (16GB recommended)

### Software
- Windows 11
- Koneksi internet
- Arduino IDE

---

## 1. Instalasi WSL dan Ubuntu

### Step 1.1: Enable WSL
Buka **PowerShell sebagai Administrator** (klik kanan → Run as Administrator)

```powershell
wsl --install
```

### Step 1.2: Restart Komputer
Restart komputer Anda setelah instalasi selesai.

### Step 1.3: Setup Ubuntu
Setelah restart:
1. Buka aplikasi **Ubuntu** dari Start Menu
2. Tunggu proses instalasi selesai (beberapa menit)
3. Buat username (contoh: `robotika`)
4. Buat password (catat baik-baik!)
5. Confirm password

### Step 1.4: Verifikasi Instalasi
```bash
lsb_release -a
```

Output yang diharapkan:
```
Distributor ID: Ubuntu
Description:    Ubuntu 24.04 LTS
Release:        24.04
Codename:       noble
```

### Step 1.5: Update System
```bash
sudo apt update
sudo apt upgrade -y
```

---

## 2. Instalasi ROS2 Jazzy

### Step 2.1: Set Locale
```bash
sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Step 2.2: Setup Sources
```bash
sudo apt install software-properties-common -y
sudo add-apt-repository universe -y
sudo apt update
sudo apt install curl -y
```

### Step 2.3: Add ROS2 GPG Key
```bash
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

### Step 2.4: Add Repository
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### Step 2.5: Install ROS2 Packages
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install ros-jazzy-desktop -y
```

**⏰ Waktu instalasi: ~10-30 menit** (tergantung koneksi internet)

### Step 2.6: Setup Environment
```bash
source /opt/ros/jazzy/setup.bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```

### Step 2.7: Install Development Tools
```bash
sudo apt install python3-colcon-common-extensions -y
sudo apt install python3-rosdep -y
sudo apt install python3-pip -y
```

### Step 2.8: Install Python Dependencies
```bash
pip3 install pyserial
```

### Step 2.9: Verify Installation
```bash
ros2 --help
```

Jika berhasil, akan muncul daftar command ROS2.

---

## 3. Setup Workspace ROS2

### Step 3.1: Create Workspace
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

### Step 3.2: Build Workspace
```bash
colcon build --executor sequential
```

### Step 3.3: Source Workspace
```bash
source ~/ros2_ws/install/setup.bash
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
```

### Step 3.4: Verify
```bash
echo $ROS_DISTRO
```
Output: `jazzy`

---

## 4. Instalasi Package

### Option A: Clone dari GitHub (Jika sudah diupload)

```bash
cd ~/ros2_ws/src
git clone https://github.com/USERNAME/buzzer_keyboard.git
cd ~/ros2_ws
colcon build --packages-select buzzer_keyboard --executor sequential
source install/setup.bash
```

### Option B: Manual Copy

1. Copy folder `buzzer_keyboard` ke `~/ros2_ws/src/`
2. Build package:

```bash
cd ~/ros2_ws
colcon build --packages-select buzzer_keyboard --executor sequential
source install/setup.bash
```

### Verify Package Installation
```bash
ros2 pkg list | grep buzzer
```
Output yang diharapkan: `buzzer_keyboard`

---

## 5. Setup Arduino

### Step 5.1: Install Arduino IDE
Download dan install dari: https://www.arduino.cc/en/software

### Step 5.2: Upload Code
1. Buka Arduino IDE
2. File → Open → Pilih file `arduino/buzzer_control.ino`
3. Tools → Board → Pilih board Anda (contoh: Arduino Uno)
4. Tools → Port → Pilih COM port (contoh: COM3)
5. Klik Upload button (→)
6. Tunggu sampai "Done uploading"

### Step 5.3: Test Serial Monitor
1. Tools → Serial Monitor
2. Set baud rate: **9600**
3. Ketik `1` → Buzzer menyala
4. Ketik `0` → Buzzer mati

✅ **Jika berhasil, lanjut ke step berikutnya**

---

## 6. Setup USB pada WSL

WSL tidak bisa langsung akses USB. Perlu tool **usbipd**.

### Step 6.1: Install usbipd di Windows

Buka **PowerShell sebagai Administrator**:

```powershell
winget install --interactive --exact dorssel.usbipd-win
```

### Step 6.2: Install usbipd tools di Ubuntu

```bash
sudo apt install linux-tools-virtual hwdata -y
sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip | tail -n1` 20
```

### Step 6.3: List USB Devices (di Windows PowerShell)

```powershell
usbipd list
```

Output contoh:
```
BUSID  VID:PID    DEVICE
1-4    2341:0043  Arduino Uno  
```

### Step 6.4: Bind Arduino (di Windows PowerShell Admin)

**Ganti `1-4` dengan BUSID Arduino Anda:**

```powershell
usbipd bind --busid 1-4
```

### Step 6.5: Attach ke WSL (setiap kali restart)

```powershell
usbipd attach --wsl --busid 1-4
```

### Step 6.6: Verify di Ubuntu

```bash
ls /dev/ttyACM*
```

Output yang diharapkan: `/dev/ttyACM0`

### Step 6.7: Set Permissions

```bash
sudo chmod 666 /dev/ttyACM0
```

---

## 7. Testing

### Test 7.1: Test Publisher Only

Terminal 1:
```bash
source ~/ros2_ws/install/setup.bash
ros2 run buzzer_keyboard keyboard_publisher
```

Ketik `1` atau `0` dan Enter.

Terminal 2 (monitor topic):
```bash
ros2 topic echo /buzzer_cmd
```

### Test 7.2: Test Full System

**Terminal 1 - Publisher:**
```bash
source ~/ros2_ws/install/setup.bash
ros2 run buzzer_keyboard keyboard_publisher
```

**Terminal 2 - Subscriber:**
```bash
source ~/ros2_ws/install/setup.bash
ros2 run buzzer_keyboard buzzer_subscriber
```

**Cara penggunaan:**
- Ketik `1` di Terminal 1 → Buzzer menyala
- Ketik `0` di Terminal 1 → Buzzer mati

### Test 7.3: Check Topics

```bash
ros2 topic list
```

Output yang diharapkan:
```
/buzzer_cmd
/parameter_events
/rosout
```

### Test 7.4: Check Nodes

```bash
ros2 node list
```

Output yang diharapkan:
```
/keyboard_publisher
/buzzer_subscriber
```

---

## 8. Troubleshooting

### Problem: "ros2: command not found"

**Solusi:**
```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

---

### Problem: "Package 'buzzer_keyboard' not found"

**Solusi:**
```bash
cd ~/ros2_ws
colcon build --packages-select buzzer_keyboard --executor sequential
source install/setup.bash
```

---

### Problem: WSL Crash saat Build

**Solusi:**
Gunakan `--executor sequential`:
```bash
colcon build --executor sequential
```

---

### Problem: Arduino tidak terdeteksi di WSL

**Solusi:**
1. Pastikan Arduino terhubung ke Windows
2. Check di Windows PowerShell (Admin):
   ```powershell
   usbipd list
   ```
3. Attach ulang:
   ```powershell
   usbipd attach --wsl --busid X-X
   ```
4. Verify di Ubuntu:
   ```bash
   ls /dev/ttyACM*
   ```

---

### Problem: Permission denied /dev/ttyACM0

**Solusi:**
```bash
sudo chmod 666 /dev/ttyACM0
```

Atau permanen:
```bash
sudo usermod -a -G dialout $USER
```
(Logout dan login ulang)

---

### Problem: ModuleNotFoundError: serial

**Solusi:**
```bash
pip3 install pyserial
```

---

### Problem: Buzzer tidak bunyi

**Solusi:**
1. Test dengan Arduino Serial Monitor dulu
2. Cek wiring hardware
3. Ganti dengan LED untuk test
4. Cek apakah buzzer rusak

---

### Problem: Node subscriber tidak menerima data

**Solusi:**
1. Pastikan kedua node running
2. Check topic:
   ```bash
   ros2 topic list
   ros2 topic echo /buzzer_cmd
   ```
3. Pastikan nama topic sama di kedua node

---

## 9. Tips & Best Practices

### 💡 Setiap kali buka Terminal baru:
```bash
source ~/ros2_ws/install/setup.bash
```

### 💡 Setiap kali restart komputer:
- Arduino perlu di-attach ulang ke WSL:
  ```powershell
  usbipd attach --wsl --busid X-X
  ```

### 💡 Setiap kali edit code:
```bash
cd ~/ros2_ws
colcon build --packages-select buzzer_keyboard --executor sequential
source install/setup.bash
```

### 💡 Hindari:
- ❌ Jangan buka Serial Monitor saat node ROS2 running
- ❌ Jangan lupa source workspace
- ❌ Jangan build parallel jika WSL crash (gunakan sequential)

---

## ✅ Checklist Instalasi Berhasil

- [ ] Ubuntu WSL terinstall dan berjalan
- [ ] ROS2 Jazzy terinstall (`ros2 --help` berfungsi)
- [ ] Workspace dibuat di `~/ros2_ws`
- [ ] Package `buzzer_keyboard` berhasil di-build
- [ ] Arduino code berhasil di-upload
- [ ] Arduino terdeteksi di WSL (`/dev/ttyACM0` ada)
- [ ] Publisher node bisa jalan
- [ ] Subscriber node bisa jalan
- [ ] Buzzer merespon perintah ON/OFF

---

## 📞 Support

Jika ada masalah yang tidak tercantum di troubleshooting, silakan:
- Cek log error dengan teliti
- Screenshot error message
- Tanyakan ke dosen atau asisten

---

**Happy Coding! 🎉**

Dokumentasi ini dibuat untuk Proyek Robotika Medis - Teknik Biomedis
