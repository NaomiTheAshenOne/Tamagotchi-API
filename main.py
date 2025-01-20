from fastapi import FastAPI
from pathlib import Path
import time, random, threading, json, time, datetime, os

#Deletes any pervious historys :,c
pathCheck = Path("historyCache")
if pathCheck.exists():
    os.remove("historyCache.txt")

#Makes a new historyCache :D
CurrentTime = datetime.datetime.now()
creationTime = str(CurrentTime)
with open("historyCache.txt", mode='w') as historyCache:
    historyCache.write(creationTime)
    historyCache.write(" A new Nami was born :3")
    
#Silly tamagotchi stat simulation :3
class tamagotchi():

    def __init__(self):
        self.name = "Nami"
        self.food = 100
        self.water = 100
        self.happiness = 50
    
    #Lowers the stats :D
    def lowerFood(self):
        while True:
            if self.food < 0:
                self.food = 0
            elif self.food > 100:
                self.food = 100
            else:
                time.sleep(10)
                self.food = self.food - 1
    def lowerWater(self):
        while True:
            if self.water < 0:
                self.water = 0
            elif self.water > 100:
                self.water = 100
            else:
                time.sleep(5)
                self.water = self.water - 1
    def lowerHappi(self):
        sadResult = 1
        while True:
            if self.happiness < 0:
                self.happiness = 0
            elif self.happiness > 100:
                self.happiness = 100

            if self.water <= 10 or self.food <= 10:
                i = 2
            if self.water <= 10 and self.food <= 10:
                i = 1
            else:
                i = 3
            time.sleep(i)
            sadResult = random.randint(1,6)
            if sadResult == 3:
                self.happiness = self.happiness - 1

    #Creates threads for each of the stat lowering defs so they always run ^0^
    def simulate(self):
        foodThread = threading.Thread(target=self.lowerFood)
        waterThread = threading.Thread(target=self.lowerWater)
        happiThread = threading.Thread(target=self.lowerHappi)

        foodThread.start()
        waterThread.start()
        happiThread.start()

class lastx():
    def __init__(self):
        self.lastfed = "never"
        self.lastdrank = "never"
        self.lastplayed = "never"

class HistoryCacheUpdate():
    
    def __init__(self, food="", drink="", play=""):
        
        #Checks which sort of item it is ;3
        if food:
            self.item = food
        elif drink:
            self.item = drink
        elif play:
            self.item = play
        self.updateHistory()

    def updateHistory(self):
        #adds what was consumed and time to the history list :3
        with open("historyCache.txt","r") as contents:
            save = contents.read()
        with open("historyCache.txt","w") as contents:
            CurrentTime = datetime.datetime.now()
            CurrentTime = str(CurrentTime)
            contents.write(CurrentTime)
            contents.write(" ")
            contents.write(self.item)
            contents.write("\n")
        with open("historyCache.txt","a") as contents:
            contents.write(save)

namigotchi = tamagotchi()
last = lastx()
namigotchi.simulate()

app = FastAPI()

@app.get('/hai')
def status():
    
    #makes happiMessage a list ^-^
    happiMessageFile = open("happiMessage.txt", "r")
    happiMessage = happiMessageFile.read() 
    happiMessage = happiMessage.split("\n") 

    if namigotchi.happiness >= 75:
            i = random.randint(0,2)
            hapMsg = happiMessage[i]
    elif namigotchi.happiness < 75 and namigotchi.happiness >= 25:
            i = random.randint(4,6)
            hapMsg = happiMessage[i]
    else:
        i = random.randint(8,10)
        hapMsg = happiMessage[i]
    
    return [
    {
        "name": namigotchi.name,
        "Birthday": creationTime,
        "food": {
            "hunger": str(namigotchi.food),
            "lastFed": last.lastfed
        },
        "water": {
            "thirst": str(namigotchi.water),
            "lastWatered": last.lastdrank
        },
        "happiness": {
            "happiScore": str(namigotchi.happiness),
            "happiMessage": hapMsg,
            "lastPlayedWith": "never - loner >:3"
        }
    }
]

@app.get('/motd')
def Motd():
    #Gives the day, i.e monday, as a number :3
    theTime = time.localtime()
    dayNum = theTime.tm_wday
    
    #Grabs the Motd from the text file :3
    motdFile = open("motd.txt", "r")
    motd = motdFile.read() 
    motd = motd.split("\n") 
    theMsg = motd[dayNum]
    
    return [
    {
        "motd": theMsg
    }
]

@app.get('/foodList')
def FoodList():
    foods = json.load(open("foods.json"))
    return [
        {
            "foods": foods
        }
]

@app.get('/drinkList')
def DrinkList():
    drinks = json.load(open("drinks.json"))
    return [
        {
            "drinks": drinks
        }
]

@app.get('/playList')
def PlayList():
    plays = json.load(open("plays.json"))
    return [
        {
            "Activities": plays
        }
]

@app.get('/history')
#History display system - shows the first 30 lines :3
def history():
    with open("historyCache.txt") as file:
        file = file.read()
        file = file.split("\n")
        lineNumber = len(file)
        file = iter(file)
        if lineNumber >= 30: 
            history = [next(file) for _ in range(30)] 
            return [
    {
        "history": history
    }
]
        else:
            history = [next(file) for _ in range(lineNumber)] 
            return [
    {
        "history": history
    }
]
            

@app.post("/scran")
def Scran(food: str):
    foodList = json.load(open("foods.json"))
    #If the food entered exists it adds the stats :D
    if food in foodList:
        foodItem = foodList[food]
        if "food" in foodItem:
            namigotchi.food = namigotchi.food + foodItem["food"]
            if namigotchi.food > 100:
                namigotchi.food = 100
            if namigotchi.food < 0:
                namigotchi.food = 0
        if "happiness" in foodItem:
            namigotchi.happiness = namigotchi.happiness + foodItem["happiness"]
            if namigotchi.happiness > 100:
                namigotchi.happiness = 100
            if namigotchi.happiness < 0:
                namigotchi.happiness = 0
        #adds what was consumed and time to the history list :3
        HistoryCacheUpdate(f"{food} was eaten :D")
        #updates last fed
        CurrentTime = datetime.datetime.now()
        CurrentTime = str(CurrentTime)
        last.lastfed = CurrentTime
        return (f"{food} was eaten :D")

    else:
        return (f"{food} not found :<")

@app.post("/hydrate")
def Hyrdrate(drink: str):
    drinkList = json.load(open("drinks.json"))
    #If the food entered exists it adds the stats :D
    if drink in drinkList:
        foodItem = drinkList[drink]
        if "water" in foodItem:
            namigotchi.water = namigotchi.water + foodItem["water"]
            if namigotchi.water > 100:
                namigotchi.water = 100
            if namigotchi.water < 0:
                namigotchi.water = 0
        if "happiness" in foodItem:
            namigotchi.happiness = namigotchi.happiness + foodItem["happiness"]
            if namigotchi.happiness > 100:
                namigotchi.happiness = 100
            if namigotchi.happiness < 0:
                namigotchi.happiness = 0
        #adds what was consumed and time to the history list :3 - MAKE THIS INTO A DEF!
        HistoryCacheUpdate(f"{drink} was drank :3")
        #updates last drank :0
        CurrentTime = datetime.datetime.now()
        CurrentTime = str(CurrentTime)
        last.lastdrank = CurrentTime
        return (f"{drink} was drank :3")

    else:
        return (f"{drink} not found :<")
    
@app.post("/play")
def PlayWith(play: str):
    playList = json.load(open("plays.json"))
    #If the food entered exists it adds the stats :D
    if play in playList:
        foodItem = playList[play]
        if "water" in foodItem:
            namigotchi.water = namigotchi.water + foodItem["water"]
            if namigotchi.water > 100:
                namigotchi.water = 100
            if namigotchi.water < 0:
                namigotchi.water = 0
        if "food" in foodItem:
            namigotchi.food = namigotchi.food + foodItem["food"]
            if namigotchi.food > 100:
                namigotchi.food = 100
            if namigotchi.food < 0:
                namigotchi.food = 0
        if "happiness" in foodItem:
            namigotchi.happiness = namigotchi.happiness + foodItem["happiness"]
            if namigotchi.happiness > 100:
                namigotchi.happiness = 100
            if namigotchi.happiness < 0:
                namigotchi.happiness = 0
        #adds what was consumed and time to the history list :3 - MAKE THIS INTO A DEF!
        HistoryCacheUpdate(f"{play} was played ^-^")
        #updates last drank :0
        CurrentTime = datetime.datetime.now()
        CurrentTime = str(CurrentTime)
        last.lastdrank = CurrentTime
        return (f"{play} was played ^-^")

    else:
        return (f"{play} not found :<")