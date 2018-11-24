import networkx as nx

from model import Graph, Result, Vertex

# these names are designed to be unlikely to conflict with actuall node names
# if one really wants to ensure that no conflict is possible one can add some escaping mechanism to the input parser
start_vertex_name = "________s"
stop_vertex_name = "________t"


def some(graph: Graph):
    if graph.number_red_vertex == 0:
        return Result.NO

    if is_directed(graph):
        return Result.UNDEFINED

    new_vertex_mapping = {
        v: SplitVertex(Vertex(v.name + "_1", v.is_red), Vertex(v.name + "_2", v.is_red)) for
        v in graph.vertex_list
    }
    nx_graph = transform_to_nx(graph, new_vertex_mapping)

    # check for every red vertex if it is possible to construct flow from start/end to the vertex
    for red_vertex in [v for v in graph.vertex_list if v.is_red]:
        nx_graph.add_edge(new_vertex_mapping[red_vertex].in_name(), stop_vertex_name, capacity=2)
        try:
            flow_value = nx.algorithms.flow.maximum_flow_value(nx_graph, start_vertex_name,
                                                               stop_vertex_name)
        except nx.NetworkXNoPath:
            flow_value = 0

        if flow_value == 2:
            return Result.YES
        nx_graph.remove_edge(new_vertex_mapping[red_vertex].in_name(), stop_vertex_name)

    return Result.NO


def is_directed(graph: Graph) -> bool:
    return graph.is_directed


def transform_to_nx(g: Graph, new_vertex_mapping: dict):
    G = nx.DiGraph()

    G.add_node(start_vertex_name)
    G.add_node(stop_vertex_name)

    for v in new_vertex_mapping:
        v_in = new_vertex_mapping[v].in_name()
        v_out = new_vertex_mapping[v].out_name()
        G.add_node(v_in)
        G.add_node(v_out)
        G.add_edge(v_in, v_out, capacity=1)

    G.add_edge(start_vertex_name, new_vertex_mapping[g.start_vertex].in_name(), capacity=1)
    G.add_edge(start_vertex_name, new_vertex_mapping[g.end_vertex].in_name(), capacity=1)

    for e in g.edge_list:
        new_origin = new_vertex_mapping[e.origin].out_name()
        new_dest = new_vertex_mapping[e.destination].in_name()
        G.add_edge(new_origin, new_dest)

    return G


class SplitVertex:
    _1 = None
    _2 = None

    def __init__(self, v_in, v_out) -> None:
        self._1 = v_in
        self._2 = v_out

    def in_name(self) -> str:
        return self._1.name

    def out_name(self) -> str:
        return self._2.name
