import networkx as nx

def parse_to_nx(vertex_list, edge_list, towards_black_weight = None, towards_red_weight = None) -> nx.Graph:
    G = nx.Graph()
    
    for v in vertex_list:
        G.add_node(v.name)

    for e in edge_list:
        if(towards_black_weight != None and towards_red_weight != None):
            if(e.destination.is_red):
                G.add_edge(e.origin.name, e.destination.name, weight=towards_red_weight)
            else:
                G.add_edge(e.origin.name, e.destination.name, weight=towards_black_weight)
        else:
            G.add_edge(e.origin.name, e.destination.name)
            G.add_edge(e.destination.name, e.origin.name)
            
    return G