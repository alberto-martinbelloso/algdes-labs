from model import Edge


def parse_input_to_model(file):
    temp_res = parse_input(file)
    return ParseRes(temp_res.vertexes, parse_to_edges(temp_res.edges))


def parse_input(file):
    vertexes = {}
    count = 0
    total_count = -1
    edges = []
    start = False
    for line in file:
        if total_count == -1:
            total_count = int(line)
        elif count < total_count:
            vertexes[count] = line.strip()
            count += 1
        elif (start):
            edges.append([int(x) for x in line.split(' ')])
        elif '119' in line:
            start = True

    return ParseRes(vertexes, edges)


def parse_to_edges(array_input: list) -> list:
    return [Edge(array[0], array[1], array[2]) for array in array_input]


class ParseRes:
    vertexes: dict
    edges: list

    def __init__(self, vertexes: dict, edges: list) -> None:
        self.vertexes = vertexes
        self.edges = edges
