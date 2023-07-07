from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Firefox()  
driver.get("https://www.kayak.fr/hotels/Senegal-u213/2023-07-05/2023-07-06/2adults?sort=rank_a&attempt=1&lastms=1688480005082&force=true")

wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.kzGk-resultInner')))
cards = driver.find_elements(By.CSS_SELECTOR, 'div.kzGk-resultInner')
data = []
print(len(cards))
for card in cards:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.FLpo-big-name')))
    nom = card.find_element(By.CSS_SELECTOR, 'a.FLpo-big-name').get_attribute('innerText')
    localisation = card.find_element(By.CSS_SELECTOR, 'div.FLpo-location-name').get_attribute('innerText')
    prix = card.find_element(By.CSS_SELECTOR, 'div.zV27-price').get_attribute('innerText')
    note = card.find_element(By.CSS_SELECTOR, 'div.FLpo-score').get_attribute('innerText')
    photo = card.find_element(By.CSS_SELECTOR, 'img.e9fk-photo').get_attribute('src')
    data.append({'nom':nom,
                 'localisation':localisation,
                 'prix':prix,
                 'note': note,
                 'photo':photo})

# Save the data to a JSON file
with open('hotel_python.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

driver.quit()

