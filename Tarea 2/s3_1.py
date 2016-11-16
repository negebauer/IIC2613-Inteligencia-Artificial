from getMatDescriptors import getMatDescriptors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from log import Log


def run_k(inF, inL, outF, outL, k):
    neighbors = KNeighborsClassifier(n_neighbors=k, weights='distance',
                                     algorithm='auto', leaf_size=30, p=2,
                                     metric='minkowski', metric_params=None,
                                     n_jobs=1)
    neighbors.fit(inF, inL)
    neighbors_predict = neighbors.predict(outF)
    matrix = confusion_matrix(outL, neighbors_predict)
    accuracy = accuracy_score(outL, neighbors_predict)
    precision = precision_score(
        outL, neighbors_predict, average="macro")

    log = '''
    KNeighborsClassifier
    k: {} neighbors
    accuracy: {}
    precision: {}
    Matrix:

    {}
    '''.format(k, accuracy, precision, matrix)
    print('\t\tk: {} - s: {} - p: {}'.format(k, accuracy, precision))
    return k, accuracy, precision, log, matrix


def run(train, test, filename, k_i=1, k_f=101, inc=1):
    log = Log(filename, 'k', train)
    descriptSize = 4096
    inFeatsTrain, inLabelsTrain = getMatDescriptors(train, descriptSize)
    outFeatsTest, outLabelsTest = getMatDescriptors(test, descriptSize)
    k = k_i
    print('Running with')
    while k < k_f:
        print('\tk: {}'.format(k))
        data = run_k(inFeatsTrain, inLabelsTrain,
                     outFeatsTest, outLabelsTest, k)
        log.add_data(data)
        log.log()

        k += inc
    print('Finished running')
    print(log.max_data())
