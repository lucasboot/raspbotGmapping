#include "Adafruit_VL53L0X.h"
#include <ros.h>
#include <std_msgs/Float32.h>

Adafruit_VL53L0X lox = Adafruit_VL53L0X();
ros::NodeHandle  lidar; //inicializaco do node do microlidar
std_msgs::Float32 d;
ros::Publisher dist_pub ("distancia", &d);
void setup() {
  Serial.begin(115200);
  lidar.advertise(dist_pub);
  while (! Serial) {
    delay(1);
  }
  if (!lox.begin()) {
    while(1);
  }
}
void loop() {
  VL53L0X_RangingMeasurementData_t measure;
  lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
  if (measure.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print("Distance (mm): "); 
    Serial.println(measure.RangeMilliMeter);
    d.data = ((measure.RangeMilliMeter)/1000.0);
    dist_pub.publish(&d);
    lidar.spinOnce();
  } 
  delay(100);
}
