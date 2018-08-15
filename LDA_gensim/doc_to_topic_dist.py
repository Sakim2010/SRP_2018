#CHANGE NUMS_TOPICS_LIST, WEEK_NUM, REL_RANGE
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
# %matplotlib inline

from dateutil import parser

# NLTK Stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

num_topics_list = [12,16,18]

week_num = '_week_28'

df = pd.read_csv('data.csv')

text = df['text']

category = df['category']

dates = df['dates']

heads = df['heads']

cats = df.category.unique()

all_dates = df.dates.unique()

unique_dates = df.dates.unique()

range_per_date = {}#[[0,0] for i in range(len(unique_dates))]
 
for d in unique_dates:
    range_per_date[d] = [0,0]
 
#np.save('range_per_date', range_per_date)
 
for d in unique_dates:
    found = 0
    for i in range(len(dates)):
        if d == dates[i] and found != 1:
            #print('d: ' + str(d))
            #print('dates[i]: ' + str(dates[i]))
            #print(d == dates[i])
            found = 1
            range_per_date[d][0] = i
            #print(dates[i])
        elif d != dates[i] and found != 0:
            range_per_date[d][1] = i-1
            #print()
            found = 0
            break
range_per_date[unique_dates[len(unique_dates)-1]][1] = len(dates) - 1

print('done range per date')

corpus = np.load('corpus.npy')

upper = range_per_date['2018-01-14'][0]

lower = range_per_date['2018-01-20'][1]

corpus = corpus[upper:lower]

rel_range = []
rel_range.append(upper)
rel_range.append(lower)

np.save('rel_range', rel_range)
#corpus = pickle.load(file('store_corpus.txt'))

for num_topics in num_topics_list:
	lda_model = gensim.models.LdaModel.load('LDA_' + str(num_topics) + str(week_num))
	
	#print('**************Topics**************')
	
	#for i in range(int(lda_model.num_topics)):
	#	print('Topic ' + str(i))
	#	print(lda_model.print_topic(i))
		
	
	doc_topic_dist = [[0 for j in range(num_topics)] for i in range(len(corpus))]
	
	topic_doc_dist = [[0 for j in range(len(corpus))] for i in range(num_topics)]
	
	cat_topic_dist = {}
	
	
	for c in cats:
		cat_topic_dist[c] = [[0,0] for j in range(num_topics)]
	
	topic_dist_dates = {}
	
	for d in all_dates:
		topic_dist_dates[str(d)] = [[0,0] for j in range(num_topics)]
	
	topic_totals = [0 for j in range(num_topics)]
	
	from statistics import mode
	from statistics import mean
	no_of_topics = []
	reps_1 = []
	
	
	for i in range(len(corpus) - 1): #change back to without -1!!!
		doc_lda = lda_model[corpus[i]]
		topics = doc_lda
		#print(i)
		no = 0
		for t in topics:
			#print(t)
			#print(t[0])
			#print(i)
			#print(category[i])
			#topic_totals[int(t[0])] += t[1]
			doc_topic_dist[i][int(t[0])] = t[1]
			no += 1
			#cat_topic_dist[category[i]][int(t[0])][0] += 1
			#cat_topic_dist[category[i]][int(t[0])][1] += t[1]
			#topic_dist_dates[dates[i]][int(t[0])][0] += 1
			#topic_dist_dates[dates[i]][int(t[0])][1] += t[1]
		#no_of_topics.append(no)	
		
	#print(mode(no_of_topics))
	#print(mean(no_of_topics))
	
	np.save(('doc_topic_dist' + week_num + '_topic_num_' + str(num_topics)), np.array(doc_topic_dist))