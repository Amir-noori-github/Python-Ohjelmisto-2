# Moduuli 12, tehtävä 2
import requests

def hae_saatiedot(kaupunki):
    pyyntö = (f"https://api.openweathermap.org"
              f"/data/2.5/weather?q={kaupunki}&"
              f"appid=4b174aadb156b3d8f5da9430d3ca3eaf&units=metric&lang=fi")
    # haetaan palvelusta data
    # muutetaan se pynnön halumaan muotoon
    data = requests.get(pyyntö).json()
    #plautetaan kaikki saatu data kutsujalle
    return data

def tulosta_vastaus(data):

        saakuvaus = data["weather"][0]["description"]
        print(f"Säätilanne: {saakuvaus}")

        lämpötila = data["main"]["temp"]
        print(f"Lämpötila: {lämpötila}°C")

        tuulen_nopeus = data["wind"]["speed"]
        print(f"Tuulen nopeus: {tuulen_nopeus}")


kaupunki = input("Anna paikkakunnan nimi: ")
sää_tiedot = hae_saatiedot(kaupunki)

tulosta_vastaus(sää_tiedot)




