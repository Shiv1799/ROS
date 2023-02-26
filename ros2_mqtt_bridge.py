import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

import paho.mqtt.client as mqtt

class MqttPublisherNode(Node):
    def __init__(self):
        super().__init__('mqtt_publisher_node')

        qos_profile = QoSProfile(depth=10)
        self.publisher = self.create_publisher(String, 'ros2_mqtt_topic', qos_profile)
        self.subscriber = self.create_subscription(String, 'ros2_mqtt_topic', self.subscription_callback, qos_profile)

        # Connect to the MQTT broker
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect("localhost", 1883, 60)

        # Start a timer to publish the message
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = 'Hello ROS2 MQTT bridge!'
        self.publisher.publish(msg)
        self.mqtt_client.publish("ros2_mqtt_topic", msg.data)

    def subscription_callback(self, msg):
        self.get_logger().info('Received message: "{}"'.format(msg.data))

def main(args=None):
    rclpy.init(args=args)
    node = MqttPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
