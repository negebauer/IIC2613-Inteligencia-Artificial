#! /usr/bin/env python

import os
import numpy as np
import scipy.io as sio
from sys import exit
from argparse import ArgumentParser


def getMatDescriptors(inDir, descripSize):

    fileType = 'mat'
    nFiles = 0
    for root, dirs, files in os.walk(inDir):
        for file in files:
            if file.endswith(fileType):
                nFiles += 1

    # Get memory to store descriptors
    inFeats = np.empty([nFiles, descripSize], dtype=np.float32)
    inLabels = np.empty([nFiles], dtype=np.int32)

    for root, dirs, files in os.walk(inDir):
        fileCounter = 0
        for name, nClasses in zip(dirs, range(0, len(dirs))):
            print('Reading descriptors of class' + str(nClasses + 1) + ' of ' + str(len(dirs)))
            classDir = os.path.join(inDir, name)
            for root2, dirs2, files2 in os.walk(classDir):
                for name2, loopFilesCnt in zip(files2, range(0, len(files2))):
                    # print 'class' + str(nClasses+1) + ': file ' +
                    # str(loopFilesCnt+1) + ' of ' + str(len(files2))
                    if name2.endswith((fileType)):
                        descFile = os.path.join(root2, name2)
                        aux = sio.loadmat(descFile)
                        inFeats[fileCounter] = aux['stored']
                        inLabels[fileCounter] = nClasses + 1
                        fileCounter += 1
    return inFeats, inLabels


if __name__ == '__main__':

    parser = ArgumentParser(description='Read image descriptors')
    parser.add_argument('-d', '--directory', type=str,
                        help='Dataset directory')
    results = parser.parse_args()

    datadir = None
    if results.directory is None:
        print('missing directory')
        print('usage: ./getDescriptors.py -d <desc_path>')
        exit(-1)
    datadir = results.directory

    inFeats, inLabels = getMatDescriptors(datadir, 4096)
    print('inFeats')
    print(inFeats)
    print('inLabels')
    print(inLabels)
