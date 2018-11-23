from sys import stdin

from alternate import alternate
from few import few
from input_parser import parse_input
from many import many
from model import Result
from none import none
from some import some


def format_tab_separated(*args) -> str:
    res = ""
    for num in args:
        res += f"{num}\t"
    res += "\n"
    return res


def format_bool_res(res: bool) -> str:
    return str(res).lower()


def format_many_res(res: int) -> str:
    if res == -2:
        return "?!"
    return str(res)


def format_some_res(res: Result) -> str:
    if res == 1:
        return "true"
    elif res == 2:
        return "false"
    else:
        return "?!"


input_data = stdin
graph = parse_input(input_data)
none_res = none(graph)
some_res = some(graph)
few_res = few(graph)
many_res = many(graph)
alternate_res = alternate(graph)

vertex_count = len(graph.vertex_list)
s_res = format_some_res(some_res)
a_res = format_bool_res(alternate_res)
m_res = format_many_res(many_res)
print(format_tab_separated(vertex_count, a_res, few_res, m_res, none_res, s_res))
# print(f"None => {none_res}")
# print(f"Some => {some_res}")
# print(f"Few => {few_res}")
# print(f"Many => {many_res}")
# print(f"Alternate => {alternate_res}")
