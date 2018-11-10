def minimum_cut(all_edges: list, source: int) -> list:
    edges = remove_overflow_edges(all_edges)
    visitable = find_visitable(edges, source)
    cut = []
    for edge in all_edges:
        if edge.origin in visitable and edge.destination not in visitable:
            cut.append(edge)

    return cut


def find_visitable(non_overflown_edges, source: int) -> list:
    to_visit = [source]
    visited = []
    while len(to_visit) > 0:
        current_node = to_visit.pop(0)
        visited.append(current_node)
        for edge in non_overflown_edges:
            if edge.origin == current_node:
                if edge.destination not in to_visit and edge.destination not in visited:
                    to_visit.append(edge.destination)
    return visited

def remove_overflow_edges(all_edges: list) -> list:
    return [edge for edge in all_edges if not edge.is_overflown()]
