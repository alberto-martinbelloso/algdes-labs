#
# Sphinx--Snark: -8
# KQR-------K
# KQRIKAAKABK
# Sphinx--Bandersnatch: 5
# KQRK
# K-AK
# Snark--Bandersnatch: -18
# KQRIKAAKABK
# -------KA-K
#
from sys import stdin

from input_parser import extract_input_data
from model import SequenceRes, Sequence
from output_tester import test_output

data = stdin

# output = [
#     SequenceRes(Sequence("Sphinx", "KQR-------K"), Sequence("Snark", "KQRIKAAKABK"), -8),
#     SequenceRes(Sequence("Sphinx", "KQRK"), Sequence("Bandersnatch", "K-AK"), 5),
#     SequenceRes(Sequence("Snark", "KQRIKAAKABK"), Sequence("Bandersnatch", "-------KA-K"), -18),
# ]
#
# test_output(data, output)


result = extract_input_data(data)
for r in result:
    print(r)
