#!/usr/bin/python 
__author__ = 'Arunan'

import threading
import time
import random
from DevIoTGateway.gateway import Gateway
from DevIoTGateway.sensor import Sensor,SSetting,SProperty,SAction
from DevIoTGateway.config import config

#Arduino Bridge
import sys
sys.path.insert(0, '/usr/lib/python2.7/bridge')
 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()
lock = threading.Lock()

# action name will be 'on' or 'off'
def LED_callback(sensor_id, action):
    print("action %s occur at %s " % (action.name, sensor_id))
    lock.acquire()
    if sensor_id=='BlueLED':
        if action.name =='off':
            value.put('D3','0')
        else:
            value.put('D3','1')

    if sensor_id=='YellowLED':
        if action.name =='off':
            value.put('D4','0')
        else:
            value.put('D4','1')
    lock.release()

if __name__ == '__main__':
    app_name = config.get_string("appname", "test")
    print(app_name)
    # create a gateway service instance
    # the parameters are: app name, deviot address, mq server address, deviot account
    app = Gateway("Slider_test", "52.38.220.120:9000", "52.38.220.120:1883", "account@devIoT")

    # register input sensors
    # the parameters are: sensor kind, sensor id, sensor display name
    app.register("Slider", "myslider", "Slider")

    # register some output sensors
    # don't set the  action call back function for those sensors
    app.register_action("led", "BlueLED", "BlueLED")
    app.register_action("led", "YellowLED", "YellowLED")

    # set callback for all sensors which kind is 'Pollution'
    app.register_callback_for_kind("led", LED_callback)

    # run service
    app.run()

    while True:
        # use random value to update the sensor
        # the parameters are: sensor id, new sensor value

        lock.acquire()
        PinI2State = int(float(value.get('I2')) * 20)
        print(PinI2State)
        app.set_value("myslider", PinI2State)
        lock.release()

        time.sleep(0.5)