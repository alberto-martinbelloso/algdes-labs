from decimal import Decimal

class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

# def parse(file):
#     start = False
#     points = []
#     with open(file) as f:
#         for line in f:
#             if(line.startswith("1") or line.startswith("0")):
#                 start = True
#             elif(line.startswith("EOF")):
#                 break
#             if(start):
#                 splittedLine = line.split(" ").
#                 points.append(Point(splittedLine[0], splittedLine[1], splittedLine[2]))
#     return points

# points = parse("./../data/a280-tsp.txt")
# for point in points:
#     print(point.id)