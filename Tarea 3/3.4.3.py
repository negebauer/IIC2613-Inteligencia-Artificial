from log import Log
import matplotlib
matplotlib.use('Agg')
import os
import numpy as np
from sklearn import svm, metrics
import itertools
from sklearn.model_selection import cross_val_predict
import nltk
import itertools
import numpy as np
from matplotlib import pyplot as plt
from gensim . models import Word2Vec
# Loading Stopwords model
from nltk.corpus import stopwords
# Loading Stemmer model
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()  # stemmer

model = Word2Vec.load_word2vec_format('./google_news.bin', binary=True)
st = stemmer.stem  # get the stemming function

log = Log('3.4.3')
path_polarity = './review_polarity/txt_sentoken'
path_movie_train = './aclImdb/train'
path_movie_test = './aclImdb/test'
stop_words = set(stopwords.words('english'))
class_names = ['Negative', 'Positive']
vector = 300


def vector_of_file(file):
    # print(file)
    f = open(file, 'r')
    lines = f.read()
    words = lines.split(' ')
    total = np.zeros(vector)
    count = 0
    for word in words:
        if word not in stop_words and word in model.vocab.keys():
            total += np.array(model[word])
            count += 1
    f.close()
    if count == 0:
        return total
    return total / count


def vectors_from_dir(dir, label):
    vectors = []
    files = os.listdir(dir)
    for file in files:
        vectors.append(vector_of_file('{}/{}'.format(dir, file)))
    return vectors, [label] * len(files)


def get_data(filename):
    filename_positive = filename + '/pos'
    filename_negative = filename + '/neg'
    set_positive = vectors_from_dir(filename_positive, 1)
    set_negative = vectors_from_dir(filename_negative, 0)
    critics = set_positive[0] + set_negative[0]
    labels = set_positive[1] + set_negative[1]
    return critics, labels

print('Getting data polarity')
polarity_all = get_data(path_polarity)
polarity_critics, polarity_labels = polarity_all[0], polarity_all[1]

print('polarity_linear')
log.log('polarity_linear')
classifier = svm.SVC(C=1, kernel='linear')
prediction = cross_val_predict(classifier, polarity_critics, polarity_labels, cv=10)
accuracy = metrics.accuracy_score(polarity_labels, prediction)
precision = metrics.precision_score(polarity_labels, prediction, average="macro")
log.log('accuracy')
log.log(accuracy)
log.log('precision')
log.log(precision)
confusion_matrix = metrics.confusion_matrix(polarity_labels, prediction)
log.plot_confusion_matrix(confusion_matrix, class_names, 'polarity_linear.png', 'polarity_linear')

print('polarity_rbf')
log.log('polarity_rbf')
classifier = svm.SVC(C=1, kernel='rbf')
prediction = cross_val_predict(classifier, polarity_critics, polarity_labels, cv=10)
accuracy = metrics.accuracy_score(polarity_labels, prediction)
precision = metrics.precision_score(polarity_labels, prediction, average="macro")
log.log('accuracy')
log.log(accuracy)
log.log('precision')
log.log(precision)
confusion_matrix = metrics.confusion_matrix(polarity_labels, prediction)
log.plot_confusion_matrix(confusion_matrix, class_names, 'polarity_rbf.png', 'polarity_rbf')

print('Getting data movies')
movies_train_all = get_data(path_movie_test)
movies_train_critics, movies_train_labels = movies_train_all[0], movies_train_all[1]

movies_test_all = get_data(path_movie_train)
movies_test_critics, movies_test_labels = movies_test_all[0], movies_test_all[1]

print('movies_linear')
log.log('movies_linear')
classifier = svm.SVC(C=1, kernel='linear')
classifir.fit(movies_train_critics, movies_train_labels)
prediction = cross_val_predict(classifier, movies_test_critics, movies_test_labels, cv=10)
accuracy = metrics.accuracy_score(movies_test_labels, prediction)
precision = metrics.precision_score(movies_test_labels, prediction, average="macro")
log.log('accuracy')
log.log(accuracy)
log.log('precision')
log.log(precision)
confusion_matrix = metrics.confusion_matrix(movies_test_labels, prediction)
log.plot_confusion_matrix(confusion_matrix, class_names, 'movies_linear.png', 'movies_linear')

print('movies_rbf')
log.log('movies_rbf')
classifier = svm.SVC(C=1, kernel='rbf')
classifir.fit(movies_train_critics, movies_train_labels)
prediction = cross_val_predict(classifier, movies_test_critics, movies_test_labels, cv=10)
accuracy = metrics.accuracy_score(movies_test_labels, prediction)
precision = metrics.precision_score(movies_test_labels, prediction, average="macro")
log.log('accuracy')
log.log(accuracy)
log.log('precision')
log.log(precision)
confusion_matrix = metrics.confusion_matrix(movies_test_labels, prediction)
log.plot_confusion_matrix(confusion_matrix, class_names, 'movies_rbf.png', 'movies_rbf')
