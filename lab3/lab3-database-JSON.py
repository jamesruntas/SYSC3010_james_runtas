#!/usr/bin/env python3
import sqlite3
from urllib.request import *
from urllib.parse import *
import json

# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

city = input("Enter the name of a city whose weather you want: ")

params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
webData.close()

print (results)
data = json.loads(results)

current = data["main"]
degreeSym = chr(176)

print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
newtemp = current["temp"]

print ("Humidity: %d%%" % current["humidity"])
newhumidity = current["humidity"]

print ("Pressure: %d" % current["pressure"] )
newpressure = current["pressure"]

current = data["wind"]
print ("Wind : %d" % current["speed"])
newwind = current["speed"]

#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('''insert into weather values (newtemp, newhumidity, newpressure, newwind)''');
dbconnect.commit();
cursor.execute('SELECT * FROM weather');
dbconnect.close();