#include "Adafruit_VL53L0X.h"
#include <ros.h>
#include <std_msgs/Float64.h>

Adafruit_VL53L0X lox = Adafruit_VL53L0X();
ros::NodeHandle  lidar; //inicializaco do node do microlidar
std_msgs::Float64 d;
ros::Publisher dist_pub ("distancia", &d);

void setup() {
  lidar.initNode();
  Serial.begin(9600);
  lidar.advertise(dist_pub);
}


void loop() {
  VL53L0X_RangingMeasurementData_t measure;
  lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!

  if (measure.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print("Distance (mm): "); 
    Serial.println(measure.RangeMilliMeter);
    d = ((measure.RangeMilliMeter)/1000.0);
    dist_pub.publish(&d);
    lidar.spinOnce();
    
  }   
  delay(100);
}
