# Moduuli 13, tehtävä 1

from flask import Flask, request

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def onAlkuluku(luku):
    onAlku = True

    if luku < 2:
        onAlku = False

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            onAlku = False
            break

    vastaus = {
            "Number": luku,
            "isPrime": onAlku
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

# Tulostetaa saadut vastaukset web_sivulle
#http://localhost:3000/alkuluku/31
# {"Number":31,"isPrime":true}
