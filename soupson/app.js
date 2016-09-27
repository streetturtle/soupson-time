var request = require('request');
var cheerio = require('cheerio');
var AsciiTable = require('ascii-table');
var moment = require('moment');
var table = new AsciiTable();

var today = moment().day();
request("http://www.soupson.ca/?lang=en", function(error, response, body){
  $ = cheerio.load(body);
  // table.setTitle($('.entry-title').first().text());
  // $('.entry-content').first().find('p').each(function(){
  //   if ($(this).text())
  //     table.addRow(($(this).text().split(': ')));
  // });

  var dayMenu = $('.entry-content').first().find('p').eq(1).text();
  console.log(dayMenu);
});
