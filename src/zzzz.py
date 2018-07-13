#
# transition = {'FW->O': 36, 'P->B-NP': 18288, 'V->B-AP': 1, 'N->O': 7, 'Ny->O': 1, 'X->I-NP': 4, 'A->B-VP': 1, 'Np->O': 2, 'FW->B-AP': 2, 'Nc->B-NP': 14303, 'E->B-NP': 4, 'FW->B-PP': 2, 'V->I-VP': 15, 'A->B-NP': 19, 'CH->B-NP': 70, 'E->I-NP': 9, 'Vy->I-NP': 1, 'I->O': 231, 'N->I-NP': 972, 'Np->I-NP': 8401, 'Np->B-NP': 14893, 'M->O': 4, 'T->O': 2395, 'A->I-AP': 6, 'CH->I-NP': 281, 'V->B-VP': 87906, 'FW->B-VP': 8, 'X->O': 1491, 'A->B-AP': 25936, 'C->O': 15996, 'A->I-NP': 63, 'C->B-NP': 2, 'E->O': 3, 'R->O': 28486, 'L->B-NP': 8132, 'X->B-NP': 2, 'E->B-PP': 26343, 'Z->O': 106, 'Vy->B-VP': 7, 'Nc->I-NP': 8, 'X->B-VP': 1, 'FW->I-NP': 32, 'CH->O': 60658, 'M->B-NP': 14536, 'V->I-NP': 160, 'FW->B-NP': 823, 'Nc->O': 1, 'Ny->B-NP': 1490, 'Np->B-AP': 9, 'Nu->B-NP': 2047, 'C->I-NP': 15, 'L->I-NP': 5, 'R->B-NP': 4, 'Np->B-PP': 1, 'N->B-NP': 100627, 'Ny->I-NP': 235, 'M->I-NP': 374, 'V->B-NP': 34}
# keys = []
# for key in transition:
#     keys.append(key.split("->")[0])
#
# print(len(keys), keys)
# print(len(list(set(keys))))

from src.features.features import *
import os
import sys

# sys.path.append()
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
