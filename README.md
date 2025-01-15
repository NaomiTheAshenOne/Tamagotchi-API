# Tamagotchi-API
API for interacting with a community Tamagotchi, first time doing API stuffs :D - this is going to be a lil messy X3

## Endpoints

### Get /Hai
Gets the status of the Tamagotchi
{
  "name": str,
  "food": {
                "hunger": float,
                "lastFed": str,
                }
  "water: {
                "thirst": float,
                "lastWatered": str,
                }
  "happiness": {
                "happiScore": float,
                "happiMessage": str,
                "lastPlayedWith: str,
                }
}
### Get /History
Gets last 30 interactions

### Get /Motd
{
  "motd": str,
  }
### Get /FoodList
{
  "foods": list[str]
  }

### Post /Scran
Feeds the Tamagotchi

req-
{
  "feed": float,
  }
ies-
{
  "status": YumYum
  }


### Post /Water
Feeds the Tamagotchi
{

### Post /Play
Feeds the Tamagotchi
{

### Post /
