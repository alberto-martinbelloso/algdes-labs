from parse import Point

def output(points, outputPath):
    with open(outputPath, "w") as f:
        for point in points:
            f.write(point.__str__())
            f.write("\n")