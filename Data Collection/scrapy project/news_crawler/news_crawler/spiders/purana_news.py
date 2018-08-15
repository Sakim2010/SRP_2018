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
# import scrapy

# date_this = '2018-03-01'
# class QuotesSpider(scrapy.Spider):
#     name = 'news_MAY_purana'
#     allowed_domains = ['dawn.com']
#     start_urls = ['https://www.dawn.com/archive/2018-05-01']
#     DOWNLOAD_DELAY = 2.0
#     rotate_user_agent = True

#     def parse(self, response):
#         urls = []
#         i = 0
#         for sel in response.css('div.col-11 a.story__link::attr(href)'):
#             url_current = sel.extract()
#             yield scrapy.Request(url = url_current, callback = self.parse_details)
        
#         if int(response.url[-2:]) <= 8 :
#             new_day = int(response.url[-2:]) + 1
#             new_url = response.url[:-2] + '0' + str(new_day)
#             yield scrapy.Request(url = new_url, callback = self.parse)
#         if int(response.url[-2:]) <= 30 :
#            new_day = int(response.url[-2:]) + 1
#            new_url = response.url[:-2] + str(new_day)
#            yield scrapy.Request(url = new_url, callback = self.parse)

#     def parse_details(self, response):

#         if '40' in str(response.status):
#             yield scrapy.Request(url = response.url, callback = self.parse_details)

#         else:
#             if 'images.dawn.com' in response.url:
#                 yield {
#                    'heading' : response.css('a.story__link::text').extract_first(),
#                    # 'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
#                    'date': response.css('span.timestamp--time.timeago::attr(title)').extract_first(),
#                    'text' : response.css('div.story__content p::text').extract(),
#                    'link' : response.url
#                 }
#             elif 'herald.dawn.com' in response.url:
#                 final_date = ''
#                 smallest_month = 0
#                 smallest_day = 0
#                 dates_1 = response.css('span.timestamp--time.timeago::attr(title)').extract()
#                 dates_2 = response.css('span.timestamp--time.timeago::text').extract()
#                 for d in dates_1:
#                     if d != '':
#                         smallest_month = int(d.split('-')[3][:2])
#                         smallest_day = int(d.split('-')[3][:2])
#                         break
#                 for d in dates_1:
#                     parts = d.split('-')
#                     if int(p[2][:2]) < smallest_day[]:




#                 yield {
#                     'heading' : response.css('a.story__link::text').extract_first(),
#                     # 'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
#                     'date': ,
#                     'text' : response.css('div.story__content p::text').extract(),
#                     'link' : response.url
#                 }
#             elif 'aurora.dawn.com' in response.url:
#                yield {
#                     'heading' : response.css('a.story__link::text').extract_first(),
#                     # 'date' : response.css('span.timestamp--time.timeago::text')[1].extract(),
#                     'date': response.css('span.timestamp--time.timeago::attr(title)').extract_first(),
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
