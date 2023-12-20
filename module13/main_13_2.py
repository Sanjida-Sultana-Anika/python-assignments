from flask import Flask, jsonify, make_response
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2358',
    autocommit=True
)
cursor = connection.cursor()


@app.route('/<icao_code>', methods=['GET'])
def get_airport_info(icao):
    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao,))
    try:
        name, location = cursor.fetchall()[0]
    except:
        result = {"ICAO": icao,
                  "message": "Invalid"}
        return make_response(result, 400)
    else:
        result = {"ICAO": icao,
                  "message": name,
                  "Location": location}
        return make_response(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
