from getMatDescriptors import getMatDescriptors
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from log import Log


def run_l(inF, inL, outF, outL, c):
    linear = LinearSVC(C=c, penalty='l2', loss='squared_hinge',
                       dual=True, multi_class='ovr')
    linear.fit(inF, inL)
    linear_predicted = linear.predict(outF)
    matrix = confusion_matrix(outL, linear_predicted)
    accuracy = accuracy_score(outL, linear_predicted)
    precision = precision_score(
        outL, linear_predicted, average="macro")

    log = '''
    LinearSVC
    c: {} error penalty
    accuracy: {}
    precision: {}
    Matrix:

    {}
    '''.format(c, accuracy, precision, matrix)
    print('\t\tn: {} - s: {} - p: {}'.format(c, accuracy, precision))
    return c, accuracy, precision, log, matrix


def run(train, test, filename):
    log = Log(filename, 'c', train)
    descriptSize = 4096
    penalty = 0.5
    inFeatsTrain, inLabelsTrain = getMatDescriptors(train, descriptSize)
    outFeatsTest, outLabelsTest = getMatDescriptors(test, descriptSize)
    print('Running with')
    while penalty < 10.5:
        print('\tc: {}'.format(penalty))
        data = run_l(inFeatsTrain, inLabelsTrain,
                     outFeatsTest, outLabelsTest, penalty)
        log.add_data(data)
        log.log()

        penalty += 0.5
    print('Finished running')
    print(log.max_data())
