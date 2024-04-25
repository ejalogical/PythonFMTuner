#include<stdlib.h>

#include <TEA5767Radio.h>
#include <Wire.h>;
#include <SoftwareSerial.h>
char charBuf[10];
int digitCounter=0;
boolean toggle = false;
int inputFirst[1];
int inputSecond[1];

int counter=0;
int  myCounter=0;
float  freq=87.9;
int freqCounter=0;
float freqArray[101];
TEA5767Radio radio = TEA5767Radio();
void setFrequency();
int asciiDigit[]={48,49,50,51,52,53,54,55,56,57};
 
SoftwareSerial sserial(5,6); // receive pin (used), transmit pin (unused)
void setup() {

do
{
 
dtostrf(freq, 5,1, charBuf);

 
  
freqArray[freqCounter] = atof(charBuf);

freq=freq +.2;
freqCounter=freqCounter +1;

  
}
while(freqCounter<101);



  
  Serial.begin(9600); // used for printing to serial monitor of the Arduino IDE
  sserial.begin(9600); // used to receive digits from the Java application
  while (!Serial) {
    ; // wait for serial port to connect. 
  }



  
}
void loop() {
  Wire.begin();
  
 //radio.setFrequency(freqArray[59]);
   byte incomingByte ;
   while (sserial.available() > 0) {
   
    incomingByte = sserial.read();
  Serial.print(incomingByte );
 
 if(incomingByte !=-1)
{


Wire.begin();


 radio.setFrequency(freqArray[incomingByte]);
 

Wire.begin();


}


  
}
}

 

  
 
