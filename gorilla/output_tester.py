import re
from itertools import zip_longest

from model import SequenceRes, Sequence


def test_output(output_file: str, data: list) -> None:
    expected_result = extract_output(output_file)
    assert len(expected_result) == len(data), "Length of outputs didn't match"

    for i in range(len(expected_result)):
        assert expected_result[i] == data[i], f"{expected_result[i]} is not {data[i]}"

    print("Test successful")


def extract_output(output_file) -> list:
    result = []
    grouped_file = grouper(3, output_file)
    for head_line, first_seq_line, second_seq_line in grouped_file:
        result.append(parse_lines(head_line, first_seq_line, second_seq_line))

    return result


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def parse_lines(head_line: str, first_seq_line: str, second_seq_line: str) -> SequenceRes:
    head_args = re.split(r"(?:--)|(?:: )", head_line)
    assert len(head_args) == 3
    first_seq = Sequence(head_args[0], first_seq_line.strip())
    second_seq = Sequence(head_args[1], second_seq_line.strip())
    return SequenceRes(first_seq, second_seq, int(head_args[2]))
