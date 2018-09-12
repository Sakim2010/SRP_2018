import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import requests

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] #3 letter form of months of publication of the article(s) for which has been extracted using both cats_spider and news spiders

merged = {'link': [], 'text': [], 'category': [], 'final_date': [], 'excerpt': [], 'heading': []} #final dictionary to be saved as a csv file for the final dataset

for m in months:
	news_file = 'news_' + m + '.csv' #file storing results for month 'm' from news.py
	cats_file = m + '_cats.csv' #file storing results for month 'm' from cats_spider.py
	
	print(m) #simply to show progress
	
	#get data from csv files
	df_news = pd.read_csv(news_file)
	df_cats = pd.read_csv(cats_file)
	
	#get links from both files
	link_cats = df_cats['link']
	link_news = df_news['link']
	
	i_cats = 0
	i_news = 0
	missed_links = []
	found = 0

	#for each link from the cats_spider.py results
	for l_c in link_cats:

		l_split = str(l_c).split('/')
		l_head = l_split[len(l_split)-1]
		i_news = 0
		found = 0

		#simply to show progress
		if i_cats%100 == 0:
			print(i_cats/len(link_cats))

		#find the same link in the news.py results, and when found, store it in the merged dictionary, along with the text and heading from the news.py results, as well as the excerpt, category and date from the cats_spider.py results
		for l_n in link_news:
			if l_head in str(l_n):
				found = 1
				merged['link'].append(str(l_n))
				merged['text'].append(df_news['text'][i_news])
				merged['category'].append(df_cats['category'][i_cats])
				merged['final_date'].append(df_cats['final_date'][i_cats])
				merged['excerpt'].append(df_cats['excerpt'][i_cats])
				merged['heading'].append(df_news['heading'][i_news])
				break
			i_news += 1
		
		#if that's not found though, that means the link on the archive page(found in the results from cats_spider.py) was redirected before going to the final article webpage
		if found == 0:
			i_news -= 1

			#get the redirected url
			r = requests.get(str(l_c))
			l_to_split = r.url
			
			#extract the part of the url that mentions the (possibly new) heading on the article's webpage, for example: 'ecp-takes-notice-of-alleged-misuse-of-public-funds-for-na-120-election' in 'https://www.dawn.com/news/1352995/ecp-takes-notice-of-alleged-misuse-of-public-funds-for-na-120-election'
			l_split = str(l_to_split).split('/')
			l_head = l_split[len(l_split)-1]
			
			i_news = 0
			found = 0
			
			#and try to find the same part in the links from the results from news.py. When found, store it in the merged dictionary, along with the text and heading from the news.py results, as well as the excerpt, category and date from the cats_spider.py results
			for l_n in link_news:
				if l_head in str(l_n):
					found = 1
					merged['link'].append(str(l_n))
					merged['text'].append(df_news['text'][i_news])
					merged['category'].append(df_cats['category'][i_cats])
					merged['final_date'].append(df_cats['final_date'][i_cats])
					merged['excerpt'].append(df_cats['excerpt'][i_cats])
					merged['heading'].append(df_news['heading'][i_news])
					break
				i_news += 1
		i_cats += 1

#convert dictionary to dataframe
merged_save = pd.DataFrame(data = merged)
#and then store the dataframe as a csv file
merged_save.to_csv('ALL_complete.csv', sep = ',')