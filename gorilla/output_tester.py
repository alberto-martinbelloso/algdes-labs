import re
from itertools import zip_longest

from model import SequenceRes, Sequence


def test_output(expected_output_file, data: list) -> None:
    expected_result = sorted(extract_output(expected_output_file), key=lambda x: x.value)
    data = sorted(data, key=lambda x: x.value)
    assert len(expected_result) == len(data), f"{len(expected_result)} is not {len(data)}"

    for i in range(len(expected_result)):
        test_compare(expected_result[i], data[i])

    print("Test successful")


def test_compare(first: SequenceRes, second: SequenceRes):
    assert first.value == second.value
    assert (first.first_seq == second.first_seq and first.second_seq == second.second_seq) \
           or (first.second_seq == second.first_seq and first.first_seq == second.second_seq), \
        f" {first} is not {second}"


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
    assert len(head_args) == 3, f"Expected len 3, actual args => {head_args}"
    first_seq = Sequence(head_args[0], first_seq_line.strip())
    second_seq = Sequence(head_args[1], second_seq_line.strip())
    return SequenceRes(first_seq, second_seq, int(head_args[2]))
