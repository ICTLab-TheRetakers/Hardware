import time
import grovepi
from grovepi import *
import datetime;
import urllib.request, urllib.parse
import simplejson as json
import requests
from grove_rgb_lcd import *
# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0
sound_sensor = 1

header_content = {'Content-type': 'application/json'} 

# Connect the LED to digital port D4
# SIG,NC,VCC,GND
led = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 10
dht_sensor_port = 7 # connect the DHt sensor to port 7
dht_sensor_type = 0

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

while True:
    try:
        # Get sensor value
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        lightsensor_value = grovepi.analogRead(light_sensor)
        soundsensor_value = grovepi.analogRead(sound_sensor)
        tem= int(temp)
        hu= int(hum)
        ts = datetime.datetime.now();
        print("temp =", temp, "C\thumidity =", hum,"%")
        # Calculate resistance of sensor in K
        #resistance = (float)(1023 - sensor_value) * 10 / (sensor_value + 0.00001)
        LightData= json.dumps({'room_code':'WD.001.016', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'light', 'value': lightsensor_value});
        TempData= json.dumps({'room_code':'WD.001.016', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'temp', 'value': tem});
        SoundData= json.dumps({'room_code':'WD.001.016', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'sound', 'value': soundsensor_value});
        HumidData= json.dumps({'room_code':'WD.001.016', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'humidity', 'value': hu});
        l = requests.post('http://145.24.222.238/api/readings/create', data = LightData, headers = header_content)
        s = requests.post('http://145.24.222.238/api/readings/create', data = SoundData, headers = header_content)
        t = requests.post('http://145.24.222.238/api/readings/create', data = TempData, headers = header_content)  
        h = requests.post('http://145.24.222.238/api/readings/create', data = HumidData, headers = header_content)
   
        print('Light', lightsensor_value)
        print('Sound', soundsensor_value)
        print(ts.strftime("%Y-%m-%dT%H:%M:%S"))
        #if resistance > threshold:
        #    # Send HIGH to switch on LED
         #   grovepi.digitalWrite(led,1)
        #else:
            # Send LOW to switch off LED
          #  grovepi.digitalWrite(led,0)

        #print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
        time.sleep(4)

    except IOError:
        print ("Error")
        
