import pandas as pd
import psycopg2

# Lire le fichier CSV
df = pd.read_csv('/home/faye/Downloads/fichier.csv')

# Établir une connexion à la base de données
conn = psycopg2.connect(host='localhost', port='16055', database='reservation_db', user='latyr', password='latyr123')
cur = conn.cursor()

# Insérer les données dans la table
for row in df.itertuples(index=False):
    cur.execute("""
        INSERT INTO reservation_vol (image, heure_depart, heure_arrivee, duree_vol, compagnie, aeroport_depart, escale, aeroport_arrivee, prix)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, row)

# Valider les modifications et fermer la connexion
conn.commit()
cur.close()
conn.close()

