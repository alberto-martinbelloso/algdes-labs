import networkx as nx
from model import Graph
from nx_parser import parse_to_nx


def none(graph: Graph) -> int:
    """
        Remove all the red vertices (except start and finish) and edges to them
        Find shortest path
        Returns the length of the shortest path
        If no such path exists return -1
    """
    edges = only_black_edges(graph.edge_list, (graph.start_vertex, graph.end_vertex))
    vertexes = only_black_vertexes(graph.vertex_list, (graph.start_vertex, graph.end_vertex))

    try:
        g = parse_to_nx(vertexes, edges)
        length = nx.shortest_path_length(g, source=graph.start_vertex.name,
                                         target=graph.end_vertex.name)
        if length > 0:
            return length
        else:
            return -1
    except nx.NetworkXNoPath:
        return -1


def only_black_edges(edge_list: list, non_removable_vertexes: tuple) -> list:
    return [edge for edge in edge_list if not is_removable_red_edge(edge, non_removable_vertexes)]


def only_black_vertexes(vertexes: list, non_removable_vertexes: tuple) -> list:
    return [v for v in vertexes if not v.is_red or v in non_removable_vertexes]


def is_removable_red_edge(edge, non_removable_vertexes: tuple) -> bool:
    return (edge.origin not in non_removable_vertexes and edge.origin.is_red) or \
           (edge.destination.is_red and edge.destination not in non_removable_vertexes)

# cmd_input = stdin
# print("Parsing...")
# input_res = parse_input(cmd_input)
#
#
# print(none(input_res))
