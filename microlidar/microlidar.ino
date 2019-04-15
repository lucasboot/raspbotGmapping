#include "Adafruit_VL53L0X.h"
#include <ros.h>
#include <std_msgs/Float64.h>


Adafruit_VL53L0X lox = Adafruit_VL53L0X();


ros::NodeHandle  lidar; //inicializaco do node do microlidar

std_msgs::Float64 strr_msg; //declaracao do tipo da variavel de distancia
ros::Publisher microlidar("distancia", &strr_msg); //criacao do publisher, com o tipo da variavel criada referenciado

void setup() {
  Serial.begin(9600); //rate de comunicacao do arduino
  lidar.initNode(); //start do node
  lidar.advertise(microlidar); //definicao do publisher do node
}


void loop() {
  VL53L0X_RangingMeasurementData_t measure;
  lox.rangingTest(&measure, false); 
  if (measure.RangeStatus != 4) {  
    strr_msg.data = measure.RangeMilliMeter;
    microlidar.publish(&strr_msg); //publicando o valor de range lido no topico /distancia
    
  }
  lidar.spinOnce(); //comando para o ROS compreender que houve uma comunicacao entre topicos
  delay(100);
}
