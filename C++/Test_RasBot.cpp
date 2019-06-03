#include "RasBot.h"
#include <wiringPi.h>

int main(){

    RasBot robot;

    robot.moveF(80);
    delay(1000);
    robot.moveB(80);
    delay(1000);
    robot.turnL(50);
    delay(1000);
    robot.turnR(50);
    delay(1000);

    robot.stop();
    
    return 0;

}