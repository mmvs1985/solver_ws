#!/usr/bin/env python

import rospy
import cv2

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist 

class camera_1:

  def changeAngularVel(self,vel):
        
    velo_msg = Twist() 

    # increase the current velocity by the speed defined. 
    velo_msg.angular.z = vel
      
    # publish the increased velocity 
    command_publisher.publish(velo_msg) 
    print('Publishing was successful!', velo_msg) 


  def __init__(self):
    self.image_sub = rospy.Subscriber("/rrbot/camera1/image_raw", Image, self.callback)


  def callback(self,data):
    bridge = CvBridge()

    try:
      image = bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
    except CvBridgeError as e:
      rospy.logerr(e)
    
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cv_image = cv2.resize(image, (400, 300)) 

    # detect humans in input image
    (humans, _) = hog.detectMultiScale(cv_image, winStride=(10, 10), padding=(32, 32), scale=1.1)

    # getting no. of human detected
    print('Human Detected : ', humans)
    # print(humans[0])
        
    if len(humans) > 0 :
      if 300 <= humans[0][0] : 
        print( "extremo derecha")
        self.changeAngularVel(-3)
      elif 250 <= humans[0][0] <= 299 : 
        print( "derecha")
        self.changeAngularVel(-1)
      elif 150 <= humans[0][0] <= 249 : 
        print( "de frente")
        self.changeAngularVel(0)
      elif 100 <= humans[0][0] <= 149 : 
        print( "izquierda")
        self.changeAngularVel(1)
      elif humans[0][0] < 99 : 
        print( "extremo izquierda")
        self.changeAngularVel(3)

    # loop over all detected humans
    for (x, y, w, h) in humans:
      pad_w, pad_h = int(0.15 * w), int(0.01 * h)
      cv2.rectangle(cv_image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

    # display the output image
    cv2.imshow("Robot Camera", cv_image)

    cv2.waitKey(3)

    

def main():
	camera_1()
	
	try:
		rospy.spin()
	except KeyboardInterrupt:
		rospy.loginfo("Shutting down")
	
	cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('camera_read', anonymous=False)
    command_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    main()
