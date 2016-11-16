from getClassNames import getClassNames
from plot import plot_confusion_matrix
import cPickle as pickle
import shutil
import os


class Log:

    def __init__(self, filename, iter_name, classes_dir):
        self.values = []
        self.accuracys = []
        self.precisions = []
        self.logs = []
        self.matrixes = []
        self.filename = './logs/' + filename
        self.imagename = './logs/images/' + filename.split('.log')[0] + '.png'
        self.imagename_normalized = './logs/images/' + filename.split('.log')[0] + '_normalized.png'
        self.matrixes_dir = './logs/matrixes/' + filename.split('.')[0] + '/'
        self.iter_name = iter_name
        self.classes = getClassNames(classes_dir)

    def add_data(self, data):
        self.values.append(data[0])
        self.accuracys.append(data[1])
        self.precisions.append(data[2])
        self.logs.append(data[3])
        self.matrixes.append(data[4])

    def log(self):
        file = open(self.filename, 'w')
        accuracy_max = max(self.accuracys)
        accuracy_max_index = self.accuracys.index(accuracy_max)
        iter_max = self.values[accuracy_max_index]
        file.write('max:\n\t{}: {} - a: {}\n'.format(
            self.iter_name, iter_max, accuracy_max) + '\n')
        plot_confusion_matrix(self.matrixes[accuracy_max_index],
                              self.classes, self.imagename)
        plot_confusion_matrix(self.matrixes[accuracy_max_index],
                              self.classes, self.imagename_normalized, True)
        precision_max = max(self.precisions)
        iter_max = self.values[self.precisions.index(precision_max)]
        file.write('max:\n\t{}: {} - p: {}\n'.format(
            self.iter_name, iter_max, precision_max) + '\n')
        for i in range(len(self.accuracys)):
            file.write('{}: {} - a: {} - p: {}'.format(
                self.iter_name, self.values[i], self.accuracys[i],
                self.precisions[i]) + '\n')
        for line in self.logs:
            if '    [[' in line:
                line = line.replace('    [[', '[[')
            file.write(line + '\n')
        file.close()
        if os.path.exists(self.matrixes_dir):
            shutil.rmtree(self.matrixes_dir)
        os.makedirs(self.matrixes_dir)
        for i in range(len(self.matrixes)):
            file = open(self.matrixes_dir +
                        str(self.values[i]), 'w')
            pickle.dump(self.matrixes[i], file, -1)
            file.close()

    def max_data(self):
        file = open(self.filename, 'r')
        string = ''
        for i in range(0, 5):
            string += file.readline()
        return string
