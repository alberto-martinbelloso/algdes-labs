import networkx as nx

from model import Graph
from nx_parser import parse_to_nx


def alternate(graph: Graph) -> bool:
    alternating_edges = only_alternating_edges(graph.edge_list)
    G = parse_to_nx(graph.vertex_list, alternating_edges)
    try:
        s = nx.shortest_path(G, graph.start_vertex.name, graph.end_vertex.name)
        return True
    except nx.exception.NetworkXNoPath:
        return False

    # the_file = stdin


# graph = parse_input(the_file)
# print(alternate(graph))


def only_alternating_edges(edges: list) -> list:
    return [edge for edge in edges if edge.origin.is_red != edge.destination.is_red]
