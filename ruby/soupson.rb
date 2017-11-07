require 'open-uri'
require 'nokogiri'

html = open('http://www.soupson.ca/?lang=en')

doc = Nokogiri::HTML(html)

week = doc.css('.entry-content').first.css('p').each do |day|
	puts day.xpath('text()')
end
