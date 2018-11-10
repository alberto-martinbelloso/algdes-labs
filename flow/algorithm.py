from typing import Optional


def maximum_flow(edges: list, source: int, sink: int) -> list:
    edge_dict = make_edge_dict(edges)

    flow_res = breadth_first_search(edge_dict, source, sink)
    while flow_res is not None:
        fill_flow(flow_res)
        update_reverse_edges(flow_res, edge_dict)
        flow_res = breadth_first_search(edge_dict, source, sink)


    all_edges = [edge for key in edge_dict for edge in edge_dict[key]]
    return [edge for edge in all_edges if edge.flow > 0]


def breadth_first_search(edges: dict, source: int, sink: int) -> Optional[list]:
    queue = []
    parents = {}
    visited = []

    queue.append(source)

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node in edges:
            for edge in edges[current_node]:
                if edge.has_space() and edge.destination not in visited:
                    visited.append(edge.destination)
                    queue.append(edge.destination)
                    parents[edge.destination] = current_node
                    if edge.destination == sink:
                        return create_path(parents, edges, source, sink)

    return None


def create_path(parents: dict, edges: dict, source: int, sink: int) -> list:
    path = []
    current_node = sink
    while current_node is not source:
        parent = parents[current_node]
        edge = next(e for e in edges[parent] if e.destination == current_node)
        path.append(edge)
        current_node = parent

    return list(reversed(path))


def make_edge_dict(edges: list) -> dict:
    edge_dict = {}

    for edge in edges:
        add_el_to_list_in_dict(edge_dict, edge, edge.origin)
        add_el_to_list_in_dict(edge_dict, edge.reverse(), edge.destination)

    for v in edge_dict:
        for edge in edge_dict[v]:
            if edge.is_reversed:
                edges.append(edge)

    return edge_dict


def add_el_to_list_in_dict(dictionary: dict, element, key):
    if key in dictionary:
        dictionary[key].append(element)
    else:
        dictionary[key] = [element]


def has_not_overflown_edges(edges: list) -> bool:
    return any(edge.has_space() for edge in edges)


def fill_flow(edge_path: list) -> None:
    bottleneck = min(edge.current_capacity() for edge in edge_path if edge.capacity != -1)
    for edge in edge_path:
        edge.flow += bottleneck


def update_reverse_edges(filled_edges: list, edges: dict) -> None:
    for edge in filled_edges:
        rev = next(r for r in edges[edge.destination] if
                   r.is_reversed != edge.is_reversed and r.destination == edge.origin)
        rev.capacity += edge.flow
