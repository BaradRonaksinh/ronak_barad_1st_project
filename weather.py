import requests
import json
import pyttsx3 as py3
engine = py3.init()

city = input("Enter the name of City : \n")

url = f"https://api.weatherapi.com/v1/current.json?key=0cf32d230f1c4ae094470535231806&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
cdic = json.loads(r.text)
c = cdic["current"]["condition"]["text"]

engine.say(f"the Current weather in. {city} city is. {w} degrees and air conditions is {c} ")

engine.runAndWait()



