from src.parse import Point
import os

def output(fileName, length, distance, outputPath):
    with open(outputPath, "a+") as f:
        f.write(f"{fileName} {length} {distance}")

def delete_if_exists(outputPath):
    try:
        os.remove(outputPath)
    except OSError as e:
        if e.errno != OSError.errno.ENOENT:
            raise
