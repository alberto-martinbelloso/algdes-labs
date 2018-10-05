class Sequence:
    name: str
    seq: str

    def __init__(self, name: str, seq: str) -> None:
        super().__init__()
        self.name = name
        self.seq = seq

    def __str__(self) -> str:
        return f"(name: {self.name}, seq: {self.seq})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Sequence):
            return self.name == o.name and self.seq == o.seq
        return False


class SequenceRes:
    first_seq: Sequence
    second_seq: Sequence
    value: int

    def __init__(self, first_seq: Sequence, second_seq: Sequence, value: int) -> None:
        super().__init__()
        self.first_seq = first_seq
        self.second_seq = second_seq
        self.value = value

    def __str__(self) -> str:
        return f"(first: {self.first_seq}, second: {self.second_seq}, value: {self.value})"

    def __repr__(self) -> str:
        return f"(first: {self.first_seq},\n second: {self.second_seq},\n value: {self.value})"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, SequenceRes):
            return self.value == o.value and self.first_seq == o.first_seq and self.second_seq == o.second_seq
        return False
