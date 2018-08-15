# # # -*- coding: utf-8 -*-
# # import scrapy

# # date_this = '2018-03-01'
# # class QuotesSpider(scrapy.Spider):
# #     name = 'quotes'
# #     allowed_domains = ['dawn.com']
# #     start_urls = ['https://www.dawn.com/archive/2018-03-01']
# #     DOWNLOAD_DELAY = 2.0
# #     rotate_user_agent = True

# #     def parse(self, response):
# #         urls = []
# #         i = 0
# #         for sel in response.css('div.col-11 a.story__link::attr(href)'):
# #             # i+=1
# #             # if i > 10:
# #             #     break
# #             # url = sel.xpath('@href').extract_first()
# #             url_current = sel.extract()
# #             # item = {
# #             #   'link': url
# #             # }
# #             yield scrapy.Request(url = url_current, callback = self.parse_details)
        
# #         #     urls.append(url_current)
# #         # for url in urls:
# #         #     # print(url)
# #         #     yield scrapy.Request(url = url, callback = self.parse_details)
# #         if int(response.url[-2:]) <= 10 :
# #             new_day = int(response.url[-2:]) + 1
# #             new_url = response.url[:-2] + '0' + str(new_day)
# #             yield scrapy.Request(url = new_url, callback = self.parse)

# #         # file.close()
            
# #         # file.close()
# #         # if int(response.url[-2:]) <= 30 :
# #         #     new_day = int(response.url[-2:]) + 1
# #         #     new_url = response.url[:-2] + str(new_day)
# #         #     yield scrapy.Request(url = new_url, callback = self.parse)
# #         # for quote in response.css('div.quote'):
# #         #   item = {
# #         #       'author_name': quote.css('small.author::text').extract_first(),
# #         #       'text': quote.css('span.text::text').extract_first(),
# #         #       'tags': quote.css('a.tag::text').extract(),
# #         #   }
# #         #   yield item
# #         # yield {
# #         #   'author_name': response.css('small.author_name::text').extract_first(),
# #         #   'text': response.css('span.text::text').extract_first(),
# #         #   'tags': response.css('a.tag::text').extract(),
# #         # }

# #     def parse_details(self, response):
        
# #         yield {
# #             'heading' : response.css('a.story__link::text').extract_first(),
# #             # 'date' : date_this,
# #             'text' : response.css('div.col-12 div.story__content.pt-1.mt-1 p::text').extract(),
# #             'link' : response.url
# #         }


# # -*- coding: utf-8 -*-
# import scrapy

# date_this = '2018-03-01'
# class QuotesSpider(scrapy.Spider):
#     name = 'news_may'
#     allowed_domains = ['dawn.com']
#     start_urls = ['https://www.dawn.com/archive/2018-05-01']
#     DOWNLOAD_DELAY = 2.0
#     rotate_user_agent = True

#     def parse(self, response):
#         urls = []
#         i = 0
#         for sel in response.css('div.col-11 a.story__link::attr(href)'):
#             # i+=1
#             # if i > 10:
#             #     break
#             # url = sel.xpath('@href').extract_first()
#             url_current = sel.extract()
#             # yield {
#             #   'link': url_current
#             # }
#             yield scrapy.Request(url = url_current, callback = self.parse_details)
        
#         #     urls.append(url_current)
#         # for url in urls:
#         #     # print(url)
#         #     yield scrapy.Request(url = url, callback = self.parse_details)
#         if int(response.url[-2:]) <= 8 :
#             new_day = int(response.url[-2:]) + 1
#             new_url = response.url[:-2] + '0' + str(new_day)
#             yield scrapy.Request(url = new_url, callback = self.parse)
#         if int(response.url[-2:]) <= 30 :
#            new_day = int(response.url[-2:]) + 1
#            new_url = response.url[:-2] + str(new_day)
#            yield scrapy.Request(url = new_url, callback = self.parse)


#         # file.close()
            
#         # file.close()
#         # if int(response.url[-2:]) <= 30 :
#         #     new_day = int(response.url[-2:]) + 1
#         #     new_url = response.url[:-2] + str(new_day)
#         #     yield scrapy.Request(url = new_url, callback = self.parse)
#         # for quote in response.css('div.quote'):
#         #   item = {
#         #       'author_name': quote.css('small.author::text').extract_first(),
#         #       'text': quote.css('span.text::text').extract_first(),
#         #       'tags': quote.css('a.tag::text').extract(),
#         #   }
#         #   yield item
#         # yield {
#         #   'author_name': response.css('small.author_name::text').extract_first(),
#         #   'text': response.css('span.text::text').extract_first(),
#         #   'tags': response.css('a.tag::text').extract(),
#         # }

#     # def parse_details(self, response):

#     #     if response.css('div.col-12 div.story__content.pt-1.mt-1 p::text').extract() == []:
#     #         print('1')
#     #         print(response.url)
#     #         if 'images.dawn.com' in response.url:
#     #             print('2')
#     #             yield {
#     #                 'heading' : response.css('a.story__link::text').extract_first(),
#     #                 # 'date' : date_this,
#     #                 'text' : response.css('div.col-sm-11.col-12 div.story__content.pt-4.mt-4 p::text').extract(),
#     #                 'link' : response.url
#     #             }
#     #         else:
#     #             print('3')
#     #             yield {
#     #                 'heading' : response.css('a.story__link::text').extract_first(),
#     #                 # 'date' : date_this,
#     #                 'text' : repsonse.css('div.story__content.size-six p::text').extract(),
#     #                 'link' : response.url
#     #             }
#     #     else:
#     #         yield {
#     #             'heading' : response.css('a.story__link::text').extract_first(),
#     #             # 'date' : date_this,
#     #             'text' : response.css('div.col-12 div.story__content.pt-1.mt-1 p::text').extract(),
#     #             'link' : response.url
#     #         }
#     def parse_details(self, response):

#         if '40' in response.status:
#             yield scrapy.Request(url = response.url, callback = self.parse_details)
#         else:
#             if 'images.dawn.com' in response.url:
#                 yield {
#                     'heading' : response.css('a.story__link::text').extract_first(),
#                     'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
#                     'text' : response.css('div.story__content p::text').extract(),
#                     'link' : response.url
#                 }
#             elif 'herald.dawn.com' in response.url:
#                 yield {
#                     'heading' : response.css('a.story__link::text').extract_first(),
#                     'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
#                     'text' : response.css('div.story__content p::text').extract(),
#                     'link' : response.url
#                 }
#             elif 'aurora.dawn.com' in response.url:
#                 yield {
#                     'heading' : response.css('a.story__link::text').extract_first(),
#                     'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
#                     'text' : response.css('div.story__content p::text').extract(),
#                     'link' : response.url
#                 }
#             else:
#                 yield {
#                     'heading' : response.css('a.story__link::text').extract_first(),
#                     'date' : response.css('span.story__time::text').extract_first(),
#                     'text' : response.css('div.story__content p::text').extract(),
#                     'link' : response.url
#                 }


# -*- coding: utf-8 -*-
import scrapy

year_this = '2018'
class QuotesSpider(scrapy.Spider):
    name = 'news_JAN'
    allowed_domains = ['dawn.com']
    start_urls = ['https://www.dawn.com/archive/2018-01-01']
    DOWNLOAD_DELAY = 3.0
    # rotate_user_agent = True

    def parse(self, response):
        urls = []
        i = 0
        for sel in response.css('div.col-11 a.story__link::attr(href)'):
            url_current = sel.extract()
            yield scrapy.Request(url = url_current, callback = self.parse_details)
        
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
            # self.log('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
            new_format = 0
            if ('images.dawn' in response.url) or ('herald.dawn' in response.url) or ('aurora.dawn' in response.url):
                if response.css('span.timestamp--time.timeago::text').extract() == []:
                    dates = response.css('span.story__time::text').extract()
                else:
                    dates = response.css('span.timestamp--time.timeago::text').extract()
                    if len(response.css('span.timestamp--time.timeago::text').extract()) == 1 and response.css('span.timestamp--time.timeago::text').extract()[0] == ' ':
                        dates = response.css('span.story__time::text').extract()
                        if len(dates) == 1 and dates[0] == ' ':
                            dates = response.css('span.timestamp--time.timeago::attr(title)').extract()
                            new_format = 1
                done = 0
                for d in dates:
                    if d != ' ':
                        if year_this in d:
                            date_string = d
                            if new_format == 1:
                                date_string = date_string.split('T')[0]
                                done = 1
                                break
                            if date_string[0] == ' ':
                                date_string = date_string[1:]
                            if year_this not in date_string.split(' ')[-1:]:
                                splitted = date_string.split(' ')
                                leng = len(splitted)
                                date_string = ''
                                for s in splitted:
                                    leng -= 1
                                    if leng > 1:
                                        date_string += s + ' '
                                    elif leng > 0:
                                        date_string += s
                            done = 1
                            break
                if done == 0:
                    date_string = 'None'
                # self.log('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
                yield {
                    'heading' : response.css('a.story__link::text').extract_first(),
                    'date' : date_string,
                    'text' : response.css('div.story__content p::text').extract(),
                    'link' : response.url,
                    'date_actual': (str(response.request.headers.get('Referer')).split('/'))[-1:]
                }
            else:
                if response.css('span.story__time::text').extract() == []:
                    dates = response.css('span.timestamp--time.timeago::text').extract()
                    if len(response.css('span.timestamp--time.timeago::text').extract()) == 1 and response.css('span.timestamp--time.timeago::text').extract()[0] == ' ':
                        dates = response.css('span.story__time::text').extract()
                        if len(dates) == 1 and dates[0] == ' ':
                            dates = response.css('span.timestamp--time.timeago::attr(title)').extract()
                            new_format = 1
                else:
                    dates = response.css('span.story__time::text').extract()
                    if len(dates) == 1 and dates[0] == ' ':
                            dates = response.css('span.timestamp--time.timeago::attr(title)').extract()
                            new_format = 1
                done = 0
                for d in dates:
                    # if 'another-day-at-work-for-pakistani-workers-as-world-commemorates-labour-day' in response.url:
                    #     # self.log(d + '   DATTTETESSSESSSSSSSSSSSSSSSSSSSSSSSS')
                    if d != ' ':
                        if year_this in d:
                            date_string = d
                            if new_format == 1:
                                date_string = date_string.split('T')[0]
                                done = 1
                                break
                            if date_string[0] == ' ':
                                date_string = date_string[1:]
                            if year_this not in date_string.split(' ')[-1:]:
                                splitted = date_string.split(' ')
                                leng = len(splitted)
                                date_string = ''
                                for s in splitted:
                                    leng -= 1
                                    if leng > 1:
                                        date_string += s + ' '
                                    elif leng > 0:
                                        date_string += s
                            done = 1
                            break
                if done == 0:
                    date_string = 'None'
                # self.log('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
                yield {
                    'heading' : response.css('a.story__link::text').extract_first(),
                    'date' : date_string,
                    'text' : response.css('div.story__content p::text').extract(),
                    'link' : response.url,
                    'date_actual': (str(response.request.headers.get('Referer')).split('/'))[-1:]
                }

        # if 'images.dawn.com' in response.url:
        #     yield {
        #        'heading' : response.css('a.story__link::text').extract_first(),
        #        'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
        #        'text' : response.css('div.story__content p::text').extract(),
        #        'link' : response.url
        #     }
        # elif 'herald.dawn.com' in response.url:
        #        yield {
        #         'heading' : response.css('a.story__link::text').extract_first(),
        #         'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
        #         'text' : response.css('div.story__content p::text').extract(),
        #         'link' : response.url
        #     }
        # elif 'aurora.dawn.com' in response.url:
        #    yield {
        #         'heading' : response.css('a.story__link::text').extract_first(),
        #         'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
        #         'text' : response.css('div.story__content p::text').extract(),
        #         'link' : response.url
        #     }
        # else:
        #     yield {
        #         'heading' : response.css('a.story__link::text').extract_first(),
        #         'date' : response.css('span.story__time::text').extract_first(),
        #         'text' : response.css('div.story__content p::text').extract(),
        #         'link' : response.url
        #     }
