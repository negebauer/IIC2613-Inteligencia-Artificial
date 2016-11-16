from getMatDescriptors import getMatDescriptors
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from log import Log


def run_n_bin(inF, inL, outF, outL, n):
    inL_bin = map(lambda x: int(bin(x)[2:]), inL)
    outL_bin = map(lambda x: int(bin(x)[2:]), outL)

    neural_network = MLPClassifier(hidden_layer_sizes=n,
                                   solver='sgd')
    neural_network.fit(inF, inL_bin)
    neural_network_predicted = neural_network.predict(outF)
    matrix = confusion_matrix(outL_bin, neural_network_predicted)
    accuracy = accuracy_score(outL_bin, neural_network_predicted)
    precision = precision_score(
        outL_bin, neural_network_predicted, average="macro")

    log = '''
    MLPClassifier binary
    n: {} hidden neurons
    accuracy: {}
    Matrix:

    {}
    '''.format(n, accuracy, matrix)
    print('\t\tn: {} - s: {} - p: {}'.format(n, accuracy, precision))
    return n, accuracy, precision, log, matrix


def run_n(inF, inL, outF, outL, n):
    neural_network = MLPClassifier(hidden_layer_sizes=n,
                                   solver='sgd')  # , max_iter=1000
    neural_network.fit(inF, inL)
    neural_network_predicted = neural_network.predict(outF)
    matrix = confusion_matrix(outL, neural_network_predicted)
    accuracy = accuracy_score(outL, neural_network_predicted)
    precision = precision_score(
        outL, neural_network_predicted, average="macro")

    log = '''
    MLPClassifier
    n: {} hidden neurons
    accuracy: {}
    precision: {}
    Matrix:

    {}
    '''.format(n, accuracy, precision, matrix)
    print('\t\tn: {} - s: {} - p: {}'.format(n, accuracy, precision))
    return n, accuracy, precision, log, matrix


def run(train, test, filename):
    log = Log(filename, 'n', train)
    log_bin = Log(filename.split('.log')[0] + '_bin.log', 'n', train)
    descriptSize = 4096
    hidden_layer_sizes = 4096 / 4
    inFeatsTrain, inLabelsTrain = getMatDescriptors(train, descriptSize)
    outFeatsTest, outLabelsTest = getMatDescriptors(test, descriptSize)
    print('Running with')
    limit = 9 * descriptSize + 1
    while hidden_layer_sizes < limit:
        print('\tn: {}'.format(hidden_layer_sizes))
        data = run_n(inFeatsTrain, inLabelsTrain,
                     outFeatsTest, outLabelsTest, hidden_layer_sizes)
        log.add_data(data)
        log.log()

        data_bin = run_n_bin(inFeatsTrain, inLabelsTrain,
                             outFeatsTest, outLabelsTest,
                             hidden_layer_sizes)
        log_bin.add_data(data_bin)
        log_bin.log()

        hidden_layer_sizes += descriptSize / 4
        # hidden_layer_sizes += 50
    print('Finished running')
    print(log.max_data())
