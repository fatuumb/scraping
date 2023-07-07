const puppeteer = require('puppeteer');

async function scrapeData() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const url = 'https://booking.kayak.com/flights/DSS,nearby-PAR/2023-08-02/2023-08-09?sort=bestflight_a&page=1';
  await page.goto(url);
  await page.waitForSelector('#searchResultsList', { timeout: 40000 });

  const flights = await page.$$eval('#searchResultsList div.resultWrapper', (elements) => {
    return elements.map((element) => {
      const image = element.querySelector('.top img').src;
      const heureDepart = element.querySelector('.top span:nth-child(1)').textContent.trim();
      const heureArrivee = element.querySelector('div.time.return > div.top > span').textContent.trim();
      const dureeVol = element.querySelector('div.duration > div.top').textContent.trim();
      const compagnie = element.querySelector('div.carrier > div.bottom').textContent.trim();
      const aeroportDepart = element.querySelector('div.time.depart > div.bottom').textContent.trim();
      const escale = element.querySelector('.bottom.stops').textContent.trim();
      const aeroportArrivee = element.querySelector('div.time.return > div.bottom').textContent.trim();
      const prix = element.querySelector('span.price.option-text').textContent.trim();

      return {
        image,
        heureDepart,
        heureArrivee,
        dureeVol,
        compagnie,
        aeroportDepart,
        escale,
        aeroportArrivee,
        prix,
      };
    });
  });

  console.log(flights);

  await browser.close();
}

scrapeData();
