from __future__ import print_function

from data_helpers import read_data, sent2label
from src.CONSTANT import ROOT_DIR
from src.features.features import chunking_sent2features

MODEL_NAME = "chunk.pkl"
# Read data
train_sents = read_data(ROOT_DIR + "/data/ner/vlsp2016/corpus/train.txt")
dev_sents = read_data(ROOT_DIR + "/data/ner/vlsp2016/corpus/dev.txt")
test_sents = read_data(ROOT_DIR + "/data/ner/vlsp2016/corpus/test.txt")

# Transform text data to feature
X_train = [chunking_sent2features(sent=sent, mode='train') for sent in train_sents]
y_train = [sent2label(sent) for sent in train_sents]

X_dev = [chunking_sent2features(sent=sent, mode='dev') for sent in dev_sents]
y_dev = [sent2label(sent) for sent in dev_sents]

X_test = [chunking_sent2features(sent=sent, mode='test') for sent in test_sents]
y_test = [sent2label(sent) for sent in test_sents]

transition = {}
for dataset in (train_sents, dev_sents, test_sents):
    for sent in dataset:
        for word in sent:
            tmp = word[1] + "->" + word[2]
            if tmp not in transition:
                transition[tmp] = 1
            else:
                transition[tmp] += 1

# for item in sorted(transition):
#     print(item, transition[item])

print(transition)
# transition = [(v, k) for k, v in transition.iteritems()]
# transition.sort(reverse=True)  # natively sort tuples by first element
# for v, k in transition:
#     print("%s: %d" % (k, v))
#
# print(len(transition))
