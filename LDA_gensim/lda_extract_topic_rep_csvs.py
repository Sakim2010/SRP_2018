#CHANGE TOPICS_NUMS_LIST, WEEK_NUM
no = 0
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
#import spacy

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt
# %matplotlib inline

from dateutil import parser

num_topics_list = [12,16,18]
week_num = '_week_28'

rel_range = np.load('rel_range.npy')

pd_data = pd.read_csv('data.csv')

heads = np.array(pd_data['heads'])

heads = heads[rel_range[0]:rel_range[1]]

for num_topics in num_topics_list:
	doc_topic_dist = np.load(('doc_topic_dist' + week_num + '_topic_num_' + str(num_topics) + '.npy'))
	
	topic_doc_dist = [[] for i in range(num_topics)]
	
	for i in range(len(doc_topic_dist)):
		topics = doc_topic_dist[i]
		for j in range(len(topics)):
			topic_doc_dist[j].append(i)
	
	dict_new = {'head': [], 'topic_rep': []}
	
	for i in range(len(topic_doc_dist)):
		print(('Topic_'+str(i)+'.csv'))
		dict_new = {'head': [], 'topic_rep': []}
		#print(i)
		for t in topic_doc_dist[i]:
			#print(int(t))
			dict_new['head'].append(heads[int(t)])
			dict_new['topic_rep'].append(doc_topic_dist[int(t)][i])
		pd_new = pd.DataFrame(data = dict_new)
		pd_new.to_csv(('Topic_'+str(i)+ week_num + '_' + str(num_topics) + '.csv'), sep = ',')