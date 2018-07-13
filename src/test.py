from __future__ import print_function

import pickle

from sklearn_crfsuite import metrics

from data_helpers import read_data, sent2label
from features.features import chunking_sent2features
from CONSTANT import ROOT_DIR
import argparse


def parseArgument():
    """
    Parse argument from commandline:
        Required arguments:


        Optional arguments:
            -model --model      :   Name of the model (will be saved on disk). Default chunk.pkl (add indices if duplicated)
            -i --iter       :   Max iteration for optimization. Default 300
            -e --epsilon    :   epsilon - stopping criteria. Default 1e-5
    :return: args: args list.
    """

    parser = argparse.ArgumentParser(description="Chunking")

    parser.add_argument("-model", metavar="model", type=unicode, required=True, default="chunk1.pkl",
                        help="Name of the model which will be tested")

    # parser.add_argument("-i", metavar="iter", type=int, default=300, help="Max iteration for optimization. Default 300")
    # parser.add_argument("-d", metavar="delta", type=float, default=1e-5, help="stopping criteria. Default 1e-5")

    return parser.parse_args()


def evaluate(sent_pred, sent_true, delim='-'):
    """
    Determine to what extent 2 sentences are similar
    Each sentence was segmentated into chunks with tag for each word of that chunk.
    Each chunk is considered to be matched if these two tupples of string are identical:

        (posBEGIN1_posEND1, tagWORD1_tagWORD2_...) = (posBEGIN2_posEND2, tagWORD2_tagWORD2_...) (****)

    (****) each sentence will be transform to a list of this format by *_transform(sent)*


    :param delim: tags are started with B- or B_
    :param sent_pred: [(word, word chunk tag)] (tag is in IOB format, different from postag: B-NP, I-NP, ....)
    :param sent_true: same
    :return: num(match) / len(chunked sent)
    """
    B = "B" + delim
    I = "I" + delim

    def _transform(sent, delim=delim):
        """
        transform chunked sentence into a list of (****) format
        :param sent: [(word, word chunk tag)] (tag is in IOB format, different from postag: B-NP, I-NP, ....)
        :return: [(posBEGIN1_posEND1, tagWORD1_tagWORD_2...)]
        """

        result = []

        i = 0
        tmp = ""
        while i < len(sent):
            if B in sent[i]:
                if i == len(sent) - 1:
                    result.append(str(i) + "_" + str(i) + "_" + sent[i])
                    break

                if I not in sent[i + 1]:
                    result.append(str(i) + "_" + str(i) + "_" + sent[i])
                else:
                    tmp += sent[i] + "_"
                    for j in range(i + 1, len(sent)):
                        if I in sent[j]:
                            tmp += sent[j] + "_"
                        else:
                            nextBpos = j - 1
                            break

                    try:
                        nextBpos
                    except UnboundLocalError:
                        nextBpos = len(sent) - 1

                    result.append(str(i) + "_" + str(nextBpos) + "_" + tmp.strip("_"))
                    tmp = ""
            elif sent[i] == "O":
                result.append(str(i) + "_" + str(i) + "_" + sent[i])

            i += 1  # TODO
            # # test_sentence = [(u'T\xe0i li\u1ec7u', 'N', 'B-NP'), (u'n\xe0y', 'P', 'I-NP'), (u'c\xf3', 'V', 'I-VP'), (u'm\u1ee5c \u0111\xedch', 'N', 'B-NP'), (u'li\u1ec7t k\xea', 'V', 'O'), (u'v\xe0', 'C', 'O'), (u'n\xeau', 'V', 'B-VP'), (u'ra', 'R', 'O'), (u'\xfd ngh\u0129a', 'A', 'B-AP'), (u'c\u1ee7a', 'E', 'I-VP'), (u'c\xe1c', 'L', 'I-NP'), (u'nh\xe3n chunking', 'N', 'B-NP'), (u'trong', 'E', 'B-PP'), (u'c\xe1c', 'L', 'B-NP'), (u'corpus', 'Nb', 'B-NP'), (u'ti\u1ebfng', 'N', 'I-NP'), (u'Vi\u1ec7t', 'Np', 'B-NP'), (u'.', '.', 'O'), (u'Sau', 'E', 'B-PP'), (u'\u0111\xf3', 'P', 'B-NP'), (u'\u0111\u01b0a', 'V', 'B-VP'), (u'ra', 'R', 'O'), (u'\xe1nh', 'Nc', 'B-NP'), (u'x\u1ea1', 'N', 'B-NP'), (u'chung', 'A', 'B-AP'), (u'v\xe0', 'C', 'O'), (u'chu\u1ea9n h\xf3a', 'V', 'B-VP'), (u'c\xe1c', 'L', 'B-NP'), (u'nh\xe3n chunking', 'N', 'I-PP'), (u'.', '.', 'O')]
            # pred_sentence = [(u'T\xe0i li\u1ec7u', 'N', 'B-NP'), (u'n\xe0y', 'P', '-NP'), (u'c\xf3', 'V', 'I-VP'), (u'm\u1ee5c \u0111\xedch', 'N', 'B-NP'), (u'li\u1ec7t k\xea', 'V', 'O'), (u'v\xe0', 'C', 'O'), (u'n\xeau', 'V', 'B-VP'), (u'ra', 'R', 'O'), (u'\xfd ngh\u0129a', 'A', 'B-AP'), (u'c\u1ee7a', 'E', 'I-VP'), (u'c\xe1c', 'L', 'I-NP'), (u'nh\xe3n chunking', 'N', 'B-NP'), (u'trong', 'E', 'B-PP'), (u'c\xe1c', 'L', 'B-NP'), (u'corpus', 'Nb', 'B-NP'), (u'ti\u1ebfng', 'N', 'I-NP'), (u'Vi\u1ec7t', 'Np', 'B-NP'), (u'.', '.', 'O'), (u'Sau', 'E', 'B-PP'), (u'\u0111\xf3', 'P', 'B-NP'), (u'\u0111\u01b0a', 'V', 'B-VP'), (u'ra', 'R', 'O'), (u'\xe1nh', 'Nc', 'B-NP'), (u'x\u1ea1', 'N', 'B-NP'), (u'chung', 'A', 'B-AP'), (u'v\xe0', 'C', 'O'), (u'chu\u1ea9n h\xf3a', 'V', 'B-VP'), (u'c\xe1c', 'L', 'B-NP'), (u'nh\xe3n chunking', 'N', 'I-PP'), (u'.', '.', 'O')]
            # print([(i, word[2]) for i, word in enumerate(test_sentence)])
        return result

    def _compare(sent_pred, sent_true):
        counter = 0
        for word in sent_true:
            if B in word or word == "O":
                counter += 1
        # print(len(set(_transform(sent_pred)) & set(_transform(sent_true))), counter)
        return len(set(_transform(sent_pred)) & set(_transform(sent_true))) / float(counter)

    return _compare(sent_pred, sent_true)


def predict(sent, model):
    """
    This will perform prediction for a (segmentated and tagged) sentence
    :param sent:
    :return:
    """

    raise NotImplementedError

if __name__ == "__main__":
    # test_sentence = [(u'T\xe0i li\u1ec7u', 'N', 'B-NP'), (u'n\xe0y', 'P', 'I-NP'), (u'c\xf3', 'V', 'I-VP'),
    #                  (u'm\u1ee5c \u0111\xedch', 'N', 'B-NP'), (u'li\u1ec7t k\xea', 'V', 'O'), (u'v\xe0', 'C', 'O'),
    #                  (u'n\xeau', 'V', 'B-VP'), (u'ra', 'R', 'O'), (u'\xfd ngh\u0129a', 'A', 'B-AP'),
    #                  (u'c\u1ee7a', 'E', 'I-VP'), (u'c\xe1c', 'L', 'I-NP'), (u'nh\xe3n chunking', 'N', 'B-NP'),
    #                  (u'trong', 'E', 'B-PP'), (u'c\xe1c', 'L', 'B-NP'), (u'corpus', 'Nb', 'B-NP'),
    #                  (u'ti\u1ebfng', 'N', 'I-NP'), (u'Vi\u1ec7t', 'Np', 'B-NP'), (u'.', '.', 'O'),
    #                  (u'Sau', 'E', 'B-PP'), (u'\u0111\xf3', 'P', 'B-NP'), (u'\u0111\u01b0a', 'V', 'B-VP'),
    #                  (u'ra', 'R', 'O'), (u'\xe1nh', 'Nc', 'B-NP'), (u'x\u1ea1', 'N', 'B-NP'), (u'chung', 'A', 'B-AP'),
    #                  (u'v\xe0', 'C', 'O'), (u'chu\u1ea9n h\xf3a', 'V', 'B-VP'), (u'c\xe1c', 'L', 'B-NP'),
    #                  (u'nh\xe3n chunking', 'N', 'I-PP'), (u'.', '.', 'O')]
    # pred_sentence = [(u'T\xe0i li\u1ec7u', 'N', 'B-NP'), (u'n\xe0y', 'P', 'B-NP'), (u'c\xf3', 'V', 'I-VP'),
    #                  (u'm\u1ee5c \u0111\xedch', 'N', 'B-NP'), (u'li\u1ec7t k\xea', 'V', 'O'), (u'v\xe0', 'C', 'O'),
    #                  (u'n\xeau', 'V', 'B-VP'), (u'ra', 'R', 'O'), (u'\xfd ngh\u0129a', 'A', 'B-AP'),
    #                  (u'c\u1ee7a', 'E', 'I-VP'), (u'c\xe1c', 'L', 'I-NP'), (u'nh\xe3n chunking', 'N', 'B-NP'),
    #                  (u'trong', 'E', 'B-PP'), (u'c\xe1c', 'L', 'B-NP'), (u'corpus', 'Nb', 'B-NP'),
    #                  (u'ti\u1ebfng', 'N', 'I-NP'), (u'Vi\u1ec7t', 'Np', 'B-NP'), (u'.', '.', 'O'),
    #                  (u'Sau', 'E', 'B-PP'), (u'\u0111\xf3', 'P', 'B-NP'), (u'\u0111\u01b0a', 'V', 'B-VP'),
    #                  (u'ra', 'R', 'O'), (u'\xe1nh', 'Nc', 'B-NP'), (u'x\u1ea1', 'N', 'B-NP'), (u'chung', 'A', 'B-AP'),
    #                  (u'v\xe0', 'C', 'O'), (u'chu\u1ea9n h\xf3a', 'V', 'B-VP'), (u'c\xe1c', 'L', 'B-NP'),
    #                  (u'nh\xe3n chunking', 'N', 'I-PP'), (u'.', '.', 'I-NP')]
    # print(evaluate(pred_sentence, test_sentence))
    # args = parseArgument()
    # MODEL_NAME = args.model
    MODEL_NAME = "chunk.pkl"

    # Transform text data to feature
    test_sents = read_data(ROOT_DIR + "/data/ner/vlsp2016/corpus/test.txt")

    X_test = [chunking_sent2features(sent=sent, mode='test') for sent in test_sents]
    y_test = [sent2label(sent) for sent in test_sents]

    print(list(set([x for sent in y_test for x in sent])))
    # Load trained model
    print("=======================")
    print("Load trained model ...")
    model = pickle.load(open("./models/" + MODEL_NAME, "rb"))
    print("Done!!!")

    predict = model.predict(X_test)

    print("=======================")
    print("Testing ....")
    print(len(y_test), len(predict))

    avg_count = 0
    print(predict[0])
    for i in range(len(y_test)):
        acc = evaluate(predict[i], y_test[i])
        # print(acc)
        avg_count += acc

    # print(score)

    print("Avg acc:", avg_count/float(len(y_test)))
    print(model.classes_)
    print("Accuracy\t:", metrics.flat_accuracy_score(y_test, predict))
    print("Precision\t:", metrics.flat_precision_score(y_test, predict, average=None))
    print("Recall\t:", len(metrics.flat_recall_score(y_test, predict, average=None)))
    print("F1\t:", metrics.flat_f1_score(y_test, predict, average=None))

    print("Done!!!")
