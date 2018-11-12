from model import Graph, Vertex, Edge
import networkx as nx
from nx_parser import parse_to_nx
from input_parser import parse_input
from sys import stdin

def some(graph: Graph) -> bool:
    if(graph.number_red_vertex == 0):
        return False

    G = parse_to_nx(graph.vertex_list, graph.edge_list)

    for v in graph.vertex_list:
        if(v.is_red):
            try:
                s1 = nx.shortest_path(G, graph.start_vertex.name, v.name)
                s2 = nx.shortest_path(G, v.name, graph.end_vertex.name)
                return True
            except nx.exception.NetworkXNoPath:
                continue
    
    return False
                
# the_file = stdin
# graph = parse_input(the_file)
# print(some(graph))