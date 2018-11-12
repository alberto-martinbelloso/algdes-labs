import networkx as nx
from nx_parser import parse_to_nx


def none(graph):
    """
    - None
        Remove all the red vertices (except start and finish) and edges to them
        Find shortest path
        Returns the shortest path
        If no such path exists return -1
    """
    try:
        remove_red_vertices(graph)
        g = parse_to_nx(graph.vertex_list,graph.edge_list)
        print("Calculating path")
        path = nx.shortest_path(g, source = graph.start_vertex.name, target = graph.end_vertex.name)
        if len(path) > 0:
            return path
        else:
            return -1
    except Exception:
        print("Path not found!")
        return -1


def remove_red_vertices(graph):
    print("removing red vertices")
    removed = []
    for v in graph.vertex_list[::-1]:
        if v != graph.start_vertex and v != graph.end_vertex:
            if v.is_red:
                graph.vertex_list.remove(v)
                removed.append(v.name)

    for e in graph.edge_list[::-1]:
        if e.origin.name in removed or e.destination.name in removed:
            graph.edge_list.remove(e)

    return graph


# cmd_input = stdin
# print("Parsing...")
# input_res = parse_input(cmd_input)
#
#
# print(none(input_res))

