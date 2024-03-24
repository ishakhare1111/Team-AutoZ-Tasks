import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(msg):
    linear_x = msg.linear.x
    angular_z = msg.angular.z
    print("Received Twist message - Linear: {}, Angular: {}".format(linear_x, angular_z))

def subscriber():
    rospy.init_node('cmd_vel_subscriber')
    rospy.Subscriber('/cmd_vel', Twist, cmd_vel_callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()

