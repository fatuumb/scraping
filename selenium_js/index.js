const axios = require('axios');
const fs = require('fs');
const options = {
  method: 'GET',
  url: 'https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete',
  params: {text: 'dakar'},
  headers: {
    'X-RapidAPI-Key': '3745475799msh6a037a92e03d981p104348jsn41afa590197c',
    'X-RapidAPI-Host': 'apidojo-booking-v1.p.rapidapi.com'
  }
};

async function fetchData() {


  try {
    const response = await axios.request(options);
    console.log(response.data);

    const data = response.data;
  const jsonData = JSON.stringify(data, null, 2);
    fs.writeFileSync('hotel_api.json', jsonData);

    console.log('Data saved to response_data.json');


  } catch (error) {
    console.error(error);
  }


}

fetchData();