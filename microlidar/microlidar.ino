#include "Adafruit_VL53L0X.h"
#include <ros.h>
#include <std_msgs/Float64.h>


Adafruit_VL53L0X lox = Adafruit_VL53L0X();


ros::NodeHandle  lidar;

std_msgs::Float64 strr_msg;
ros::Publisher microlidar("distancia", &strr_msg);

void setup() {
  Serial.begin(115200);
  lidar.initNode();
  lidar.advertise(microlidar);

  // wait until serial port opens for native USB devices
  // power 
}


void loop() {
  VL53L0X_RangingMeasurementData_t measure;
  lox.rangingTest(&measure, false); 
  if (measure.RangeStatus != 4) {  
    strr_msg.data = measure.RangeMilliMeter;
    microlidar.publish(&strr_msg);
  
  }
  lidar.spinOnce();
}
