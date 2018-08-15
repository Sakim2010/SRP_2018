#CHANGE RANGE PER DATE AND WEEK_NUM
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

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

text = df['text']

category = df['category']

dates = df['dates']

heads = df['heads']

cats = df.category.unique()

unique_dates = df.dates.unique()

text_words = np.load('text_words.npy')
text_words_nostops = np.load('text_words_nostops.npy')
data_lemmatized = np.load('data_lemmatized.npy')

id2word = corpora.Dictionary(data_lemmatized)

print('0.5')

corpus = np.load('corpus.npy')

range_per_date = {}#[[0,0] for i in range(len(unique_dates))]

for d in unique_dates:
	range_per_date[d] = [0,0]

print(1)

for d in unique_dates:
	found = 0
	for i in range(len(dates)):
		if d == dates[i] and found != 1:
			found = 1
			range_per_date[d][0] = i
		elif d != dates[i] and found != 0:
			range_per_date[d][1] = i-1
			found = 0
			break
range_per_date[unique_dates[len(unique_dates)-1]][1] = len(dates) - 1

print(2)

upper = range_per_date['2017-07-01'][0]

lower = range_per_date['2018-05-31'][1]

corpus = corpus[upper:lower]

print(3)

week_num = '_mid_2017_mid_2018'

for i in range(40):
	if i%2 == 0:
		if i != 0:
			print('Num of topics: ' + str(i))
			lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=i)
			lda_model.save(('LDA_' + str(i) + week_num))