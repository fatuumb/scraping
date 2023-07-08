from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psycopg2
# Configuration de Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Exécuter Chrome en mode headless (sans affichage)
service = Service("path/to/chromedriver")  # Spécifier le chemin vers le chromedriver

# Lancement du navigateur
driver = webdriver.Chrome(service=service, options=chrome_options)
driver = webdriver.Chrome()
total_pages = 1
# conn = psycopg2.connect(
#     host="localhost",
#     port="5432",
#     database="reservation_db",
#     user="latyr",
#     password="latyr123"
# )
# cur = conn.cursor()


liste_vol = []

page = 1
while True:
    url = f"https://booking.kayak.com/flights/DSS,nearby-PAR/2023-08-02/2023-08-09?sort=bestflight_a&page={page}"
    driver.get(url)

    # Attente jusqu'à ce que les résultats de recherche soient chargés (vous pouvez ajuster le délai selon vos besoins)
    driver.implicitly_wait(100)

    # Extraction des informations des vols
    errors = []
    liste_image = []
    liste_heure_depart = []
    liste_heure_arrivee = []
    liste_duree_vol = []
    liste_escale = []
    liste_compagnie = []
    liste_aeroport_depart = []
    liste_aeroport_arrivee = []
    liste_prix = []

    result_cards = driver.find_elements(By.XPATH, "//*[@id='searchResultsList']")
    for card in result_cards:
        try:
            images = driver.find_elements(By.XPATH, "//div[@class='top']/img")
            for img in images:
                image_url = img.get_attribute('src')
                liste_image.append(image_url)
            heures_depart = driver.find_elements(By.XPATH, "//div[@class='top']/span[1]")
            for heure in heures_depart:
                heures_depart = heure.text.strip()
                liste_heure_depart.append(heures_depart)


            heures_arrivee = driver.find_elements(By.CSS_SELECTOR, "div > div.col-field.time.return > div.top > span")
            for heure in heures_arrivee:
                heures_arrivee = heure.text.strip()
                liste_heure_arrivee.append(heures_arrivee)


            durees_vol = driver.find_elements(By.CSS_SELECTOR, "div > div.col-field.duration > div.top")
            for heure in durees_vol:
                durees_vol = heure.text.strip()
                liste_duree_vol.append(durees_vol)

            compagnies = driver.find_elements(By.CSS_SELECTOR, "div > div.col-field.carrier > div.bottom")
            for heure in compagnies:
                compagnies = heure.text.strip()
                liste_compagnie.append(compagnies)

            #print(liste_compagnie)


            aeroports_depart = driver.find_elements(By.CSS_SELECTOR, "div > div.col-field.time.depart > div.bottom")
            for heure in aeroports_depart:
                aeroports_depart = heure.text.strip()
                liste_aeroport_depart.append(aeroports_depart)

            #print(liste_aeroport_depart)

            escales = driver.find_elements(By.XPATH, "//div[@class='bottom stops']")
            for heure in escales:
                escales = heure.text.strip()
                liste_escale.append(escales)

            #print(liste_escale)

            aeroports_arrivee = driver.find_elements(By.CSS_SELECTOR, "div > div.col-field.time.return > div.bottom")
            for heure in aeroports_arrivee:
                aeroports_arrivee = heure.text.strip()
                liste_aeroport_arrivee.append(aeroports_arrivee)

            #print( liste_aeroport_arrivee)

            prix = driver.find_elements(By.XPATH, "//span[@class='price option-text']")
            for heure in prix:
                prix = heure.text.strip()
                liste_prix.append(prix)

        #print( liste_prix)
            #print(prix)
        except Exception as e:
            errors.append({card: e})


    for image, heure_depart, heure_arrivee, duree_vol, compagnie, aeroport_depart, escale, aeroport_arrivee, prix in zip(
            liste_image, liste_heure_depart, liste_heure_arrivee, liste_duree_vol, liste_compagnie, liste_aeroport_depart,
            liste_escale, liste_aeroport_arrivee, liste_prix):
        vol = {
            "Image": image,
            "Heure_depart": heure_depart,
            "Heure_arrivee": heure_arrivee,
            "Duree_vol": duree_vol,
            "Compagnie": compagnie,
            "Aeroport_depart": aeroport_depart,
            "Escale": escale,
            "Aeroport_arrivee": aeroport_arrivee,
            "Prix": prix
        }
        liste_vol.append(vol)
    #print(liste_vol)
    # Vérification de l'existence de l'élément de pagination suivant
    #     insert_query = """
    #     INSERT INTO reservation_vol (image, heure_depart, heure_arrivee, duree_vol, compagnie, aeroport_depart, escale, aeroport_arrivee, prix)
    #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    #     """
    # cur.execute(insert_query, (image, heure_depart, heure_arrivee, duree_vol, compagnie, aeroport_depart, escale, aeroport_arrivee, prix))
    # conn.commit()
    next_button = driver.find_elements(By.CSS_SELECTOR, "#h8E-")

    if next_button:
        # Clic sur l'élément de pagination suivant
        next_button.click()

        # Attendre que la nouvelle page se charge complètement
        driver.implicitly_wait(30)

        # Incrémenter le numéro de page
        page += 1
    else:
        # Sortir de la boucle si aucun élément de pagination suivant n'est trouvé
        break

# Fermeture du navigateur
# driver.quit()
# cur.close()
# conn.close()
df = pd.DataFrame(liste_vol)
#df = pd.DataFrame(liste_vol)
#df.to_csv('/home/faye/Sonatel_Academy/fichier.csv', index=False)

print(df)

# Affichage des résultat



# Affichage des erreurs
# for vol in liste_vol:
#     print("--- vol ---")
#     print("Image :", vol["Image"])
#     print("Heure_depart :", vol["Heure_depart"])
#     print("Heure_arrivee :", vol["Heure_arrivee"])
#     print("Duree_vol :", vol["Duree_vol"])
#     print("Compagnie :", vol["Compagnie"])
#     print("Aeroport_depart :", vol["Aeroport_depart"])
#     print("Escale :", vol["Escale"])
#     print("Aeroport_arrivee :", vol["Aeroport_arrivee"])
#     print("Prix :", vol["Prix"])

