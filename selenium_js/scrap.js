const { Builder, By, Key, until } = require('selenium-webdriver');
const fs = require('fs');

async function initializeDriver() {
  let driver = await new Builder().forBrowser('firefox').build();
  return driver;
}

async function runScraping() {
  let driver = await initializeDriver();

  try {
    await driver.get('https://www.booking.com/searchresults.en-gb.html?ss=Senegal&ssne=Senegal&ssne_untouched=Senegal&label=gen173rf-1BCAEoggI46AdIM1gDaNABiAEBmAEJuAEZyAEM2AEB6AEBiAIBmAIiqAIDuALjzY-lBsACAdICJDA4ZDA2NTVlLTYzZTAtNGQyNi04ZjQyLTNkNDlmNWRkZmJhN9gCBeACAQ&sid=aac11da12268b9f6f8f3b86fc9a43d53&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=187&dest_type=country&checkin=2023-07-16&checkout=2023-07-23&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure');

    let hasNextPage = true;
    let pageNumber = 1;
    let tab = [];

    while (hasNextPage && pageNumber <= 5 ) {
      console.log('Page', pageNumber);

      // Attendre que les annonces se chargent
      await driver.wait(until.elementLocated(By.className('d20f4628d0')), 5000);

      // Récupérer tous les éléments d'annonce
      let adCards = await driver.findElements(By.className('d20f4628d0'));

      // Parcourir les annonces et extraire les informations souhaitées
      for (let adCard of adCards) {
        
        let nom = await adCard.findElement(By.className('fcab3ed991 a23c043802')).getText();
        let localisation = await adCard.findElement(By.className('f4bd0794db b4273d69aa')).getText();
        let prix = await adCard.findElement(By.className('fcab3ed991 fbd1d3018c e729ed5ab6')).getText();
        let note = await adCard.findElement(By.className('b5cd09854e d10a6220b4')).getText();
        let photo = await adCard.findElement(By.className('b8b0793b0e')).getAttribute('src');
        

        tab.push({ nom,localisation,prix,note,photo});
      }

      // Vérifier s'il y a une page suivante
      let nextPageButton = await driver.findElement(By.className('fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 f9d6150b8e'));
      hasNextPage = await nextPageButton.isEnabled();

      // Si une page suivante existe, cliquer dessus
      if (hasNextPage) {
        await driver.executeScript("arguments[0].click();", nextPageButton);

        // Attendre que la nouvelle page se charge
        await driver.wait(until.elementLocated(By.className('d20f4628d0')), 5000);
      }

      pageNumber++;
    }

    let jsonData = JSON.stringify(tab);

    fs.writeFile('info_hotels.json', jsonData, 'utf8', (err) => {
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