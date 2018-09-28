from sys import stdin
from parse import parse_lines
from algorithm import closest_point_full


data = stdin

results = parse_lines(data)

lowest_distance = closest_point_full(results)
print(len(results), lowest_distance.distance)

