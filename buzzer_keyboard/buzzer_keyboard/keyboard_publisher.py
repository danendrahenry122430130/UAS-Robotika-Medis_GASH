import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher_ = self.create_publisher(String, 'buzzer_cmd', 10)
        self.get_logger().info("=== KEYBOARD PUBLISHER AKTIF ===")
        self.get_logger().info("Ketik '1' untuk MENYALAKAN buzzer")
        self.get_logger().info("Ketik '0' untuk MEMATIKAN buzzer")
        self.get_logger().info("Tekan CTRL+C untuk keluar")
        self.get_logger().info("================================")

    def run(self):
        while rclpy.ok():
            try:
                cmd = input("Masukkan perintah (1/0): ")
                msg = String()
                msg.data = cmd.strip()
                self.publisher_.publish(msg)
                
                if cmd == '1':
                    self.get_logger().info("✅ Buzzer MENYALA")
                elif cmd == '0':
                    self.get_logger().info("❌ Buzzer MATI")
                else:
                    self.get_logger().warn("⚠️  Perintah tidak valid! Gunakan 1 atau 0")
                    
            except EOFError:
                break

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardPublisher()
    
    try:
        node.run()
    except KeyboardInterrupt:
        node.get_logger().info("Program dihentikan oleh user")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
