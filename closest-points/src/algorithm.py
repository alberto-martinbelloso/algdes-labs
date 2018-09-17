import math

from src.parse import Point


def closest_point_full(points: list):
    x_sorted_points = sorted(points, key=lambda p: p.x)
    y_sorted_points = sorted(points, key=lambda p: p.y)
    return closest_point(x_sorted_points, y_sorted_points)


def closest_point(x_sorted: list, y_sorted: list) -> float:
    if len(x_sorted) <= 3:
        return find_min_distance(x_sorted)

    mid_x_pos = int(len(x_sorted) / 2)
    mid_x_val = x_sorted[mid_x_pos].x
    y_sorted_left, y_sorted_right = split_y_sorted_by_x(mid_x_val, y_sorted)

    closest_left = closest_point(x_sorted[:mid_x_pos], y_sorted_left)
    closest_right = closest_point(x_sorted[mid_x_pos:], y_sorted_right)

    smallest_distance = min(closest_left, closest_right)

    middle_belt_y_sorted = [p for p in y_sorted if abs(p.x - mid_x_val) <= smallest_distance]
    if len(middle_belt_y_sorted) < 2:
        return smallest_distance

    min_middle_belt_distance = smallest_middle_belt_distance(middle_belt_y_sorted)
    return min(smallest_distance, min_middle_belt_distance)


def split_y_sorted_by_x(mid_x_val: float, y_sorted: list):
    y_sorted_left = []
    y_sorted_right = []
    # check if this should be <= or <
    for point in y_sorted:
        if point.x <= mid_x_val:
            y_sorted_left.append(point)
        else:
            y_sorted_right.append(point)
    return y_sorted_left, y_sorted_right


def smallest_middle_belt_distance(middle_belt: list) -> float:
    length = len(middle_belt)
    assert length >= 2

    distances = [distance(middle_belt[i], middle_belt[j]) for i in range(length - 1) for j in
                 range(i, min(length, i + 7))]
    return min(distances)


def find_min_distance(points: list) -> float:
    length = len(points)
    assert length <= 3

    distances = [distance(points[i], points[j]) for i in range(length - 1) for j in
                 range(i, length)]
    return min(distances)


def distance(first: Point, second: Point) -> float:
    return math.sqrt(math.pow(first.x - second.x, 2) + math.pow(first.y - second.y, 2))
