#include <Bridge.h>
#include <stdio.h>
 
// Here we will hold the values coming from Python via Bridge.
char D4value[2];
char D3value[2];
 
void setup() {
  // Zero out the memory we're using for the Bridge.
  memset(D4value, 0, 2);
  memset(D3value, 0, 2);
   
  // Initialize digital pins 4 and 3 as output.
  pinMode(3, OUTPUT); 
  pinMode(5, OUTPUT); 
 
  // Start using the Bridge.
  Bridge.begin();
}
 
void loop() {

 // put your main code here, to run repeatedly:
  int sensorValue = analogRead(2);
  float voltage= sensorValue * (5.0 / 1023.0);
  Bridge.put("I2",String(voltage));

  // Write current value of D4 to the pin (basically turning it on or off).
  Bridge.get("D4", D4value, 2);
  int D4int = atoi(D4value);
  digitalWrite(5, D4int);
   
  // An arbitrary amount of delay to make the whole thing more reliable. YMMV
  delay(10);
   
  // Write current value of D3 to the pin (basically turning it on or off).
  Bridge.get("D3", D3value, 2);
  int D3int = atoi(D3value);
  digitalWrite(3, D3int);
   
  // An arbitrary amount of delay to make the whole thing more reliable. YMMV
  delay(10);  
}
