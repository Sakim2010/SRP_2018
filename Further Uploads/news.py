# -*- coding: utf-8 -*- #converts utf-8 encoding to regular text to allow for ease in data processing
import scrapy

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_nums = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
num_days = ['30', '31']

year_this = '2018' #year of publication of the article(s) which need to be extracted
month_this = 'Feb' #3 letter form of month of publication of the article(s) which need to be extracted

month_no = ''
max_days = 0

for m in range(len(month_names)):
    if month_this == month_names[m]:
        month_no = month_nums[m]


if month_this == 'Feb':
	max_days = 28
else:
	max_days = num_days[(int(month_no)%2)]

class QuotesSpider(scrapy.Spider):
    name = 'news_' + month_this #name of the spider when uploaded to the cloud
    
    allowed_domains = ['dawn.com'] #allowed domains for all urls to be accessed by the spider
    
    first_url = 'https://www.dawn.com/archive/' + (year_this + '-' + month_no + '-01')

    start_urls = [first_url] #the first url to be accessed by the spider

    DOWNLOAD_DELAY = 3.0 #delay in seconds before every new GET Request for a url

    def parse(self, response):
        urls = []
        i = 0
        for sel in response.css('div.col-11 a.story__link::attr(href)'): #for each css element in the archive page containing the links to articles
            url_current = sel.extract() #extract the url
            yield scrapy.Request(url = url_current, callback = self.parse_details) #and pass it into the function parse_details

        #this section of the code simply updates the url based on the first url to allow data to be collected from an entire month
        if int(response.url[-2:]) <= 8 :
            new_day = int(response.url[-2:]) + 1
            new_url = response.url[:-2] + '0' + str(new_day)
            yield scrapy.Request(url = new_url, callback = self.parse)
        elif int(response.url[-2:]) <= 30 :
           new_day = int(response.url[-2:]) + 1
           new_url = response.url[:-2] + str(new_day)
           yield scrapy.Request(url = new_url, callback = self.parse)

    def parse_details(self, response):
        if response.status == 403: #incase there is an error, rerun the request
            yield scrapy.Request(url = response.url, callback = self.parse_details)
        else: #else, get extract the heading and text from the relevant css elements and store it alongside the link using the yield function
            yield {
               'heading' : response.css('a.story__link::text').extract_first(),
               'text' : response.css('div.story__content p::text').extract(),
               'link' : response.url,
            }
