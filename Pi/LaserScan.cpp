#include <ros/ros.h>
#include <std_msgs/Float32.h>
#include <sensor_msgs/LaserScan.h>



ros::NodeHandle  lidar; //inicializaco do node do microlidar
std_msgs::Float32 dist;
ros::Publisher scan_pub ("scan", &x);


void callback(const std_msgs::Float32& dist){
  scan.ranges[i] = dist.data;
}
void setup() {
  lidar.initNode(); //start do node
  lidar.advertise(scan_pub); 
}

void loop() {
  unsigned int num_readings = 50;
  double laser_frequency = 40;
  double ranges[num_readings];
  double intensities[num_readings];
  //ros::Rate r(1.0);
  ros::Time scan_time = ros::Time::now();
  sensor_msgs::LaserScan scan;
  scan.header.stamp = scan_time;
  scan.header.frame_id = "laser_frame";
  scan.angle_min = -1.57;
  scan.angle_max = 1.57;
  scan.angle_increment = 0.157075; //valor do incremento de cada 0.1 da lib gpiozero
  scan.time_increment = (1/laser_frequency) / (num_readings);
  scan.range_min = 0.05;
  scan.range_max = 4.00;

  for (unsigned int i = 0; i< num_readings; i++){
      ros::Subscriber scan_sub = lidar.subscribe("distancia", 1000, callback);
      scan.intensities[i] = 1;
    }
    
  }
  scan_pub.publish(&scan);
  lidar.spinOnce(); //comando para o ROS compreender que houve uma comunicacao entre topicos
}
