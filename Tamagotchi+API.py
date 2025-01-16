from flask import Flask
import time, random, threading, jsonify, json, time

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
            else:
                time.sleep(1)
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
    
    #Currently just a debug output :P
    def interface(self):
        while True:
            print(f"Food: {self.food}")
            print(f"Water: {self.water}")
            print(f"Happi: {self.happiness}")

namigotchi = tamagotchi()
namigotchi.simulate()
#namigotchi.interface()
app = Flask(__name__)

@app.route('/Hai', methods=["GET"])
def status():
    return [
    {
        "name": namigotchi.name,
        "food": {
            "hunger": str(namigotchi.food),
            "lastFed": "never :3"
        },
        "water": {
            "thirst": str(namigotchi.water),
            "lastWatered": "your meant to water them?!?!?!"
        },
        "happiness": {
            "happiScore": str(namigotchi.happiness),
            "happiMessage": "gay :3",
            "lastPlayedWith": "never - loner >:3"
        }
    }
]

@app.route('/Motd', methods=["GET"])
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

@app.route('/FoodList', methods=["GET"])
def FoodList():
    return [
    {
        "foods": "food go here lol"       #list[str]
    }
]

#@app.route('/Play', methods=["POST"])
#def Play():

if __name__ == "__main__":
    app.run(debug=True)
