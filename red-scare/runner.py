from sys import stdin

from input_parser import parse_input
from many import many

input_data = stdin

graph = parse_input(input_data)
many_res = many(graph)
print(many_res)
