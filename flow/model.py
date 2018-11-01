class Edge:
    origin: int
    destination: int
    capacity: int
    flow: int
    is_reversed: bool

    def __init__(self, origin, destination, capacity, flow=0, is_reversed=False) -> None:
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.flow = flow
        self.is_reversed = is_reversed

    def __str__(self) -> str:
        return f"(origin: {self.origin}, destination: {self.destination}, " \
               f"capacity: {self.capacity}, flow: {self.flow}, reversed: {self.is_reversed})"

    def __repr__(self) -> str:
        return self.__str__()

    def is_overflown(self) -> bool:
        return self.current_capacity() == 0

    def has_space(self):
        return not self.is_overflown()

    def current_capacity(self) -> int:
        return self.capacity - self.flow if self.capacity != -1 else -1

    def reverse(self):
        return Edge(self.destination, self.origin, self.capacity, 0, True)


