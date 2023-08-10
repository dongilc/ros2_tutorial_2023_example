import rclpy
from std_msgs.msg import String

def callback(msg):
    print("I heard: ", msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('my_subscriber')
    subscription = node.create_subscription(String,'my_topic', callback,10)
    
    try:
        rclpy.spin(node)    # keep the node running
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()