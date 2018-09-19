import os
import errno
from os.path import join

import data_extractor
from alghorithm import gale_shapely


def run_test(input_path, expected_output_path):
    #test_name = input_path[:-7]
    test_name = input_path.rsplit('\\', 1)[-1]
    print("")
    print("")
    print(f"Running test    =>  {test_name}")
    print(f"Input path      =>  {input_path}")
    print(f"Output path     =>  {expected_output_path}")
    input_data = data_extractor.read_input_data_from_file(input_path)
    expected_output_data = data_extractor.read_output_data_from_file(expected_output_path)
    actual_output_data = gale_shapely(input_data)

    print(f"Expected data   =>  {expected_output_data}")
    print(f"Executed data   =>  {actual_output_data}")
    print(f"Expected length =>  {len(expected_output_data.male_to_female_matchings)}")
    print(f"Executed length =>  {len(actual_output_data.male_to_female_matchings)}")
    print("")

    executed_output_file_path = test_name.rsplit('-', 1)[0] + "-out.txt"

    #delete_if_exists("./out/" + executed_output_file_path)
    delete_if_exists(executed_output_file_path)

    for p in actual_output_data.male_to_female_matchings:
        output(p[0], p[1], executed_output_file_path)
        #output(p[0], p[1], "./out/" + executed_output_file_path)

    data_matches = expected_output_data == actual_output_data
    print(f"Test successful =>  {data_matches}")


def run_all_tests():
    directory = os.getcwd()
    data_directory = join(directory, "data")

    #create_output_directory_if_not_exist("./out")

    in_out_paths = data_extractor.get_in_out_paths_in_directory(data_directory)

    for file_entry in in_out_paths:
        run_test(file_entry.get_full_input_path(), file_entry.get_full_output_path())


def output(entry_1, entry_2, output_path):
    with open(output_path, "a+") as f:
        f.write(f"{entry_1} -- {entry_2}\n")


def delete_if_exists(output_path):
    try:
        os.remove(output_path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


def create_output_directory_if_not_exist(output_forlder_path):
    try:
        os.mkdir(output_forlder_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


run_all_tests()
