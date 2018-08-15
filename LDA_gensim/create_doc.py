import time
import sys
#mallet_path = '/home/sakim/Downloads/mallet-2.0.8/bin/mallet' # update this path 
import numpy as np
import pandas as pd

from pprint import pprint 
pd.options.mode.chained_assignment = None 

from dateutil import parser

df = pd.read_csv('ALL_complete.csv')

text = df['text']

category = df['category']

dates = df['final_date']

heads = df['heading']

cats = df.category.unique()

cats_doc_no = {}

count = 0
for c in cats:
	#print(c)
	count = 0
	for cat in category:
		if cat == c:
			count += 1
	cats_doc_no[c] = count

#sys.exit()

removal_indices = []

date_vals = [0 for j in range(len(dates))]
for i in range(len(dates)):
	d = parser.parse(dates[i])
	dates[i] = d.strftime("%Y-%m-%d")
	date_vals[i] = int(d.strftime("%Y%m%d"))


new_df_dict = {'heads': heads, 'dates': dates, 'category': category, 'text': text, 'date_vals': date_vals}

new_df = pd.DataFrame(data = new_df_dict)

new_df = new_df.sort_values(by='date_vals')

new_df = new_df.drop_duplicates(['text'])

new_df = new_df.drop_duplicates(['heads'])

new_df = new_df[new_df.category != 'Entertainment']

new_df = new_df[new_df.category != 'Sport']

new_df = new_df[new_df.category != 'Business']

new_df = new_df[new_df.category != 'Tech']

new_df = new_df[new_df.category != 'Multimedia']

new_df.to_csv('data.csv', index = False, index_label = False)
