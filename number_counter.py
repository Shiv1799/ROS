#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64

class NumberCounter(Node):

    def __init__(self):
        super().__init__("number_counter")
        self.counter=0
        self.publisher_ = self.create_publisher(Int64,"number_count",10)
        self.timer_= self.create_timer(0.5,self.publish_count)
        self.get_logger().info("Publisher has started")
        self.subscribe=self.create_subscription(String,"number",self.callback_number_publisher,10)
        self.get_logger().info("smartphone has been started")
        
    def publish_count(self):
        self.counter +=1
        msg=Int64()
        msg.data=self.counter
        self.publisher_.publish(msg)

    def callback_number_publisher(self,msg):
        self.get_logger().info(msg.data)


    

def main(args=None):
    rclpy.init(args=args)
    node=NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__== "__main__":
    main()