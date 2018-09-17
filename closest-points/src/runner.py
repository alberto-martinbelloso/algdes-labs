from src.parse import *
from src.algorithm import closest_point_full
from src.output_maker import *

# file_name = "/Users/Arin/PyCharm Projects/AlgDes/closest-points/data/berlin52-tsp.txt"
folder_path = "../data/"
result_path = "../data/closest-pair-out.txt"
output_path = "../data/result-out.txt"
delete_if_exists(output_path)

results = parse_all(folder_path)
for res in results:
    lowest_distance = closest_point_full(res[1])
    output(res[0], len(res[1]), lowest_distance, output_path, folder_path)


print("Execution finished")


expected_points = parse(result_path)
actual_points = parse(output_path)


actual_point_dict = {p.id.replace(".txt", "").replace("-tsp", ".tsp"): p.y for p in actual_points}

assert len(actual_point_dict) >= len(expected_points)
for point in expected_points:
    assert abs(actual_point_dict[point.id] - point.y) < 0.0001, f"{actual_point_dict[point.id]} was not {point.y}"


print("Man. You gut!")
