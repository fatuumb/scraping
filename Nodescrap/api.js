// const axios = require('axios');

// async function fetchFlightData() {
//   try {
//     const response = await axios.get('https://app.apidog.com/project/345182');
//     const flightData = response.data;

//     // Récupérer les informations spécifiques de chaque vol
//     flightData.forEach(flight => {
//       const image = flight.image;
//       const departureDate = flight.departureDate;
//       const arrivalDate = flight.arrivalDate;
//       const layovers = flight.layovers;
//       const duration = flight.duration;
//       const departureAirport = flight.departureAirport;
//       const arrivalAirport = flight.arrivalAirport;
//       const price = flight.price;

//       // Faire ce que vous souhaitez avec les informations récupérées
//       console.log('Image:', image);
//       console.log('Date de départ:', departureDate);
//       console.log('Date d\'arrivée:', arrivalDate);
//       console.log('Escales:', layovers);
//       console.log('Durée du vol:', duration);
//       console.log('Aéroport de départ:', departureAirport);
//       console.log('Aéroport d\'arrivée:', arrivalAirport);
//       console.log('Prix:', price);
//       console.log('------------------------------');
//     });
//   } catch (error) {
//     console.error('Une erreur s\'est produite :', error);
//   }
// }

// fetchFlightData();

const axios = require('axios');
const fs = require('fs');
async function fetchData() {


const options = {
  method: 'GET',
  url: 'https://flight-radar1.p.rapidapi.com/aircrafts/list',
  headers: {
    'Content-Type': 'application/json',
    'X-RapidAPI-Key': '0ebb338956msh171c0b762c43089p1e77b1jsncccae7c8b5a6',
    'X-RapidAPI-Host': 'flight-radar1.p.rapidapi.com'
  }
};

try {
      const response = await axios.request(options);
      const data = response.data;

      fs.writeFile('data.json', JSON.stringify(data), (err) => {
         if (err) {
         console.error('Une erreur s\'est produite lors de l\'enregistrement des données:', err);
} else {
console.log(response.data);
}
});
} catch (error) {
	console.error(error);
}
}
fetchData();
