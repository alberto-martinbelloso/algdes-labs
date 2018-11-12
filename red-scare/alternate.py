from model import Edge, Vertex, Graph
from input_parser import parse_input
from nx_parser import parse_to_nx
import networkx as nx
from sys import stdin

def alternate(graph: Graph) -> bool:
    for edge in graph.edge_list:
        if (edge.origin.is_red and edge.destination.is_red) or (not edge.origin.is_red and not edge.destination.is_red):
            graph.edge_list.remove(edge)
    G = parse_to_nx(graph.vertex_list,graph.edge_list)
    try:
        s = nx.shortest_path(G, graph.start_vertex.name, graph.end_vertex.name)
        return True
    except nx.exception.NetworkXNoPath:
        return False    

# the_file = stdin
# graph = parse_input(the_file)
# print(alternate(graph))