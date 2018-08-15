import time
import sys
#mallet_path = '/home/sakim/Downloads/mallet-2.0.8/bin/mallet' # update this path
import numpy as np
import pandas as pd
from pprint import pprint
pd.options.mode.chained_assignment = None
# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# spacy for lemmatization
import spacy

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt
import requests
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
new_months = ['AUG', 'SEP', 'OCT', 'NOV', 'DEC']

merged = {'link': [], 'text': [], 'category': [], 'final_date': [], 'excerpt': [], 'heading': []}

#almost = pd.read_csv('ALL.csv')
#merged['link'].append(almost['link'][:13461])
#merged['text'].append(almost['text'][:13461])
#merged['category'].append(almost['category'][:13461])
#merged['final_date'].append(almost['final_date'][:13461])
#merged['excerpt'].append(almost['excerpt'][:13461])
#merged['heading'].append(almost['heading'][:13461])

for m in months:
	news_file = 'news_' + m + '.csv'
	cats_file = m + '_cats.csv'
	print(m)
	df_news = pd.read_csv(news_file)
	df_cats = pd.read_csv(cats_file)
	link_cats = df_cats['link']
	link_news = df_news['link']
	i_cats = 0
	i_news = 0
	missed_links = []
	found = 0
	#print(len(link_news))

	for l_c in link_cats:
		#r = requests.get(str(l_c))
		#l_to_split = r.url
		l_split = str(l_c).split('/')
		l_head = l_split[len(l_split)-1]
		i_news = 0
		found = 0
		if i_cats%100 == 0:
			print(i_cats/len(link_cats))
		for l_n in link_news:
			#print(i_news)
			if l_head in str(l_n):
				found = 1
				merged['link'].append(str(l_n))
				merged['text'].append(df_news['text'][i_news])
				merged['category'].append(df_cats['category'][i_cats])
				merged['final_date'].append(df_cats['final_date'][i_cats])
				merged['excerpt'].append(df_cats['excerpt'][i_cats])
				merged['heading'].append(df_news['heading'][i_news])
				#del link_news[i_news]
				break
			i_news += 1
		if found == 0:
			#print('im in...')
			i_news -= 1
			r = requests.get(str(l_c))
			l_to_split = r.url
			l_split = str(l_to_split).split('/')
			l_head = l_split[len(l_split)-1]
			i_news = 0
			found = 0
			#if i_cats%100 == 0:
			#	print(i_cats/len(link_cats))
			for l_n in link_news:
				#print(i_news)
				if l_head in str(l_n):
					#print('done' + str(l_n))
					found = 1
					merged['link'].append(str(l_n))
					merged['text'].append(df_news['text'][i_news])
					merged['category'].append(df_cats['category'][i_cats])
					merged['final_date'].append(df_cats['final_date'][i_cats])
					merged['excerpt'].append(df_cats['excerpt'][i_cats])
					merged['heading'].append(df_news['heading'][i_news])
					#del link_news[i_news]
					break
				i_news += 1
		i_cats += 1
		
	print(len(df_news))
	print(len(df_cats))
	print(len(merged['link']))
	#merged_save = pd.DataFrame(data = merged)
	#merged_save.to_csv(('ALL_' + str(m) + '.csv'), sep = ',')

merged_save = pd.DataFrame(data = merged)
merged_save.to_csv('ALL_complete.csv', sep = ',')
#print(len(missed_links))
#for i in range(int(len(missed_links)/10)):
#	print(missed_links[i])
