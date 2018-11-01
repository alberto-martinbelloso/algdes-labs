from algorithm import maximum_flow
from input_parser import parse_input_to_model, parse_vertexes


def print_result(res: list, ver: dict):
    data = [(ver[r.origin], ver[r.destination], str(r.flow), str(r.capacity)) for r in res]
    data.insert(0, ("From", "To", "Flow", "Capacity"))
    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print("".join(word.ljust(col_width) for word in row))


vertexes = parse_vertexes()
edges = parse_input_to_model()

result = maximum_flow(edges, 0, 54)
print_result(result, vertexes)
