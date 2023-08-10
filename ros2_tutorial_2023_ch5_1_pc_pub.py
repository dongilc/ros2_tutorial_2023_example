import rclpy
from std_msgs.msg import String
import time

def talker():
    rclpy.init(args=None)
    node = rclpy.create_node('talker')
    publisher = node.create_publisher(String, 'my_topic', 10)
    msg = String()
    msg.data = 'I love MJU'
    
    while(True):
        print("publish : ",msg.data)
        publisher.publish(msg)
        time.sleep(1)

if __name__ == '__main__':
    talker()