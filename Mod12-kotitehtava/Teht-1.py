# Moduuli 12, tehtävä 1

import requests

def hae_vitsi():
    pyynto = "https://api.chucknorris.io/jokes/random"

    # haetaan data netistä, muunnetaan se pythonin ymmärtämään muotoon
    data = requests.get(pyynto).json()

    # Palautetaan pelkkä vitsi
    return data["value"]
foo = input("Painamalla Enter saat Chuck Norris vitsin: ")

#Tulostetaan vitsi
print(hae_vitsi())
