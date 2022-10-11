#!/usr/bin/env python2

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage

class myCamera():

    def __init__(self):
        print("init_camera")
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/realsense/rgb", Image, self.callback_SubscribeCamera)
        self.pub = rospy.Publisher("/my_robot/camera/image/compressed", CompressedImage, queue_size=1)

    def callback_SubscribeCamera(self, msg):
        print("callback_camera")
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.compressed_image = self.bridge.cv2_to_compressed_imgmsg(self.cv_image, "jpeg")
        except CvBridgeError as e:
            print(e)

        self.pub.publish(self.compressed_image)
        # print(self.cv_image[0][0])
        # print(self.cv_image[0][0][0])

        # cv2.imshow("raw", self.cv_image)
        # cv2.waitKey(3)

rospy.init_node("conversor_Image_to_Compressed")
c = myCamera()

rospy.spin()
