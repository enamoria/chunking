from __future__ import print_function
import os


def read_data(filepath):
    """
    Read data in filepath. Currently only support ConLL format
    :param filepath: Abspath
    :return: [ [ [word, postag, chunktag] ] ]
               \  \       word         / /
                \  -------------------- /
                 \       sentence      /
                  ---------------------

    """
    print("=======================")
    print("Reading data .... ")

    try:
        f = open(filepath, "r")

        data = f.read().strip("\n").strip(" ").split("\n\n")

        tmp = [sentence.split("\n") for sentence in data]

        sents = [[word.split("\t")[:-1] for word in sentence] for sentence in tmp]

        print("Done reading!")
        return sents

    except IOError:
        print(filepath + ": File not found, terminating ...")
        exit()


def sent2label(sent):
    return [word[2] for word in sent]


def checkModelFileExistAndCreateNewModelName(name):
    i = 0
    tmp = name

    filename = "".join(name.split(".")[:-1])
    extension = name.split(".")[-1]

    while os.path.isfile(tmp):
        tmp = filename + "_" + str(i) + "." + extension
        i += 1

    if tmp != name:
        print(name, "is exist. Output file renamed to", tmp)
    else:
        print(name, "is available")
    return tmp
