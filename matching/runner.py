import os
from os.path import join

import data_extractor
from alghorithm import gale_shapely


def run_test(input_path, expected_output_path):
    test_name = input_path[:-7]
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

    data_matches = expected_output_data == actual_output_data
    print(f"Test successful =>  {data_matches}")


def run_all_tests():
    directory = os.getcwd()
    data_directory = join(directory, "data")

    in_out_paths = data_extractor.get_in_out_paths_in_directory(data_directory)

    for file_entry in in_out_paths:
        run_test(file_entry.get_full_input_path(), file_entry.get_full_output_path())


run_all_tests()
