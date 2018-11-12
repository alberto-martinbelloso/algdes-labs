from networkx import NetworkXNoPath
from networkx.algorithms import is_directed_acyclic_graph, dag_longest_path_length

from nx_parser import parse_to_nx


def many(graph) -> int:
    nx_graph = parse_to_nx(graph.vertex_list, graph.edge_list, 0, 1)

    try:
        if not is_directed_acyclic_graph(nx_graph):
            return -2

        return dag_longest_path_length(nx_graph)
    except NetworkXNoPath:
        return -1
