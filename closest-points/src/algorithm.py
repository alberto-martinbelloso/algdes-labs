import math

from src.parse import Point, Distance


def closest_point_full(points: list) -> Distance:
    x_sorted_points = sorted(points, key=lambda p: p.x)
    y_sorted_points = sorted(points, key=lambda p: p.y)
    return closest_point(x_sorted_points, y_sorted_points)


def closest_point(x_sorted: list, y_sorted: list) -> Distance:
    if len(x_sorted) <= 3:
        return find_min_distance(x_sorted)

    mid_x_pos = int(len(x_sorted) / 2)
    mid_x_val = x_sorted[mid_x_pos].x
    y_sorted_left, y_sorted_right = split_y_sorted_by_x(mid_x_val, y_sorted)

    closest_left = closest_point(x_sorted[:mid_x_pos], y_sorted_left)
    closest_right = closest_point(x_sorted[mid_x_pos:], y_sorted_right)

    smallest_distance = min_dist([closest_left, closest_right])

    middle_belt_y_sorted = [p for p in y_sorted if abs(p.x - mid_x_val) <= smallest_distance.distance]
    if len(middle_belt_y_sorted) < 2:
        return smallest_distance

    min_middle_belt_distance = smallest_middle_belt_distance(middle_belt_y_sorted)
    return min_dist([smallest_distance, min_middle_belt_distance])


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


def smallest_middle_belt_distance(middle_belt: list) -> Distance:
    length = len(middle_belt)
    assert length >= 2

    distances = [distance(middle_belt[i], middle_belt[j]) for i in range(length - 1) for j in
                 range(i + 1, min(length, i + 7))]
    smallest_belt_distance = min_dist(distances)
    return smallest_belt_distance


def find_min_distance(points: list) -> Distance:
    length = len(points)
    assert length <= 3
    distances = [distance(points[i], points[j]) for i in range(length - 1) for j in
                 range(i + 1, length)]
    min_distance = min_dist(distances)

    return min_distance

def min_dist(distances: list) -> Distance:
    num_distances = [d.distance for d in distances]
    min_distance = min(num_distances)
    return distances[num_distances.index(min_distance)]


def distance(first: Point, second: Point) -> Distance:
    dist = math.sqrt(math.pow(first.x - second.x, 2) + math.pow(first.y - second.y, 2))
    #print(f"First => {first} Second => {second}")
    #print(f"Calculate distance => {dist}")
    return Distance(first, second, dist)
