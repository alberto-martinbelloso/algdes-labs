class Edge:
    origin = None
    destination = None

    def __init__(self, origin, destination) -> None:
        self.origin = origin
        self.destination = destination

    def __str__(self) -> str:
        return f"(origin: {self.origin}, destination: {self.destination}, "

    def __repr__(self) -> str:
        return self.__str__()


class Vertex:
    name: str
    is_red: bool

    def __init__(self, name, is_red):
        self.name = name
        self.is_red = is_red

    def __str__(self) -> str:
        return f"(name: {self.name}, is_red: {self.is_red}, "

    def __repr__(self) -> str:
        return self.__str__()