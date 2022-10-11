#!/usr/bin/env python2

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

class myWheel():

    def __init__(self):
        print("init_imu")
        self.o = Odometry()
        self.o.header.stamp.secs = 0
        self.o.header.stamp.nsecs = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.px = 0
        self.py = 0
        self.pz = 0
        self.image_sub = rospy.Subscriber("/realsense/imu/gyro", Imu, self.callback_SubscribeWheel)
        self.pub = rospy.Publisher("/my_robot/odom", Odometry, queue_size=1)

    def callback_SubscribeWheel(self, msg):
        print("callback_imu")
        self.o.twist.twist.angular.z = msg.angular_velocity.z
        # self.o.pose.pose.orientation.x += self.o.twist.twist.angular.x
        # self.o.pose.pose.orientation.y += self.o.twist.twist.angular.y
        # self.o.pose.pose.orientation.z += self.o.twist.twist.angular.z
        self.o.twist.twist.linear.x = 0.001*abs(msg.linear_acceleration.x)
        self.vx = self.o.twist.twist.linear.x
        # self.o.twist.twist.linear.y = self.vy + msg.linear_acceleration.y
        # self.vx = self.o.twist.twist.linear.y
        # self.o.twist.twist.linear.z = self.vz + msg.linear_acceleration.z
        # self.vx = self.o.twist.twist.linear.z
        # self.o.pose.pose.position.x = self.px + self.o.twist.twist.linear.x
        # self.px = self.o.pose.pose.position.x
        # self.o.pose.pose.position.y = self.py + self.o.twist.twist.linear.y
        # self.py = self.o.pose.pose.position.y
        # self.o.pose.pose.position.z = self.pz + self.o.twist.twist.linear.z
        # self.pz = self.o.pose.pose.position.z
        self.pub.publish(self.o)
        self.o.header.stamp.nsecs += 100000000
        if self.o.header.stamp.nsecs == 1000000000:
            self.o.header.stamp.nsecs = 0
            self.o.header.stamp.secs += 1


rospy.init_node("conversor_Imu_to_Odom")
w = myWheel()
# o = Odometry()
# o.twist.twist.angular.z = 0.015
# o.twist.twist.linear.x = 21.0
# while 1:
#     w.pub.publish(o)
rospy.spin()
