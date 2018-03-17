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
  
  LightData= json.dumps({'room_code':'H.4.312', 'created_on': ts.strftime("%Y-%m-%dT%H:%M:%S"), 'temperature': randomTemp,
                    'humidity': randomTemp, 'light': 'true', 'people_present': 'false'})
  r = requests.post('http://145.24.222.238:8080/api/readings/create', data = data, headers = header_content)
  
  print("Temperature: ", randomTemp)
  print("Humidity: ", randomHumid, "%")
  
  time.sleep(10)
  printRoomReadings()
  
printRoomReadings()
	


