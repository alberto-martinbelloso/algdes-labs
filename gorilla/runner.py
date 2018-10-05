import time
from sys import stdin

from cost_parser import parse_cost_file
from input_parser import extract_input_data
#iterative version
from it_algorithm import calc_vals
#uncomment for recursive version
#from re_algorithm import calc_vals
from model import SequenceRes, Sequence


def process_file(input_file, values: dict):
    input_data = extract_input_data(input_file)
    results = calculate_all_with_all(input_data, values)

    for res in results:
        print(format_output(res))


def calculate_all_with_all(inputs: list, values: dict):
    length = len(inputs)
    start_time = time.time()
    outputs = [calculate_single(inputs[i], inputs[j], values) for i in range(length - 1)
               for j in range(i + 1, length)]

    print(f"All took => {time.time() - start_time}")

    return outputs


def calculate_single(first_input: Sequence, second_input: Sequence, values: dict) -> SequenceRes:
    result = calc_vals(values, first_input.seq, second_input.seq)
    first_res_seq = Sequence(first_input.name, result[1])
    second_res_seq = Sequence(second_input.name, result[2])
    return SequenceRes(first_res_seq, second_res_seq, result[0])


def format_output(output: SequenceRes) -> str:
    return f"{output.first_seq.name}--{output.second_seq.name}: {output.value}\n" \
           f"{output.first_seq.seq}\n" \
           f"{output.second_seq.seq}"


in_data = stdin

vals = parse_cost_file("BLOSUM62.txt")

process_file(in_data, vals)

#If you wish to run the recursive version of the algo uncomment the import statement at the top