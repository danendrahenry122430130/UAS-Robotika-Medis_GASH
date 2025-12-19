/*
 * Proyek Robotika Medis - Sistem Kendali Buzzer ROS2
 * 
 * Program Arduino untuk mengontrol buzzer berdasarkan perintah 
 * dari ROS2 Node Subscriber melalui komunikasi serial
 * 
 * Mata Kuliah: Robotika Medis (BM25-41203)
 * Program Studi: Teknik Biomedis
 * 
 * Hardware:
 * - Arduino Uno/Nano
 * - Buzzer (passive atau active)
 * - Kabel jumper
 * 
 * Koneksi:
 * - Buzzer (+) → Pin Digital 8
 * - Buzzer (-) → GND
 * 
 * Protokol Komunikasi:
 * - Baud Rate: 9600 bps
 * - Perintah '1' = Buzzer ON (HIGH)
 * - Perintah '0' = Buzzer OFF (LOW)
 */

// Pin untuk buzzer
const int buzzerPin = 8;

void setup() {
  // Set pin buzzer sebagai output
  pinMode(buzzerPin, OUTPUT);
  
  // Inisialisasi komunikasi serial dengan baud rate 9600
  Serial.begin(9600);
  
  // Pastikan buzzer mati di awal
  digitalWrite(buzzerPin, LOW);
  
  // Indikator Arduino siap menerima perintah
  Serial.println("=================================");
  Serial.println("Arduino Buzzer Controller Ready");
  Serial.println("Waiting for ROS2 commands...");
  Serial.println("=================================");
  
  // Tes buzzer (beep singkat) untuk memastikan buzzer berfungsi
  digitalWrite(buzzerPin, HIGH);
  delay(200);
  digitalWrite(buzzerPin, LOW);
  delay(100);
  digitalWrite(buzzerPin, HIGH);
  delay(200);
  digitalWrite(buzzerPin, LOW);
  
  Serial.println("Buzzer test completed!");
}

void loop() {
  // Cek apakah ada data dari serial (dari ROS2)
  if (Serial.available() > 0) {
    // Baca karakter yang dikirim
    char data = Serial.read();
    
    // Perintah '1' = Buzzer ON
    if (data == '1') {
      digitalWrite(buzzerPin, HIGH);
      Serial.println(">>> Buzzer MENYALA");
    }
    // Perintah '0' = Buzzer OFF
    else if (data == '0') {
      digitalWrite(buzzerPin, LOW);
      Serial.println(">>> Buzzer MATI");
    }
    // Perintah tidak dikenali
    else {
      Serial.print(">>> Perintah tidak valid: ");
      Serial.println(data);
    }
  }
}
