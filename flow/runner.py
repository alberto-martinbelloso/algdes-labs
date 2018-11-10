from sys import stdin

from algorithm import maximum_flow
from input_parser import parse_input_to_model
from min_cut_algo import minimum_cut

cmd_input = stdin
input_res = parse_input_to_model(cmd_input)
edges = input_res.edges
vertexes = input_res.vertexes

result = maximum_flow(edges, 0, 54)

flow = sum(r.flow for r in result if r.origin == 0)

print (flow)
cut_res = minimum_cut(edges, 0)
for r in cut_res:
    print(r.origin, r.destination, r.capacity)



