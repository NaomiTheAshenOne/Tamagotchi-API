from datetime import datetime
import time
import json

print(json.load(open("foods.json")))

#Gives the day, i.e monday, as a number :3
TheTime = time.localtime()
DayNum = TheTime.tm_wday
#Grabs the Motd from the text file :3
MotdFile = open("motd.txt", "r")
Motd = MotdFile.read() 
Motd = Motd.split("\n") 
print(Motd[DayNum])


