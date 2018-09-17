
class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return f"{self.id} {self.x} {self.y}"

def parse(file):
    points = []
    with open(file) as f:
        for line in f:
            splittedLine = list(filter(None, line.split(" ")))
            length = len(splittedLine)

            if(length < 3 or length > 3):
                continue
            elif(line.startswith("EOF")):
                break
            else:
                try:
                    point = Point(splittedLine[0], splittedLine[1], splittedLine[2])
                    points.append(point)
                except ValueError:
                    print('Non-numeric data found in the file.')
    return points