from enum import Enum


class Edge:
    origin = None
    destination = None

    def __init__(self, origin, destination) -> None:
        self.origin = origin
        self.destination = destination

    def __str__(self) -> str:
        return f"(origin: {self.origin}, destination: {self.destination})"

    def __repr__(self) -> str:
        return self.__str__()


class Vertex:
    name: str
    is_red: bool

    def __init__(self, name, is_red):
        self.name = name
        self.is_red = is_red

    def __str__(self) -> str:
        return f"(name: {self.name}, is_red: {self.is_red})"

    def __repr__(self) -> str:
        return self.__str__()


class Graph:
    number_red_vertex: int
    start_vertex = None
    end_vertex = None
    vertex_list = None
    edge_list = None

    def __init__(self, start_vertex, end_vertex, vertex_list, edge_list, number_red_vertex) -> None:
        self.number_red_vertex = number_red_vertex
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def __str__(self) -> str:
        return f"(number_red_vertex: {self.number_red_vertex}, start_vertex: {self.start_vertex}, " \
               f"end_vertex: {self.end_vertex}, vertex_list: {self.vertex_list}, edge_list: {self.edge_list})"

    def __repr__(self) -> str:
        return self.__str__()


class Result(Enum):
    YES = 1
    NO = 2
    UNDEFINED = 3