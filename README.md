# Standalone things for DevIoT using Arduino YUN
Arduino Yun is one of the Arduino development board. It distinguishes itself from other Arduino family boards by its Wi-Fi and Ethernet connectivity. Similar to Arduino basic boards like Arduino Uno, Yun has an ATmega32u4 to control the I/O pins. It has an additional microcontroller(AR 9331) installed with OpenWRT linux operating system. However both of them can be communicated using Bridge Library.
![alt tag](https://www.arduino.cc/en/uploads/Guide/BridgeBlockDiag.png)

The main purpose of this project is demonstrating, how to connect an Arduino Yun with devIOT platform as standalone without any host.

##How to setup?

1. Build the circuit as shown below
![alt tag](https://raw.githubusercontent.com/arunmir/DevIOT_standalone_ArduinoYUN/master/circuit.png)
![alt tag](https://raw.githubusercontent.com/arunmir/DevIOT_standalone_ArduinoYUN/master/circuit_schem.png)

2. Connect the Arduino Yun with a PC using USB cable

3. Open Arduino IDE and select your board type as Arduino YUN and select the proper serial port as shown below
![alt tag](https://www.arduino.cc/en/uploads/Guide/YUN_SelBoard.jpg)
![alt tag](https://www.arduino.cc/en/uploads/Guide/YUN_SelPort.jpg)
(for more information read:https://www.arduino.cc/en/Guide/ArduinoYun#toc4)

4. Open Sketch/sketch.ino in Arduino IDE and upload the firmware for ATmega32u4 microcontroller.

5. Connect the Arduino Yun to a Wi-Fi Access point and obtain the IP address of it (Refer the documentation of Arduino Yun: https://www.arduino.cc/en/Guide/ArduinoYun#toc16)
In this tutorial IP address of the arduino was assumed as 192.168.0.6

6. Download MQTT library in your PC and copy it to Arduino YUN OpenWRT platform using SCP command from your PC
 ```
git clone https://github.com/eclipse/paho.mqtt.python.git
scp -r ./paho.mqtt.python/ root@192.168.0.6:~/
 ```
7. Replace the devIoT account in the app.py at line 42
` app = Gateway("Slider_test", "52.38.220.120:9000", "52.38.220.120:1883", "account@devIoT")`

8. Copy app.py to OpenWRT platform from PC using following SCP command
 ```
scp -r ./gateway/*  root@192.168.0.6:~/
 ```

9. Log in to the Arduino YUN openwrt platform using ssh
 ```
ssh root@192.168.0.6
 ```

10. Install MQTT library in Arduino openwrt platform
 ```
cd ./paho.mqtt.python/
python setup.py install
cd ../
 ```

11. Execute the app.py script
 ```
python app.py
 ```
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/SAnkb1BB3O0/0.jpg)](https://www.youtube.com/watch?v=SAnkb1BB3O0)
