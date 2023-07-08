import { Builder, By, Key, until } from 'selenium-webdriver';
import fs from  'fs';
import postgres from 'postgres';

// const { Builder, By, Key, until } = require('selenium-webdriver');
// const fs = require('fs');

async function initializeDriver() {
  let driver = await new Builder().forBrowser('firefox').build();
  return driver;
}

async function runScraping() {
  let driver = await initializeDriver();

  try {
    await driver.get('https://www.cruisedirect.com/destination/europe');

    let hasNextPage = true;
    let pageNumber = 1;
    let tab = [];

    while (hasNextPage && pageNumber <= 30) {
      console.log('Page', pageNumber);

      // Attendre que les annonces se chargent
      await driver.wait(until.elementLocated(By.className('result_section')), 5000);

      // Récupérer tous les éléments d'annonce
      let adCards = await driver.findElements(By.className('result_section'));

      // Parcourir les annonces et extraire les informations souhaitées
      for (let adCard of adCards) {
        
        let title = await adCard.findElement(By.className('fw-b')).getText();
        let dure = await adCard.findElement(By.className('col-blk pop ft-0')).getText();
        // let image = await adCard.findElement(By.xpath('//*[@id="listing_view_container"]/div[2]/div/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div/div/section/div/div[1]/div/div[1]/div/div[1]/a/div/img')).getAttribute('data-src');
        let port = await adCard.findElement(By.className('col-blk pop ft-0 ft-weight-light')).getText();
        let prix = await adCard.findElement(By.className('col-red ft-weight-bolder')).getText();

        tab.push({ title,dure, port,prix });
      }

      // Vérifier s'il y a une page suivante
      let nextPageButton = await driver.findElement(By.className('pager-next'));
      hasNextPage = await nextPageButton.isEnabled();

      // Si une page suivante existe, cliquer dessus
      if (hasNextPage) {
        await driver.executeScript("arguments[0].click();", nextPageButton);

        // Attendre que la nouvelle page se charge
        await driver.wait(until.elementLocated(By.className('result_section')), 5000);
      }

      pageNumber++;
    }

    let jsonData = JSON.stringify(tab);

    fs.writeFile('data.json', jsonData, 'utf8', (err) => {
      if (err) {
        console.error('Une erreur s\'est produite lors de l\'écriture du fichier JSON :', err);
        return;
      }
      console.log('Les données ont été enregistrées dans le fichier JSON avec succès.');
    });
  } finally {
    await driver.quit();
  }
}

runScraping();
