# 🤝 Contributing Guide

Terima kasih atas minat Anda untuk berkontribusi pada proyek ini!

## 🎯 Cara Berkontribusi

### 1. Fork Repository
```bash
# Fork via GitHub UI, kemudian clone
git clone https://github.com/YOUR_USERNAME/robotika-medis-buzzer-ros2.git
cd robotika-medis-buzzer-ros2
```

### 2. Buat Branch Baru
```bash
git checkout -b feature/nama-fitur
# atau
git checkout -b fix/nama-bug
```

### 3. Buat Perubahan
- Edit file yang diperlukan
- Test perubahan Anda
- Pastikan kode berjalan tanpa error

### 4. Commit Changes
```bash
git add .
git commit -m "feat: tambah fitur XYZ"
# atau
git commit -m "fix: perbaiki bug ABC"
```

### 5. Push ke GitHub
```bash
git push origin feature/nama-fitur
```

### 6. Buat Pull Request
- Buka GitHub repository Anda
- Klik "New Pull Request"
- Jelaskan perubahan yang dibuat
- Submit PR

---

## 📝 Commit Message Convention

Gunakan format:
```
<type>: <description>

[optional body]
[optional footer]
```

### Types:
- `feat`: Fitur baru
- `fix`: Bug fix
- `docs`: Perubahan dokumentasi
- `style`: Format code (tidak mengubah logic)
- `refactor`: Refactoring code
- `test`: Menambah test
- `chore`: Maintenance

### Contoh:
```bash
git commit -m "feat: tambah support LED output"
git commit -m "fix: perbaiki koneksi serial timeout"
git commit -m "docs: update installation guide"
```

---

## 🧪 Testing

Sebelum submit PR, pastikan:
- [ ] Code bisa di-build tanpa error
- [ ] Publisher dan Subscriber berfungsi
- [ ] Dokumentasi di-update (jika perlu)
- [ ] Tidak ada syntax error

```bash
# Test build
cd ~/ros2_ws
colcon build --packages-select buzzer_keyboard

# Test run
ros2 run buzzer_keyboard keyboard_publisher  # Terminal 1
ros2 run buzzer_keyboard buzzer_subscriber   # Terminal 2
```

---

## 💡 Ideas for Contribution

Beberapa ide untuk berkontribusi:

### Features
- [ ] Web-based control interface
- [ ] Mobile app control
- [ ] Voice command input
- [ ] Pattern-based buzzer output
- [ ] Multiple output devices support
- [ ] Data logging to database
- [ ] Grafana dashboard
- [ ] ROS2 bag recording

### Improvements
- [ ] Unit tests
- [ ] Integration tests
- [ ] Performance optimization
- [ ] Better error handling
- [ ] Auto-reconnect serial
- [ ] Config file support

### Documentation
- [ ] Video tutorials
- [ ] More diagrams
- [ ] Translation (English)
- [ ] API documentation
- [ ] Deployment guide

### Bug Fixes
- Check [Issues](https://github.com/USERNAME/robotika-medis-buzzer-ros2/issues) untuk bug yang perlu diperbaiki

---

## 📋 Code Style

### Python
- Follow PEP 8
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use type hints when possible

```python
# Good
def send_command(command: str) -> bool:
    """Send command to Arduino."""
    try:
        self.ser.write(command.encode())
        return True
    except Exception as e:
        self.get_logger().error(f"Error: {e}")
        return False
```

### Arduino
- Use consistent indentation (2 spaces)
- Comment your code
- Follow Arduino naming conventions

```cpp
// Good
const int buzzerPin = 8;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}
```

---

## 📞 Questions?

Jika ada pertanyaan:
- Open an [Issue](https://github.com/USERNAME/robotika-medis-buzzer-ros2/issues)
- Email: your_email@example.com
- Discussion: [GitHub Discussions](https://github.com/USERNAME/robotika-medis-buzzer-ros2/discussions)

---

## 🙏 Thank You!

Kontribusi Anda sangat dihargai! Bersama-sama kita bisa membuat proyek ini lebih baik.

---

**Happy Coding! 🎉**
