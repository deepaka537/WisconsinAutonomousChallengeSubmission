import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import random

print("tester_init")

class merge_arrays_tester(Node):
    def __init__(self):
        super().__init__("merge_arrays_tester")
        self.publisher_array_1 = self.create_publisher(Int32MultiArray, "/input/array1", 10)
        self.publisher_array_2 = self.create_publisher(Int32MultiArray, "/input/array2", 10)
        self.array1 = Int32MultiArray()
        self.array2 = Int32MultiArray()
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.publish_arrays)
        self.i = 0

    def publish_arrays(self):
        length1 = random.randint(4, 10)
        random_array1 = [random.randint(0, 100) for _ in range(length1)]
        self.array1.data = random_array1

        length2 = random.randint(4, 10)
        random_array2 = [random.randint(0, 100) for _ in range(length2)]
        self.array2.data = random_array2

        print(str(self.array1.data) + " AR1")
        print(str(self.array2.data) + " AR2")
        self.publisher_array_1.publish(self.array1)
        self.publisher_array_2.publish(self.array2)

def main(args=None):
    rclpy.init(args=args)
    node = merge_arrays_tester()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
