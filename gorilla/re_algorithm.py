from functools import reduce

memorizer = {}


def calc_vals(values: dict, first_seq: str, second_seq: str) -> (int, str, str):
    if len(first_seq) == 0 and len(second_seq) == 0:
        return 0, "", ""

    pair = (first_seq, second_seq)

    if pair in memorizer:
        return memorizer[pair]

    res_vals = []
    if len(second_seq) > 0:
        second_last = last(second_seq)
        prev_res = calc_vals(values, first_seq, second_seq[:-1])
        first_gap_value = (
            prev_res[0] + values['*'][second_last], prev_res[1] + "-", prev_res[2] + second_last
        )
        res_vals.append(first_gap_value)

    if len(first_seq) > 0:
        first_last = last(first_seq)
        prev_res = calc_vals(values, first_seq[:-1], second_seq)
        second_gap_value = (
            prev_res[0] + values[first_last]['*'], prev_res[1] + first_last, prev_res[2] + "-"
        )
        res_vals.append(second_gap_value)

    if len(first_seq) > 0 and len(second_seq) > 0:
        first_last = last(first_seq)
        second_last = last(second_seq)
        prev_res = calc_vals(values, first_seq[:-1], second_seq[:-1])
        match_value = (prev_res[0] + values[first_last][second_last], prev_res[1] + first_last,
                       prev_res[2] + second_last)
        res_vals.append(match_value)

    value = tuple_max(res_vals)

    memorizer[pair] = value
    return value


def tuple_max(tuples: list) -> (int, str, str):
    return reduce(lambda el, acc: el if el[0] > acc[0] else acc, tuples)


def last(li):
    return li[len(li) - 1]
