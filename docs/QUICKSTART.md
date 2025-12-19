# 🎯 Quick Start Guide

Panduan singkat untuk menjalankan sistem setelah semua terinstall.

## Prerequisites
✅ ROS2 Jazzy sudah terinstall  
✅ Package `buzzer_keyboard` sudah di-build  
✅ Arduino sudah di-upload dengan `buzzer_control.ino`  
✅ Arduino terhubung ke WSL  

---

## 🚀 Menjalankan Sistem

### 1. Attach Arduino ke WSL (setiap restart komputer)

**Di Windows PowerShell (Admin):**
```powershell
usbipd list
usbipd attach --wsl --busid X-X
```
*Ganti X-X dengan BUSID Arduino Anda*

---

### 2. Buka 2 Terminal Ubuntu

#### Terminal 1: Publisher (Keyboard Input)
```bash
source ~/ros2_ws/install/setup.bash
ros2 run buzzer_keyboard keyboard_publisher
```

#### Terminal 2: Subscriber (Buzzer Control)
```bash
source ~/ros2_ws/install/setup.bash
ros2 run buzzer_keyboard buzzer_subscriber
```

---

### 3. Gunakan Sistem

Di **Terminal 1**, ketik:
- `1` + Enter → Buzzer MENYALA 🔊
- `0` + Enter → Buzzer MATI 🔇
- `CTRL+C` → Keluar

---

## 🔧 Quick Troubleshooting

**Arduino tidak terdeteksi:**
```bash
ls /dev/ttyACM*
sudo chmod 666 /dev/ttyACM0
```

**ROS2 command not found:**
```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

**Package not found:**
```bash
cd ~/ros2_ws
colcon build --packages-select buzzer_keyboard
source install/setup.bash
```

---

## 📊 Monitoring

**Cek topic aktif:**
```bash
ros2 topic list
```

**Monitor data di topic:**
```bash
ros2 topic echo /buzzer_cmd
```

**Cek node yang running:**
```bash
ros2 node list
```

---

Untuk panduan instalasi lengkap, lihat [INSTALLATION.md](INSTALLATION.md)
