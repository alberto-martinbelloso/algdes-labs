from sys import stdin

from algorithm import maximum_flow
from input_parser import parse_input_to_model


# def print_result(res: list, ver: dict):
#     data = [(ver[r.origin], str(r.origin), ver[r.destination], str(r.destination), str(r.flow), str(r.capacity)) for r in res]
#     data.insert(0, ("From", "From id", "To", "To id", "Flow", "Capacity"))
#     col_width = max(len(word) for row in data for word in row) + 2  # padding
#     for row in data:
#         print("".join(word.ljust(col_width) for word in row))
#
# def print_full_capacities(res: list, ver: dict):
#     data = [(ver[r.origin], str(r.origin), ver[r.destination], str(r.destination), str(r.flow), str(r.capacity)) for r in res if r.flow == r.capacity]
#     data.insert(0, ("From", "From id", "To", "To id", "Flow", "Capacity"))
#     col_width = max(len(word) for row in data for word in row) + 2  # padding
#     for row in data:
#         print("".join(word.ljust(col_width) for word in row))



# def calc_flow(res: list) -> int:
#     return sum(r.flow for r in res if r.destination == 54)


cmd_input = stdin
input_res = parse_input_to_model(cmd_input)
edges = input_res.edges
vertexes = input_res.vertexes

result = maximum_flow(edges, 0, 54)

for r in result:
    print(r.origin, r.destination, r.flow)

