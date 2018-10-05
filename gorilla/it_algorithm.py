def generate_matrix(first_dim: int, second_dim: int, init_fun) -> list:
    res = []
    for i in range(first_dim):
        res.append([])
        for j in range(second_dim):
            res[i].append(init_fun(i, j))

    return res


def init_matrix(x: int, y: int) -> int:
    if x > 0 and y == 0:
        return x * -4
    elif x == 0 and y > 0:
        return y * -4
    else:
        return 0


def create_string_matrix_init_fun(first_seq: str, second_seq: str):
    def init_string_matrix(x: int, y: int) -> (str, str):
        if x > 0 and y == 0:
            return first_seq[:x], x * '-'
        elif x == 0 and y > 0:
            return y * '-', second_seq[:y]
        return '', ''

    return init_string_matrix


def calc_vals(values: dict, first_seq: str, second_seq: str) -> (int, str, str):
    x_len = len(first_seq) + 1
    y_len = len(second_seq) + 1
    matrix = generate_matrix(x_len, y_len, init_matrix)

    str_matrix = generate_matrix(x_len, y_len, create_string_matrix_init_fun(first_seq, second_seq))

    for i in range(1, x_len):
        for j in range(1, y_len):
            first_char = first_seq[i - 1]
            second_char = second_seq[j - 1]

            match_value = matrix[i - 1][j - 1] + values[first_char][second_char]
            first_gap_value = matrix[i][j - 1] + values['*'][second_char]
            second_gap_value = matrix[i - 1][j] + values[first_char]['*']

            max_val = max(match_value, first_gap_value, second_gap_value)
            matrix[i][j] = max_val

            if max_val == match_value:
                str_matrix[i][j] = (
                    str_matrix[i - 1][j - 1][0] + first_char,
                    str_matrix[i - 1][j - 1][1] + second_char)
            elif max_val == first_gap_value:
                str_matrix[i][j] = \
                    (str_matrix[i][j - 1][0] + "-",
                     str_matrix[i][j - 1][1] + second_char)
            else:
                str_matrix[i][j] = (
                    str_matrix[i - 1][j][0] + first_char, str_matrix[i - 1][j][1] + "-")

    res_strings = str_matrix[x_len - 1][y_len - 1]
    return matrix[x_len - 1][y_len - 1], res_strings[0], res_strings[1]
