# Arduino Buzzer Control

Kode Arduino untuk sistem kendali buzzer berbasis ROS2.

## Hardware Requirements
- Arduino Uno/Nano/Mega
- Buzzer (passive atau active)
- Kabel jumper
- USB Cable

## Wiring Diagram
```
Arduino Pin 8  ─────────────► Buzzer (+)
Arduino GND    ─────────────► Buzzer (-)
```

## Upload Instructions

1. Buka Arduino IDE
2. File → Open → Pilih `buzzer_control.ino`
3. Tools → Board → Pilih board Arduino Anda (contoh: Arduino Uno)
4. Tools → Port → Pilih COM port yang sesuai (contoh: COM3)
5. Klik tombol Upload (→)
6. Tunggu hingga upload selesai

## Testing

Setelah upload berhasil:
1. Buka Serial Monitor (Tools → Serial Monitor)
2. Set baud rate ke **9600**
3. Ketik `1` dan Enter → Buzzer akan menyala
4. Ketik `0` dan Enter → Buzzer akan mati

## Troubleshooting

**Buzzer tidak bunyi:**
- Cek wiring/koneksi
- Pastikan buzzer tidak terbalik
- Coba ganti dengan LED untuk test
- Coba ganti buzzer (mungkin rusak)

**Arduino tidak terdeteksi:**
- Install CH340 driver (untuk Arduino clone)
- Ganti kabel USB
- Cek di Device Manager (Windows)

## Notes
- Pastikan tutup Serial Monitor sebelum menjalankan ROS2 node
- Port serial hanya bisa digunakan oleh 1 program pada saat bersamaan
