import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

print("node_init")
def mergesortpublish(self, msg):

    # This creates a queue with the arrays coming in from the topic to make sure that the array1 and array2 
    # that are meant to be processed together get processed together and published
    if (len(self.queuearray1)>1) and (len(self.queuearray2)>1):
        print(str((len(self.queuearray1))) + " 1, 2 " + str((len(self.queuearray2))))
        merged_array = sorted(self.queuearray1[0] + self.queuearray2[0])
        print(merged_array)
        merged_msg = Int32MultiArray()
        merged_msg.data = merged_array
        self.publish_array.publish(merged_msg)
        self.queuearray1.pop(0)
        self.queuearray2.pop(0)



class merge_arrays_node(Node):
    def __init__(self):
        super().__init__("merge_arrays_node")
        self.subscription_array_1 = self.create_subscription(Int32MultiArray, "/input/array1", lambda msg: self.queue1(msg), 10)
        self.subscription_array_2 = self.create_subscription(Int32MultiArray, "/input/array2", lambda msg: self.queue2(msg), 10)
        self.publish_array = self.create_publisher(Int32MultiArray, '/output/array', 10)
        self.array1 = []
        self.array2 = []
        self.operationlist = []
        self.queuearray1 = []
        self.queuearray2 = []

    # Sends all array topic data into the respective queue, where mergesortpublish processes it
    def queue1(self, msg):
        # print(str(msg.data) + " AR1")
        self.queuearray1.append(msg.data)
        mergesortpublish(self, msg)

    def queue2(self, msg):
        # print(str(msg.data) + " AR2")
        self.queuearray2.append(msg.data)
        mergesortpublish(self, msg)

def main(args=None):
    rclpy.init(args=args)
    node = merge_arrays_node()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
