#include "Adafruit_VL53L0X.h"
#include <ros.h>
#include <std_msgs/Float64.h>
#include <sensor_msgs/LaserScan.h>

Adafruit_VL53L0X lox = Adafruit_VL53L0X();


ros::NodeHandle  lidar; //inicializaco do node do microlidar
sensor_msgs::LaserScan x;
ros::Publisher scan_pub ("scan", &x);
float dist;

void setup() {
  lidar.initNode(); //start do node
  Serial.begin(9600); //rate de comunicacao do arduino
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
  scan.angle_increment = 0.174532; //valor do incremento de cada 0.1 da lib gpiozero
  scan.time_increment = (1/laser_frequency) / (num_readings);
  scan.range_min = 0.05;
  scan.range_max = 3.80;

  for (unsigned int i = 0; i< num_readings; i++){
    VL53L0X_RangingMeasurementData_t measure;
    lox.rangingTest(&measure, false); 
    if (measure.RangeStatus != 4) {  
      dist = measure.RangeMilliMeter;
      scan.ranges[i] = dist;  //publicando o valor de range lido no topico /distancia
      scan.intensities[i] = 1;
    }
    
  }
  scan_pub.publish(&scan);
  lidar.spinOnce(); //comando para o ROS compreender que houve uma comunicacao entre topicos
}
