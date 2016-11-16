import pickle
from getClassNames import getClassNames
from plot import plot_confusion_matrix
import os
import shutil


def matrix(folder, name):
    file = open('./logs/matrixes/' + folder + '/' + name, 'r')
    matrix = pickle.load(file)
    file.close()
    return matrix


def image(matrix, filename=None, size='b'):
    classes_dir = 'TestSet 2' if size == 'b' else 'TestSet'
    plot_confusion_matrix(matrix, getClassNames(classes_dir), filename)


def image_matrix(folder, name):
    classes_dir = 'TestSet 2' if '_b' in folder or '_b_bin' in folder else 'TestSet'
    m = matrix(folder, name)
    image_folder = './logs/all_images/' + folder + '/'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    plot_confusion_matrix(m, getClassNames(classes_dir),
                          image_folder + folder + '.png')
    plot_confusion_matrix(m, getClassNames(classes_dir),
                          image_folder + folder + '_normalized.png', True)


def all_images():
    matrixes_images_folder = './logs/all_images/'
    matrixes_folder = './logs/matrixes/'
    if os.path.exists(matrixes_images_folder):
        shutil.rmtree(matrixes_images_folder)
    os.makedirs(matrixes_images_folder)
    for matrix_folder in os.listdir(matrixes_folder):
        if '.DS_Store' in matrix_folder:
            continue
        matrix_folder += '/'
        images_folder = matrixes_images_folder + matrix_folder
        os.makedirs(images_folder)
        classes_dir = 'TestSet 2' if '_b.' in matrix_folder or '_b_bin' in matrix_folder else 'TestSet'
        classes = getClassNames(classes_dir)
        for matrix_file in os.listdir(matrixes_folder + matrix_folder):
            imagename = matrixes_images_folder + matrix_folder + matrix_file + '.png'
            print('Going to generate matrix {}{}'.format(matrix_folder,
                                                         matrix_file))
            m = matrix(matrix_folder, matrix_file)
            plot_confusion_matrix(m, classes, imagename)
