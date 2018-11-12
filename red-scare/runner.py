from sys import stdin

from input_parser import parse_input
from many import many
from none import none

input_data = stdin

graph = parse_input(input_data)
many_res = none(graph)
print(many_res)
