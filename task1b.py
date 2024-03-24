#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import sin

class TurtleController:
    def __init__(self):
        rospy.init_node('task1b', anonymous=True)
        self.rate=rospy.Rate(10)
        self.velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
        
    def move_in_sine_wave(self):
        amp=2
        freq=1
        angular_velocity=2*freq
        
        while not rospy.is_shutdown():
            angular_vel=angular_velocity* sin(rospy.get_time()*freq)
            twist=Twist()
            twist.linear.x=1
            twist.angular.z=angular_vel
            
            self.velocity_publisher.publish(twist)
            self.rate.sleep()
            
if __name__=='__main__':
    try:
        controller=TurtleController()
        controller.move_in_sine_wave()
    except rospy.ROSInterruptException:
        pass
        
