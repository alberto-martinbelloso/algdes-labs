
import os

class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return f"{self.id} {self.x} {self.y}"

def testOutFile(pointsLength, fileName, outTestFile = "../data/closest-pair-out.txt"):
    with open(outTestFile) as f:
        for line in f:
            if(fileName.split("/")[-1].split("-")[0] in line):
                length = line.split(" ")[1]
                if(float(length) != float(pointsLength)):
                    raise Exception(f"length of the parsed points is different from the output file \n file name: {fileName} \n was: {pointsLength} \n should be: {length}")

def parse(file):
    points = []
    with open(file) as f:
        for line in f:
            splittedLine = line.split(None)
            length = len(splittedLine)

            if(length < 3 or length > 3):
                continue
            elif(line.startswith("EOF") or line == "\n"):
                break
            else:
                try:
                    point = Point(splittedLine[0], splittedLine[1], splittedLine[2])
                    points.append(point)
                except ValueError:
                    print('Non-numeric data found in the file.')
    
    testOutFile(len(points), file)

    return points

def parseAll(folder):
    result = []

    for file in os.listdir(folder):
        if (file.endswith(".txt") and file not in "closest-pair-out.txt"):
            result.append((file, parse(f"{folder}{file}")))
    
    return result
