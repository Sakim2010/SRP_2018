# -*- coding: utf-8 -*-
import scrapy

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
class QuotesSpider(scrapy.Spider):
    name = 'cats_JAN'
    allowed_domains = ['dawn.com']
    start_urls = ['https://www.dawn.com/archive/2018-02-01']
    DOWNLOAD_DELAY = 2.0
    # rotate_user_agent = True
    # def __init__(self):
    #     with open('dates.txt') as f:
    #         self.start_urls  = [line.strip() for line in f.readlines()]
    def parse(self, response):
        # self.log('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
        urls = []
        i = 0
        links = response.css('div.col-11 a.story__link::attr(href)').extract()
        category = response.css('article.box.story span.badge.size-three a::attr(title)').extract()
        cats = response.css('article.box.story span.badge.size-three').extract()
	headings = response.css('article.box.story.border--bottom h2.story__title a::text').extract()
	excerpts = response.css('article.box.story.border--bottom div.story__excerpt::text').extract()
	excerpts_final = []
	for t in range(len(excerpts)):
		if t%2 == 0:
			excerpts_final.append(excerpts[t])
        j = 0
        num = []
        for c in cats:
            if 'Entertainment' in str(c):
                num.append(j)
                # self.log('AAAAAAAAAAAAAAAAAAAAA' + str(j))
            j += 1
                # self.log('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')

        # self.log('Links...')
        # self.log(str(len(links)))
        # self.log('cats...')
        # self.log(str(len(category)))
        # self.log('num....')
        # self.log(str(num))
        done = len(num)
	#j = 0
	x = 0
        for l in links:
            # self.log('i....')
            # self.log(str(i))
            # self.log('i==num')
            # self.log(str((i == num)))
            if i in num:
                if done != 0:
                    yield{
                        'link': l,
                        'category': 'Entertainment',
			'final_date': str(response.url).split('/')[-1:],
			'heading': headings[x],
			'excerpt': excerpts_final[x]
                    }
                    done = done - 1
                    i = i-1
            else:
                yield{
                    'link': l,
                    'category': category[i],
		    'final_date': str(response.url).split('/')[-1:],
		    'heading': headings[x],
		    'excerpt': excerpts_final[x]
                }
            i += 1
	    x += 1
	    #j += 1
        if int(response.url[-2:]) <= 8 :
            new_day = int(response.url[-2:]) + 1
            new_url = response.url[:-2] + '0' + str(new_day)
            yield scrapy.Request(url = new_url, callback = self.parse)
        elif int(response.url[-2:]) <= 30 :
           new_day = int(response.url[-2:]) + 1
           new_url = response.url[:-2] + str(new_day)
           yield scrapy.Request(url = new_url, callback = self.parse)

    def parse_details(self, response):
        # print 'hi'
        if response.status == 403:
            yield scrapy.Request(url = response.url, callback = self.parse_details)

        else:
            self.log(str(response.request.headers.get('Referer')) + 'hiooooooooo')
            if ('images.dawn' in response.url) or ('herald.dawn' in response.url) or ('aurora.dawn' in response.url):
                if response.css('span.timestamp--time.timeago::text').extract() == []:
                    dates = response.css('span.story__time::text').extract()
                else:
                    dates = response.css('span.timestamp--time.timeago::text').extract()
                for d in dates:
                    if d != ' ':
                        date_string = d
                        break
                # self.log('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
                yield {
                    'heading' : response.css('a.story__link::text').extract_first(),
                    'date' : date_string,
                    'text' : response.css('div.story__content p::text').extract(),
                    'link' : response.url
                }
            else:
                if response.css('span.story__time::text').extract() == []:
                    dates = response.css('span.timestamp--time.timeago::text').extract()
                else:
                    dates = response.css('span.story__time::text').extract()
                for d in dates:
                    if d != ' ':
                        date_string = d
                        break
                # self.log('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
                yield {
                    'heading' : response.css('a.story__link::text').extract_first(),
                    'date' : date_string,
                    'text' : response.css('div.story__content p::text').extract(),
                    'link' : response.url
                }
