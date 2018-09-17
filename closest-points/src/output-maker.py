from parse import Point

def output(fileName, length, distance, outputPath):
    with open(outputPath, "w") as f:
        f.write(f"{fileName} {length} {distance}")