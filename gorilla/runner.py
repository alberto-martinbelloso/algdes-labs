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

from cost_parser import parse_cost_file
from input_parser import extract_input_data
from model import SequenceRes, Sequence
from output_tester import test_output

# data = stdin

# print(results['A']['A'])  # 4
# print(results['A']['F'])  # -2
# print(results['R']['R'])  # 5

# cost_dict = parse_cost_file("data/BLOSUM62.txt")
# for k in cost_dict:
#     print_line = [f"{j}: {cost_dict[k][j]}" for j in cost_dict[k]]
#     print(f"{k} => {print_line}")


# result = extract_input_data(data)
# for r in result:
#     print(r)

# output = [
#     SequenceRes(Sequence("Sphinx", "KQR-------K"), Sequence("Snark", "KQRIKAAKABK"), -8),
#     SequenceRes(Sequence("Sphinx", "KQRK"), Sequence("Bandersnatch", "K-AK"), 5),
#     SequenceRes(Sequence("Snark", "KQRIKAAKABK"), Sequence("Bandersnatch", "-------KA-K"), -18),
# ]
#
# test_output(data, output)

input_file = stdin

costs = parse_cost_file("data/BLOSUM62.txt")
input_data = extract_input_data(input_file)

output = []  # put algo here

# just for testing
with open("data/HbB_FASTAs-out.txt") as file:
    test_output(file, output)
