import numpy as np
import pandas as pd
import guidedlda
from nltk.corpus import stopwords
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import textmining

stop_words = stopwords.words('english')
stop_words.extend(['from', 'use', 'us', 'take', 'make', 'say', 'said', "say's", 'also', 'many', 'like'])
stopWords = set(stop_words)
df = pd.read_csv('data.csv')
text = df['text']
heads = df['heads']
dates = df['dates']

heads_new = []
dates_new = []

type_str = type(text[0])

import string
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
whitespace = ' \t\n\r\x0b\x0c'
alphas = []
for l in ascii_letters:
	alphas.append(l)

for d in digits:
		alphas.append(d)

for w in whitespace:
		alphas.append(w)

for t in text:
	num += 1
	if num%5000 == 0:
		print(num)
	if type(t) == type_str:
		#print((''.join(filter((lambda x: x in alphas), t))).split(' '))
		#sys.exit()
		texts_new.append((''.join(filter((lambda x: x in alphas), t))).split(' '))
		heads_new.append(heads[num-1])
		dates_new.append(dates[num-1])
	else:
		num_nonString = num

text = texts_new
dates = dates_new
heads = heads_new

def sent_to_words(sentences):
	for sentence in sentences:
		yield(gensim.utils.simple_preprocess(str(sentence), deacc= True))

text_words = list(sent_to_words(text))
new_text = []

for doc in text_words:
	new_doc = []
	for w in doc:
		if w not in stopWords:
			new_doc.append(w)
	new_text.append(' '.join(new_doc))

tdm = textmining.TermDocumentMatrix()
final_X = []
final_temp = []

for i in range(len(new_text)):
	tdm.add_doc(new_text[i])

temp = list(tdm.rows(cutoff=1))
vocab = tuple(temp[0])
X = np.array(temp[1:], dtype = np.int16)
word2id = dict((v, idx) for idx, v in enumerate(vocab))

n_top_words = 10
topic_word = model.topic_word_
for i, topic_dist in enumerate(topic_word):
	topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
	print('Topic {}: {}'.format(i, ' '.join(topic_words)))

model = guidedlda.GuidedLDA(n_topics=20, n_iter=100, random_state=7, refresh=20)

seed_topic_list = [['rape', 'raped', 'rapes', 'gangrape', 'gangraped', 'harassment', 'harasser', 'harasses', 'harassing', 'harassed', 'harass', 'harassers', 'harrassed', 'harrassment', 'sexual']]

seed_topics = {}
for t_id, st in enumerate(seed_topic_list):
	for word in st:
		seed_topics[word2id[word]] = t_id

model.fit(X, seed_topics=seed_topics, seed_confidence=0.4)

doc_topic = model.transform(X)

for t in range(20):
	rel_heads = []
	indices = []
	rel_texts = []
	rel_dates = []
	reps = []
	for i in range(len(doc_topic)):
		topic = doc_topic[i].argmax()
		if topic == t:
			rel_heads.append(heads[i])
			rel_dates.append(dates[i])
			rel_texts.append(text[i])
			indices.append(i)
			reps.append(max(doc_topic[i]))

	dict_topic_0 = {'doc_num': indices, 'rep': reps, 'head': rel_heads, 'texts': rel_texts, 'dates': rel_dates}

	pd_new = pd.DataFrame(data = dict_topic_0)
	pd_new.to_csv(('Topic_' + str(t) + '.csv'), sep = ',')