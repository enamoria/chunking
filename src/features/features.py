# coding=utf-8
"""
Feature engineering procedure is defined here.
"""

from feature_function import *


def chunking_word2features(sent, i, mode):
    if mode == "raw":  # Do not confused raw mode with test mode: input in raw mode is raw text, while test mode input have pos-tag and were segmentated beforehand
        # This mode won't be encountered in real problem: raw sentence will be segmentated and tagged before chunking
        word = sent[i]  # Just splited text, no label
        word1 = sent[i - 1] if i >= 1 else ""
        word2 = sent[i - 2] if i >= 2 else ""
        word3 = sent[i - 3] if i >= 3 else ""
        word4 = sent[i - 4] if i >= 4 else ""
        postag = ''
        postag1 = ''
    else:  # Train or test mode: in test mode, input string will be output of pos-tag, which was segmentated and tagged
        word = sent[i][0]  # Labeled (both pos and chunk)
        word1 = sent[i - 1][0] if i >= 1 else ""
        word2 = sent[i - 2][0] if i >= 2 else ""
        word3 = sent[i - 3][0] if i >= 3 else ""
        word4 = sent[i - 4][0] if i >= 4 else ""
        postag = sent[i][1]
        postag1 = sent[i-1][1]

    features = {
        'sent[-4:]': word4,
        'sent[-3:]': word3,
        'sent[-2:]': word2,
        'sent[-1:]': word1,
        'word.lower': word.lower(),

        'postag': postag,  # New feature, compare to ws and postag
        'postag1': postag1,

        'isNumber': isNumber(word),
        'punc&sym': isPunc(word),
        'isBOS': i == 0,
        'isEOS': i == (len(sent) - 1),
        'num_tok': len(word.split("_")),
        'word.istitle': word.istitle(),
        'word.isupper': word.isupper(),
        'word.ispunc': isPunc(word)
    }

    return features
    # raise NotImplementedError


def chunking_sent2features(sent, mode="test"):
    return [chunking_word2features(sent, i, mode) for i in range(len(sent))]
    # raise NotImplementedError


if __name__ == "__main__":
    xxx = "Một chuyến hải_trình xuyên ba nước Malaysia , Singapore , Indonesia vừa được phóng_viên Tuổi_Trẻ thực_hiện , để cảm_nhận điều mà các thuỷ_thủ tàu viễn_dương đã cảm_nhận mỗi khi nghe nhắc tới : hải_tặc eo_biển Malacca ! ..."

    print(chunking_sent2features(xxx.split(" "), "test"))
