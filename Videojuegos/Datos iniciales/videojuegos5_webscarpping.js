const cheerio = require("cheerio");
const axios = require("axios");
const j2cp = require("json2csv").Parser;
const fs = require("fs");

let baseUrl = "https://www.metacritic.com/browse/game/?releaseYearMin=1958&releaseYearMax=2024&page=";

let games = [];
let num_pags = 2;

async function getGames(url) {
  try {
    const response = await axios.get(url); 
    const $ = cheerio.load(response.data);
    const game = $(".c-finderProductCard_info");

    game.each(function () {
      const spans = $(this).find(".c-finderProductCard_titleHeading span");
      const id = $(spans[0]).text();
      const title = $(spans[1]).text();
      const date = $(this).find(".u-text-uppercase").text().trim(); 
      const description = $(this).find(".c-finderProductCard_description span").text();
      const metascore = $(this).find(".c-siteReviewScore span").text();

      games.push({ id, title, date, description, metascore });
    });

    if (num_pags < 549) {
      const next_page = baseUrl + num_pags;
      getGames(next_page);
      num_pags += 1;
      
      console.log(next_page);
    } else {
      const parser = new j2cp();
      const csv = parser.parse(games);

      fs.writeFileSync("./equisde.csv", csv, "utf-8");
    }
  } catch (error) {
    console.error(error);
  }
}

getGames("https://www.metacritic.com/browse/game/?releaseYearMin=1958&releaseYearMax=2024&page=1");
