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

    DOWNLOAD_DELAY = 2.0 #delay in seconds before every new GET Request for a url

    def parse(self, response):
        urls = []
        i = 0
        links = response.css('div.col-11 a.story__link::attr(href)').extract() # extarct the links to all articles found on the archive page from their css element
        category = response.css('article.box.story span.badge.size-three a::attr(title)').extract() #extarct the categories for all articles found on the archive page from their css element
        cats = response.css('article.box.story span.badge.size-three').extract()
    	excerpts = response.css('article.box.story.border--bottom div.story__excerpt::text').extract() #extarct the excerpts of all articles found on the archive page from their css element
    	excerpts_final = []
    	
        for t in range(len(excerpts)):
    		if t%2 == 0:
    			excerpts_final.append(excerpts[t])
            
            #in the above section of the code, the category 'Entertainment' isn't extracted...this section finds and stores the indexes of all articles who's category is 'Entertainment' so it can be added manually
	j = 0
	num = []
	for c in cats:
		if 'Entertainment' in str(c):
			num.append(j)
			j += 1
	done = len(num)
	self.log(('done = ' + str(done) + '\n'))
    	x = 0
        for l in links:
		if i in num:
			if done != 0:
				yield{
		                'link': l,
		                'category': 'Entertainment',
		       		'final_date': str(response.url).split('/')[-1:],
		       		'excerpt': excerpts_final[x]
				}
				done = done - 1
				x = x-1
		else:
			yield{
			'link': l,
			'category': category[x],
			'final_date': str(response.url).split('/')[-1:],
	                'excerpt': excerpts_final[x]
			}
		i += 1
		x += 1
#this section of the code simply updates the url based on the first url to allow data to be collected from an entire month
	if int(response.url[-2:]) <= 8 :
		new_day = int(response.url[-2:]) + 1
		new_url = response.url[:-2] + '0' + str(new_day)
		yield scrapy.Request(url = new_url, callback = self.parse)
	elif int(response.url[-2:]) <= max_days :
		new_day = int(response.url[-2:]) + 1
		new_url = response.url[:-2] + str(new_day)
		yield scrapy.Request(url = new_url, callback = self.parse)
