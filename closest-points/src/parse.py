import os


class Point:
    id: str
    x: float
    y: float

    def __init__(self, id, x, y):
        self.id = id
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"({self.id}, {self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"({self.id}, {self.x}, {self.y})"


def test_out_file(points_length, file_name, out_test_file="../data/closest-pair-out.txt"):
    with open(out_test_file) as f:
        for line in f:
            if file_name.split("/")[-1].split("-")[0] in line:
                length = line.split(" ")[1]
                if float(length) != float(points_length):
                    raise Exception(
                        f"length of the parsed points is different from the output file \n file "
                        f"name: {file_name} \n was: {points_length} \n should be: {length}")


def parse(file_name):
    points = []
    with open(file_name) as f:
        for line in f:
            splitted_line = line.split(None)
            length = len(splitted_line)

            if length < 3 or length > 3:
                continue
            elif line.startswith("EOF") or line == "\n":
                break
            else:
                try:
                    point = Point(splitted_line[0], splitted_line[1], splitted_line[2])
                    points.append(point)
                except ValueError:
                    #print(f"Non-numeric data found in the file => {file_name}")
                    pass

    test_out_file(len(points), file_name)

    return points


def parse_all(folder) -> list:
    result = []

    for file in sorted(os.listdir(folder)):
        if file.endswith(".txt") and file not in ["closest-pair-out.txt", "result-out.txt"]:
            result.append((file, parse(f"{folder}{file}")))

    return result
