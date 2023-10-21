import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2358',
    autocommit=True
)

cursor = connection.cursor()
user_input1 = input("Enter ICAO code of airport 1: ").upper()
user_input2 = input("Enter ICAO code of airport 2: ").upper()
query1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
query2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(query1, (user_input1,))
result1 = cursor.fetchone()
cursor.execute(query2, (user_input2,))
result2 = cursor.fetchone()

if result1 and result2:
    lati1, long1 = result1
    lati2, long2 = result2
    location1 = (lati1, long1)
    location2 = (lati2, long2)
    distance = geodesic(location1, location2).kilometers
    print(f"The distance between them is {distance:.2f} kilometers")
else:
    print("Error. Enter correct ICAO code/s.")
