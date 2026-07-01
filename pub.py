import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class PubNode(Node):
    def __init__(self):
        super().__init__("pub_node")
        self.publisher_=self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer=self.create_timer(1.0, self.timer_callback)
        self.count_=0

    def timer_callback(self):
        msg=Twist()
        msg.linear.x=0.0
        msg.angular.z=0.0
        if self.count_<3.01:
            msg.linear.x=5.0
            msg.angular.z=2.0
            self.count_+=1
        self.publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    pub_node=PubNode()
    rclpy.spin(pub_node)
    pub_node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
