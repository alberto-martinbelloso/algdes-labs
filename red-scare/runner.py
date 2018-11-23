from sys import stdin

from alternate import alternate
from few import few
from input_parser import parse_input
from many import many
from none import none
from some import some

input_data = stdin
graph = parse_input(input_data)
none_res = none(graph)
some_res = some(graph)
few_res = few(graph)
many_res = many(graph)
alternate_res = alternate(graph)

print(f"None => {none_res}")
print(f"Some => {some_res}")
print(f"Few => {few_res}")
print(f"Many => {many_res}")
print(f"Alternate => {alternate_res}")

