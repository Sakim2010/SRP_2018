#CHANGE WEEK_NUM & LIMIT,STEP,ETC
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

week_num = '_week_28'

texts = np.load('data_lemmatized.npy')
print(1)
dictionary = corpora.Dictionary(texts)
print(2)
coherence_values = []
model_list = []
limit=40; start=2; step=2;
for num_topics in range(start, limit, step):
	print('num_topics: ' + str(num_topics))
	model = gensim.models.LdaModel.load('LDA_' + str(num_topics) + week_num)
	model_list.append(model)
	coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
	coherence_values.append(coherencemodel.get_coherence())

np.save(('coherence_values' + week_num), coherence_values)
np.save(('model_list' + week_num), model_list)


# Show graph

x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show() 