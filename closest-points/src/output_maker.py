import errno

from src.parse import Point
import os

def output(file_name, length, distance, output_path, input_folder):
    with open(output_path, "a+") as f:
        f.write(f"{input_folder}{file_name}: {length} {distance}\n")

def delete_if_exists(output_path):
    try:
        os.remove(output_path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
