from random import *
import time
import requests
import datetime;
import urllib.request, urllib.parse
import simplejson as json

header_content = {'Content-type': 'application/json'} 





#print(r)


def printRoomReadings():
  randomTemp = randint(5,15);
  randomHumid = randint(5,100);
  ts = datetime.datetime.now();
  #ts.strftime("%Y-%m-%dT%H:%M:%S");
  LightData= json.dumps({'room_code':'H.4.312', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'light',
                    'humidity': randomTemp, 'light': 'true', 'people_present': 'false'})
  
  LightData= json.dumps({'room_code':'H.4.312', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'temperature': randomTemp,
                    'humidity': randomTemp, 'light': 'true', 'people_present': 'false'})
  from random import *
import time
import requests
import datetime;
import urllib.request, urllib.parse
import simplejson as json

header_content = {'Content-type': 'application/json'} 
#print(r)

def printRoomReadings():
  randomTemp = randint(5,15);
  randomHumid = randint(5,100);
  randomLight = randint(0,100);
  randomSound = randint(0,100);
  ts = datetime.datetime.now();
  
  #ts.strftime("%Y-%m-%dT%H:%M:%S");
  Device= json.dumps({'device_id': '1', 'room_code': 'WD.001.016'});
  
  
  
  LightData= json.dumps({'room_code':'WD.001.016', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'light', 'value': randomLight});
  
  TempData= json.dumps({'room_code':'WD.001.016', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'temp', 'value': randomTemp});
  
  HumidData= json.dumps({'room_code':'WD.001.016', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'humidity', 'value': randomHumid});
  
  SoundData= json.dumps({'room_code':'WD.001.016', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'type': 'sound', 'value': randomSound});
  
  #r = requests.post('http://145.24.222.238:8080/api/devices/create', data = Device, headers = header_content)
  
  l = requests.post('http://145.24.222.238:8080/api/readings/create', data = LightData, headers = header_content)
  
  t = requests.post('http://145.24.222.238:8080/api/readings/create', data = TempData, headers = header_content)
  
  h = requests.post('http://145.24.222.238:8080/api/readings/create', data = HumidData, headers = header_content)
  
  s = requests.post('http://145.24.222.238:8080/api/readings/create', data = SoundData, headers = header_content)
  
 # print("Temperature: ", randomTemp)
 # print("Humidity: ", randomHumid, "%")
  print(l)
  print(t)
  print(h)
  print(s)
  
  time.sleep(10)
  printRoomReadings()
  
printRoomReadings()
	




  LightData= json.dumps({'room_code':'H.4.312', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'temperature': randomTemp,
                    'humidity': randomTemp, 'light': 'true', 'people_present': 'false'})
  r = requests.post('http://145.24.222.238:8080/api/readings/create', data = data, headers = header_content)
  
  print("Temperature: ", randomTemp)
  print("Humidity: ", randomHumid, "%")
  
  time.sleep(10)
  printRoomReadings()
  
printRoomReadings()
	


