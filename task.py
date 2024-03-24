#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys

def move_turtle(radius,duration):
    rospy.init_node('task', anonymous=True)
    pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate=rospy.Rate(10)
    
    vel=Twist()
    
    start=rospy.Time.now()
    
    while rospy.Time.now()-start<rospy.Duration(duration):
        vel.linear.x=radius
        
        vel.angular.z= 1
        
        pub.publish(vel)
        rate.sleep()
        
    vel.linear.x=0
    vel.angular.z=0
    pub.publish(vel)
move_turtle(2.0,6.5)
