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
input_country_code = input("Enter your area code (for example FI): ").upper()
query = "SELECT name, municipality, type FROM airport WHERE iso_country = %s ORDER BY type"
cursor.execute(query, (input_country_code,))
result = cursor.fetchall()

if result:
    print(f"Airports in {input_country_code}:")
    current_type = None
    for airport in result:
        airport_name, location, airport_type = airport
        if airport_type != current_type:
            current_type = airport_type
            print(f"{current_type} airports:")
            print(f"Airport Name: {airport_name} | Town: {location}")

else:
    print(f"No airport found for {input_country_code}")
