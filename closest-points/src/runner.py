from src.parse import parse
from src.algorithm import closest_point_full

file_name = "/Users/Arin/PyCharm Projects/AlgDes/closest-points/data/berlin52-tsp.txt"

points = parse(file_name)
lowest_distance = closest_point_full(points)
print(f"Lowest distance => {lowest_distance}")
