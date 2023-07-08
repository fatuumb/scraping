import json
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="postgresql-134145-0.cloudclusters.net",
    port=16055,
    database="reservation_db",
    user="latyr",
    password="latyr123"
)


# INSERTION DES DONNEES SCRAPPES AVEC PYTHON
with open('latyr.json', 'r') as json_file:
    data = json.load(json_file)

# Iterate through the data and insert each record into the database
for item in data:
    image = item['image']
    heure_depart = item['heure_depart']
    heure_arrivee = item['heure_arrivee']
    duree_vol = item['duree_vol']
    compagnie = item['compagnie']
    aeroport_depart = item['aeroport_depart']
    escale = item['escale']
    aeroport_arrivee = item['aeroport_arrivee']
    prix = item['prix']




    # Create a cursor to execute SQL queries
    cur = conn.cursor()

    # Define the SQL query to insert the data
    sql = """
    INSERT INTO reservation_vol (image,heure_depart, heure_arrivee, duree_vol, compagnie, aeroport_depart, escale, aeroport_arrivee, prix)
    VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)
    """

    # Execute the query with the data
    cur.execute(sql, (image, heure_depart, heure_arrivee, duree_vol, compagnie, aeroport_depart, escale, aeroport_arrivee, prix))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor
    cur.close()

# Close the connection to the database
conn.close()