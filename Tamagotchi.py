from flask import Flask, jsonify, request
import time, random, threading

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
            time.sleep(10)
            self.food = self.food - 1
            if self.food < 0:
                self.food = 0
    def lowerWater(self):
        while True:
            time.sleep(5)
            self.water = self.water - 1
            if self.water < 0:
                self.water = 0
    def lowerHappi(self):
        sadResult = 1
        while True:
            time.sleep(1)
            sadResult = random.randint(1,6)
            if sadResult == 3:
                self.happiness = self.happiness - 1

    #Creates threads for each of the stat lowering defs so they always run ^0^
    def simulate(self):
        foodThread = threading.Thread(target=self.lowerFood)
        waterThread = threading.Thread(target=self.lowerWater)
        HappiThread = threading.Thread(target=self.lowerHappi)

        foodThread.start()
        waterThread.start()
        HappiThread.start()
    
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

if __name__ == "__main__":
    app.run(debug=True)
