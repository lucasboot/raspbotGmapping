//Programa: Sensor de velocidade Arduino LM393
//Autor: Arduino e Cia
#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  encoder; //inicializaco do node do microlidar
std_msgs::Int16 pulsosl;
std_msgs::Int16 pulsosr;
ros::Publisher lwheel_pub ("lwheel", &pulsosl);
ros::Publisher rwheel_pub ("rwheel", &pulsosr);


//Pino ligado ao pino D0 do sensor
int pino_D0 = 2;
int pino_D1 = 3;
volatile byte pulsos;
volatile byte pulsos2;
unsigned long timeold;


void contador()
{
  //Incrementa contador
  pulsos++;
}
void contador2(){
  pulsos2++;
}

void setup()
{
  Serial.begin(9600);
  encoder.advertise(lwheel_pub);
  encoder.advertise(rwheel_pub);
  //Pino do sensor como entrada
  pinMode(pino_D0, INPUT);
  pinMode(pino_D1, INPUT);
  //Interrupcao 0 - pino digital 2
  //Aciona o contador a cada pulso
  attachInterrupt(digitalPinToInterrupt(pino_D0), contador, FALLING);
  attachInterrupt(digitalPinToInterrupt(pino_D1), contador2, FALLING);
  pulsos = 0;
  pulsos2 = 0;
  timeold = 0;
}

void loop()
{
  //Atualiza contador a cada segundo
  if (millis() - timeold >= 1000)
  {
    //Desabilita interrupcao durante o calculo
    detachInterrupt(digitalPinToInterrupt(pino_D0));
    detachInterrupt(digitalPinToInterrupt(pino_D1));
    pulsosl.data = pulsos;
    pulsosr.data = pulsos2;
    lwheel_pub.publish(&pulsosl);
    rwheel_pub.publish(&pulsosr);
    encoder.spinOnce();
    timeold = millis();
    //Habilita interrupcao
    attachInterrupt(digitalPinToInterrupt(pino_D0), contador, FALLING);
    attachInterrupt(digitalPinToInterrupt(pino_D1), contador2, FALLING);
  }
}
