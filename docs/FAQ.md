# 🎓 FAQ - Frequently Asked Questions

## Pertanyaan Umum tentang Proyek

### Q1: Mengapa menggunakan ROS2 dan bukan ROS1?
**A:** ROS2 lebih modern dengan fitur:
- Support real-time systems
- Security yang lebih baik
- Multi-platform (Windows, Linux, macOS)
- Better distributed communication
- Active development dan long-term support

### Q2: Apakah bisa menggunakan distribusi ROS2 selain Jazzy?
**A:** Ya, bisa menggunakan:
- **ROS2 Humble** (Ubuntu 22.04) - LTS
- **ROS2 Iron** (Ubuntu 22.04)
- **ROS2 Jazzy** (Ubuntu 24.04) - Recommended

### Q3: Apakah harus menggunakan WSL atau bisa dual boot Ubuntu?
**A:** Kedua-duanya bisa:
- **WSL** - Lebih praktis, tidak perlu restart
- **Dual Boot** - Performance lebih baik
- **Virtual Machine** - Alternatif lain (VMware/VirtualBox)

### Q4: Buzzer saya tidak bunyi, padahal kode sudah benar. Kenapa?
**A:** Cek beberapa hal:
1. **Buzzer rusak** - Coba ganti dengan LED untuk test
2. **Wiring salah** - Cek polaritas (+) dan (-)
3. **Pin salah** - Pastikan di Pin 8
4. **Arduino tidak mendapat perintah** - Cek Serial Monitor
5. **Tipe buzzer** - Active vs Passive (keduanya bisa)

### Q5: Apakah bisa menggunakan board selain Arduino Uno?
**A:** Ya, bisa:
- Arduino Nano
- Arduino Mega
- Arduino Leonardo
- ESP32 (perlu modifikasi library)
- ESP8266 (perlu modifikasi library)

### Q6: Error "Permission denied: /dev/ttyACM0". Bagaimana solusinya?
**A:** Jalankan salah satu dari:
```bash
# Temporary (untuk sekali pakai)
sudo chmod 666 /dev/ttyACM0

# Permanent (tambahkan user ke group dialout)
sudo usermod -a -G dialout $USER
# Logout dan login ulang setelah ini
```

### Q7: Apakah wajib menggunakan keyboard sebagai input?
**A:** Tidak, bisa diganti dengan:
- Joystick
- Web interface
- Mobile app
- Sensor (untuk auto trigger)
- GUI tkinter/PyQt

### Q8: Bagaimana cara mengubah baud rate serial?
**A:** Ubah di kedua tempat:
1. **Arduino** (`buzzer_control.ino`):
   ```cpp
   Serial.begin(9600);  // Ganti angka ini
   ```
2. **Python** (`buzzer_subscriber.py`):
   ```python
   self.ser = serial.Serial('/dev/ttyACM0', 9600)  # Ganti angka ini
   ```

### Q9: Apakah bisa menambahkan fitur lain seperti LED atau motor?
**A:** Sangat bisa! Tinggal:
1. Tambahkan hardware (LED/motor) ke Arduino
2. Modifikasi kode Arduino untuk kontrol pin tambahan
3. Extend protokol serial (misal: '1'=buzzer, '2'=LED, '3'=motor)

### Q10: Bagaimana cara membuat website dari dokumentasi ini?
**A:** Gunakan GitHub Pages:
```bash
# 1. Push ke GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/repo.git
git push -u origin main

# 2. Enable GitHub Pages
# - Go to repo Settings
# - Pages section
# - Source: Deploy from branch
# - Branch: main, folder: / (root)
# - Save
```

### Q11: Sistem saya delay/lambat. Bagaimana cara optimasi?
**A:** Beberapa cara:
1. **Naikkan baud rate** (9600 → 115200)
2. **Reduce logging** - Kurangi print statement
3. **Use threading** - Jalankan serial read di thread terpisah
4. **Optimize Arduino code** - Hindari delay()

### Q12: Apakah bisa menjalankan tanpa ROS2?
**A:** Bisa, tapi tidak memenuhi requirement tugas:
```python
# Simple version without ROS2
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    cmd = input("1/0: ")
    ser.write(cmd.encode())
```

### Q13: Error "colcon: command not found"
**A:** Install colcon:
```bash
sudo apt install python3-colcon-common-extensions -y
```

### Q14: Bagaimana cara test tanpa hardware Arduino?
**A:** Gunakan **Virtual Serial Port**:
- **Linux**: `socat` untuk virtual serial
- **Python**: Mock serial dengan `unittest.mock`
- **Simulation**: Gazebo + ROS2 untuk full simulation

### Q15: Apakah proyek ini bisa dikembangkan untuk aplikasi medis nyata?
**A:** Ya! Beberapa contoh pengembangan:
- **Patient Monitoring System** - Alert ketika vital signs abnormal
- **Medication Reminder** - Alarm pengingat minum obat
- **Emergency Call System** - Panic button untuk pasien
- **Medical Device Controller** - Remote control perangkat medis

### Q16: Berapa total waktu pengerjaan proyek ini?
**A:** Estimasi waktu:
- **Setup WSL + ROS2**: 1-2 jam
- **Buat package ROS2**: 1 jam
- **Kode Python**: 2 jam
- **Kode Arduino**: 30 menit
- **Testing & debugging**: 2-3 jam
- **Dokumentasi**: 2-3 jam
- **Total**: ~10-12 jam

### Q17: Apakah harus online untuk menjalankan sistem?
**A:** Tidak, sistem bisa jalan offline setelah semua terinstall.
Yang perlu internet hanya saat:
- Install ROS2
- Install dependencies (pip3 install pyserial)

### Q18: Error "ModuleNotFoundError: No module named 'rclpy'"
**A:** ROS2 belum di-source:
```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

### Q19: Bagaimana cara membuat presentasi dari proyek ini?
**A:** Gunakan struktur:
1. **Slide 1** - Judul & anggota kelompok
2. **Slide 2** - Latar belakang & tujuan
3. **Slide 3** - Arsitektur sistem (diagram)
4. **Slide 4** - Hardware & software yang digunakan
5. **Slide 5** - Demo video/live demo
6. **Slide 6** - Kendala & solusi
7. **Slide 7** - Kesimpulan & pengembangan

### Q20: Di mana saya bisa belajar ROS2 lebih lanjut?
**A:** Resources:
- **Official**: https://docs.ros.org/en/jazzy/
- **Tutorial**: https://roboticsbackend.com/
- **YouTube**: The Construct, Articulated Robotics
- **Course**: Udemy ROS2 courses
- **Community**: ROS Discourse, Reddit r/ROS

---

## 💡 Tips & Tricks

### Tip 1: Shortcut untuk Source Workspace
Tambahkan alias di `~/.bashrc`:
```bash
echo "alias ros2_source='source /opt/ros/jazzy/setup.bash && source ~/ros2_ws/install/setup.bash'" >> ~/.bashrc
source ~/.bashrc

# Sekarang tinggal ketik:
ros2_source
```

### Tip 2: Auto-restart Subscriber saat Arduino disconnect
Modifikasi `buzzer_subscriber.py` dengan try-catch loop untuk auto-reconnect.

### Tip 3: Logging ke File
```python
import logging
logging.basicConfig(filename='buzzer.log', level=logging.INFO)
```

### Tip 4: Gunakan tmux untuk Multiple Terminal
```bash
sudo apt install tmux -y
tmux new -s ros2
# Split: Ctrl+B then %
# Switch: Ctrl+B then arrow keys
```

### Tip 5: Buat Launcher Script
Create `run.sh`:
```bash
#!/bin/bash
source ~/ros2_ws/install/setup.bash
gnome-terminal -- bash -c "ros2 run buzzer_keyboard keyboard_publisher; exec bash"
gnome-terminal -- bash -c "ros2 run buzzer_keyboard buzzer_subscriber; exec bash"
```

---

Jika ada pertanyaan lain yang tidak tercantum, silakan kontak dosen atau asisten.
