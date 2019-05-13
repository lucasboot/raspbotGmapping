#include <ros.h>
#include <std_msgs/Int16.h>

 
//float distRoda = 7.4*3.1415;  
//int qtFendas = 20; 
int pin1 = A5;
int pin2 = A4;
int limiar = 0;
int pulsos1 = 0;
int pulsos2 = 0;

ros::NodeHandle encoder;
std_msgs::Int16 pulsosl;
std_msgs::Int16 pulsosr;
ros::Publisher lwheel_pub ("lwheel", &pulsosl);
ros::Publisher rwheel_pub ("rwheel", &pulsosr);


void setup() {
  Serial.begin(9600); 
  encoder.initNode();
  encoder.advertise(lwheel_pub);
  encoder.advertise(rwheel_pub);

}
void contador()
{
  pulsos1++;
}
void contador2(){
  pulsos2++;
}

void atualiza(int pin, int ind){
  int inSensor = analogRead(pin); 
  
  if (inSensor > limiar) {
    if(ind == 2){
      contador2();
      pulsosl.data = pulsos2;
      Serial.println(pulsos2);
      lwheel_pub.publish(&pulsosl);
    } else {
      contador();
      pulsosr.data = pulsos1;
      rwheel_pub.publish(&pulsosr);
      Serial.println(pulsos1);
    }
  }
  encoder.spinOnce();
   
}


void loop() {
  atualiza(pin1, 1);
  atualiza(pin2, 2);
  delay(100);
}
