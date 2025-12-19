import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class BuzzerSubscriber(Node):
    def __init__(self):
        super().__init__('buzzer_subscriber')
        
        # Inisialisasi koneksi serial ke Arduino
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            time.sleep(2)  # Tunggu Arduino siap
            self.get_logger().info("✅ Koneksi ke Arduino berhasil pada /dev/ttyACM0")
        except serial.SerialException:
            try:
                self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
                time.sleep(2)
                self.get_logger().info("✅ Koneksi ke Arduino berhasil pada /dev/ttyUSB0")
            except serial.SerialException as e:
                self.get_logger().error(f"❌ Gagal koneksi ke Arduino: {e}")
                self.ser = None
        
        # Buat subscriber ke topic 'buzzer_cmd'
        self.subscription = self.create_subscription(
            String,
            'buzzer_cmd',
            self.listener_callback,
            10
        )
        
        self.get_logger().info("=== BUZZER SUBSCRIBER AKTIF ===")
        self.get_logger().info("Menunggu perintah dari Publisher...")
        self.get_logger().info("================================")

    def listener_callback(self, msg):
        """Callback yang dipanggil ketika menerima pesan"""
        command = msg.data
        
        if self.ser is None:
            self.get_logger().error("❌ Arduino tidak terhubung!")
            return
        
        try:
            if command == '1':
                self.ser.write(b'1')
                self.get_logger().info("🔊 Buzzer MENYALA - Perintah '1' diterima")
            elif command == '0':
                self.ser.write(b'0')
                self.get_logger().info("🔇 Buzzer MATI - Perintah '0' diterima")
            else:
                self.get_logger().warn(f"⚠️  Perintah tidak valid: '{command}'")
        except Exception as e:
            self.get_logger().error(f"❌ Error mengirim ke Arduino: {e}")

    def destroy_node(self):
        """Cleanup ketika node dihentikan"""
        if self.ser is not None:
            self.ser.close()
            self.get_logger().info("🔌 Koneksi serial ditutup")
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = BuzzerSubscriber()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Program dihentikan oleh user")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
