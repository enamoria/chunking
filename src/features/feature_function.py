"""
    This  specify some feature function for CRF
"""

from CONSTANT import punctuations_and_symbols


def isNumber(s):
    """
    return True if string s is a number, by trying casting s to float
    :param s:
    :return:
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def isPunc(s):
    """
    return True if string s is punctuation or symbols by searching a predefined symbols list
    :param s:
    :return:
    """
    if s in punctuations_and_symbols:
        return True
    return False


def isDate(s):
    """
    return True if string s is date
    :param s:
    :return:
    """
    raise NotImplementedError


def isNp(s):
    # TODO Need a dicktionary here
    # This implementation only handle Np which has more than 2 syllables. 1 syllable Np is temporary ignored
    if s.split("_") > 1 and s.istitle():
        return True
    return False

    # raise NotImplementedError
