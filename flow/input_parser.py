from model import Edge


def parse_input_to_model():
    return parse_to_edges(parse_input())


def parse_input():
    start = False
    array = []
    with open('./data/rail.txt') as f:
        for line in f:
            if (start):
                array.append([int(x) for x in line.split(' ')])

            if ('119' in line):
                start = True

    return array


def parse_to_edges(array_input: list) -> list:
    return [Edge(array[0], array[1], array[2]) for array in array_input]


def parse_vertexes() -> dict:
    vertexes = {}
    count = 0
    total_count = -1
    with(open('./data/rail.txt')) as f:
        for line in f:
            if total_count == -1:
                total_count = int(line)
            elif count < total_count:
               vertexes[count] = line.strip()
               count += 1
            else:
                break
    return vertexes

