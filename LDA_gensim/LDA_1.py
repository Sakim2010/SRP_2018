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
 
from dateutil import parser 
 
# NLTK Stop words 
from nltk.corpus import stopwords 
stop_words = stopwords.words('english') 
stop_words.extend(['from', 'subject', 're', 'edu', 'use']) 

#new_df.to_csv('data.csv', index = False, index_label = False)

df = pd.read_csv('data.csv')

text = df['text']

category = df['category']

dates = df['dates']

heads = df['heads']

cats = df.category.unique()

all_dates = df.dates.unique()

removal_indices = []

for i in range(len(text)):
    #if i%100 == 0:
    #    print(i)
    if type(text[i]) is float:
        removal_indices.append(i)
        continue
    text[i] = text[i].replace("\'", "")
    text[i] = text[i].replace("\n", " ")

print('0.25')

for i in range(len(removal_indices)):
	removal_indices[i] -= i

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

text_words = list(sent_to_words(text))

#text_words = np.load('text_words.npy')

print('0.5')

np.save('text_words', text_words)

#print(text_words[:1])

bigram = gensim.models.Phrases(text_words, min_count=5, threshold=100)

print('0.75')

trigram = gensim.models.Phrases(bigram[text_words], threshold=100)

print('0.9')

# Faster way to get a sentence clubbed as a trigram/bigram
bigram_mod = gensim.models.phrases.Phraser(bigram)
trigram_mod = gensim.models.phrases.Phraser(trigram)

print(1)

# Define functions for stopwords, bigrams, trigrams and lemmatization
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]
# Define functions for stopwords, bigrams, trigrams and lemmatization 
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

def make_trigrams(texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
       doc = nlp(" ".join(sent))
       texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out

# Remove Stop Words
text_words_nostops = remove_stopwords(text_words)
np.save('text_words_nostops', text_words_nostops)

print(2)

# Form Bigrams
text_words_bigrams = make_bigrams(text_words_nostops)
#text_words_bigrams = np.load('text_words_bigrams.npy')
np.save('text_words_bigrams', text_words_bigrams)

print(3)
# Initialize spacy 'en' model, keeping only tagger component (for efficiency) 
#python3 -m spacy download en
nlp = spacy.load('en', disable=['parser', 'ner'])

print(4)

# Do lemmatization keeping only noun, adj, vb, adv
data_lemmatized = lemmatization(text_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
np.save('data_lemmatized', data_lemmatized)

#data_lemmatized = np.load('data_lemmatized.npy')
print(5)

# Create Dictionary
id2word = corpora.Dictionary(data_lemmatized)

print(6)

# Create Corpus
texts = data_lemmatized

print(7)

# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
print(8)
np.save('corpus', corpus)