import sys
from sys import stdin

from alternate import alternate
from few import few
from input_parser import parse_input
from many import many
from model import Result
from none import none
from output_creator import output
from some import some


def prepare_filename(filename: str) -> str:
    return filename.replace("./data/", "").replace(".txt", "")

def format_tab_separated(*args) -> str:
    res = ""
    for num in args:
        res += f"{num}\t"
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

if len(sys.argv) > 1:
    filename = prepare_filename(sys.argv[1])
    out = format_tab_separated(filename, vertex_count, a_res, few_res, m_res, none_res, s_res)
else:
    out = format_tab_separated(vertex_count, a_res, few_res, m_res, none_res, s_res)
print(out)


output("./results.txt", out + "\n")
