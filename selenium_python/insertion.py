import json
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="postgresql-134145-0.cloudclusters.net",
    port=16055,
    database="reservation_db",
    user="aissatou",
    password="passer123"
)

# INSERTION DES DONNEES SCRAPPES AVEC JAVASCRIPT
# with open('hotel_js_traite.json', 'r') as json_file:
#     data = json.load(json_file)

# INSERTION DES DONNEES SCRAPPES AVEC PYTHON
with open('hotel_python_traite.json', 'r') as json_file:
    data = json.load(json_file)

# Iterate through the data and insert each record into the database
for item in data:
    nom = item['nom']
    localisation = item['localisation']
    prix = item['prix']
    note = item['note']
    photo = item['photo']

    # Create a cursor to execute SQL queries
    cur = conn.cursor()

    # Define the SQL query to insert the data
    sql = """
    INSERT INTO hotel (nom, localisation, prix, note, photo)
    VALUES (%s, %s, %s, %s, %s)
    """

    # Execute the query with the data
    cur.execute(sql, (nom, localisation, prix, note, photo))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor
    cur.close()

# Close the connection to the database
conn.close()
