from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
    host='127.0.0.1',
    database='flight_game',
    user='root',
    password='3452',
)


@app.route('/kenttä/<icao>', methods=['GET'])
def get_airport(icao):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Kysely ICAO-koodilla
    cursor.execute("SELECT ident AS ICAO, name AS Name, municipality AS Municipality FROM airport WHERE ident = %s",
                   (icao,))
    airport = cursor.fetchone()

    # Suljetaan tietokantayhteys
    cursor.close()
    conn.close()

    # Tarkistetaan löytyikö lentokenttää
    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(port=3000, debug=True)

# Tulostetaa saadut vastaukset web_sivulle
#http://localhost:3000/kenttä/EFHK
#{"ICAO":"EFHK","Municipality":"Helsinki","Name":"Helsinki Vantaa Airport"}
