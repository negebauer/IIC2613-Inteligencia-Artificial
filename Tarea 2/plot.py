import itertools
import numpy as np
from config_matplotlib import nothing
from matplotlib import pyplot as plt


nothing()


def plot_confusion_matrix(cm, classes, imagename,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):

    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.figure(figsize=(25, 25))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        for i in range(len(cm)):
            for j in range(len(cm[i])):
                n = cm[i][j]
                cm[i][j] = float(int(n*100))/100
    #     print("Normalized confusion matrix")
    # else:
    #     print('Confusion matrix, without normalization')
    #
    # print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

    open(imagename, 'w').close()
    plt.savefig(imagename)
    plt.close()
