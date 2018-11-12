import networkx as nx
from nx_parser import parse_to_nx
from model import Graph, Vertex, Edge
from sys import stdin
from input_parser import parse_input


def few(graph: Graph) -> int:
    if (graph.number_red_vertex == 0):
        return -1

    G = parse_to_nx(graph.vertex_list, graph.edge_list, 0, 1)
    shortest_path_vertex_list = []
    try:
        shortest_path_name_list = nx.shortest_path(G, graph.start_vertex.name,
                                                   graph.end_vertex.name)
    except nx.NetworkXNoPath:
        return -1

    for name in shortest_path_name_list:
        shortest_path_vertex_list = [x for x in graph.vertex_list if x.name == name]

    shortest_red_vertex_list = [x for x in shortest_path_vertex_list if x.is_red]
    return len(shortest_red_vertex_list)

# the_file = stdin
# graph = parse_input(the_file)
# print(few(graph))
