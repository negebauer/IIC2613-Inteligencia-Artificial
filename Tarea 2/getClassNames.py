import os


def getClassNames(dir):
    list = os.listdir(dir)
    rm = '.DS_Store'
    while rm in list:
        list.remove(rm)
    return list
