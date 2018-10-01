import re
from functools import reduce
from itertools import takewhile

from model import Sequence


class RawDataObject:
    head_line: str
    data_lines: list

    def __init__(self) -> None:
        super().__init__()
        self.head_line = ""
        self.data_lines = []


def extract_input_data(input_data: str) -> list:
    raw_data = extract_raw_data(input_data)
    return [parse_raw_to_sequence(raw) for raw in raw_data]


def extract_raw_data(input_data: str) -> list:
    current_data: RawDataObject = None
    result_data = []
    for line in input_data:
        if line.startswith(">"):
            if current_data is not None:
                result_data.append(current_data)

            current_data = RawDataObject()
            current_data.head_line = line
        else:
            current_data.data_lines.append(line)

    if current_data is not None:
        result_data.append(current_data)

    return result_data


def parse_raw_to_sequence(raw_data: RawDataObject) -> Sequence:
    head_args = raw_data.head_line.strip(">").split()
    name_args = takewhile(lambda el: not re.fullmatch("\d+", el), head_args)
    name = reduce(lambda el, acc: el + " " + acc, name_args, "").strip()
    seq = reduce(lambda el, acc: el + acc.strip(), raw_data.data_lines, "")
    return Sequence(name, seq)
