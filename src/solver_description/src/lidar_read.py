#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 


class sensor_cheking:

    def __init__(self):
        scan_topic = "/scan"
        vel_topic = "/cmd_vel"
        self.lidar_subscriber = rospy.Subscriber(scan_topic, LaserScan, self.lidar_data)
        self.vel_subscriber = rospy.Subscriber(vel_topic, Twist, self.update_robot_velocity_data)
        self.command_publisher = rospy.Publisher(vel_topic, Twist, queue_size=10)
        self.robot_linear_vel=0
    def changeLinearVel(self,vel):
            
        velo_msg = Twist() 

        # increase the current velocity by the speed defined. 
        velo_msg.linear.x = vel
        
        # publish the increased velocity 
        self.command_publisher.publish(velo_msg) 
        print('Publishing linear velocity was successful! x:', velo_msg.linear.x) 
        
        
    def changeAngularVel(self,vel):
            
        velo_msg = Twist() 

        # increase the current velocity by the speed defined. 
        velo_msg.angular.z = vel
        
        # publish the increased velocity 
        self.command_publisher.publish(velo_msg) 
        print('Publishing angular velocity was successful!', velo_msg) 
        
    def update_robot_velocity_data(self,velo_msg):
        self.robot_linear_vel=velo_msg.linear.x
        print("actual vel",self.robot_linear_vel)

    def lidar_data(self, data):
        # print("lidar:",data)
        # print("dataRanges: ",len(data.ranges))
        region_a = round(min(data.ranges[280:300]),3)
        region_b = round(min(data.ranges[301:420]),3) 
        region_c = round(min( data.ranges[421:440]),3)
        region_atr_iz = round(min( data.ranges[0:280]),3)
        region_atr_der = round(min( data.ranges[441:720]),3)
        print("A :" ,region_a , " B :", region_b , " C: ", region_c , " D: ", region_atr_iz, " E: ", region_atr_der  )
        if region_b > 2 and region_b < 30 and self.robot_linear_vel<=0:
            self.changeLinearVel(region_b)
        elif region_atr_iz > 2 and region_atr_iz <30:
            self.changeAngularVel(-3)
        elif region_atr_der > 2 and region_atr_der <30:
            self.changeAngularVel(3)
        elif region_b < 2:
            self.changeLinearVel(-0.5)
        elif region_b ==2 or region_b >30:
            self.changeLinearVel(0)
        
                



if __name__ == '__main__':
    node_name ="lidar_check"
    rospy.init_node(node_name)
    sensor_cheking()
  
    rospy.spin()