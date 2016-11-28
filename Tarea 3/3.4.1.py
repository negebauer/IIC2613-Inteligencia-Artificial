#!/usr/bin/env python
# -*- coding: utf-8 -*-
from log import Log
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, metrics
import itertools
from sklearn.model_selection import cross_val_predict

# Loading Word2Vec, this takes a while ...”
from gensim . models import Word2Vec
# Loading Stopwords model
from nltk.corpus import stopwords
# Loading Stemmer model
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()  # stemmer


model = Word2Vec.load_word2vec_format('./google_news.bin', binary=True)
st = stemmer.stem  # get the stemming function


log = Log('3.4.1')
relations = [
    {
        'positive': ['woman', 'king'],
        'negative': ['man']
    },
    {
        'positive': ['paris', 'italy'],
        'negative': ['france']
    },
    {  # Extra
        'positive': ['car', 'water'],
        'negative': ['wheels']
    }
]
for relation in relations:
    positive = relation['positive']
    negative = relation['negative']
    line = 'Comparing most similar to positives {} and negatives {}'.format(positive, negative)
    log.log(line)
    print(line)
    similarities = model.most_similar(positive=positive, negative=negative)
    for s in similarities:
        log.log(s)
    log.log('')

similars = [
    {
        'first': 'breakfast',
        'second': 'cereal'
    },
    {
        'first': 'class',
        'second': 'course'
    },
    {  # Extra
        'first': 'man',
        'second': 'men'
    }
]
for similar in similars:
    first = similar['first']
    second = similar['second']
    line = 'Comparing similarity of {} with {}'.format(first, second)
    log.log(line)
    print(line)
    similarity = model.similarity(first, second)
    log.log(similarity)
    log.log('')
