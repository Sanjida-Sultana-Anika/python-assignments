import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2358',
    autocommit=True
)
cursor = connection.cursor()
input_icao_code = input("Enter your ICAO code: ")
query = 'SELECT name, municipality FROM airport WHERE ident = %s'
cursor.execute(query, (input_icao_code,))
result = cursor.fetchone()

if result:
    airport_name, location = result
    print(f"Airport name: {airport_name}")
    print(f"Town: {location}")
else:
    print("Invalid ICAO code.")
