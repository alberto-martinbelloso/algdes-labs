import os
import re
from os.path import isfile, join


def read_input_file_into_entries(path):
    ids = []
    names = {} #implemented as name to id mapper
    entries = {}
    with open(path, mode='r') as file:
        for line in file:
            if line.startswith("#"):
                pass
            elif re.match(r"^\d+ .+$", line):
                id = line.split(" ")[0]
                name = line.split(" ")[1][:-1]
                ids.append(id)
                names[id] = name #implemented as name to id mapper
                entries[id] = []
            elif re.match("^\d+:(?: \d+)+.+$", line):
                position = int(line.split(":")[0]) - 1
                preferences = entries[ids[position]]
                references = line[:-1].split(" ")
                for ref in references[1:]:
                    if re.match(r"\d+", ref):
                        ref_position = int(ref) - 1
                        preferences.append(ids[ref_position])
            else:
                print("WARNING => Non readable line.")

    males = {}
    females = {}
    male_count = 0
    female_count = 0
    for i in range(len(ids)):
        id = ids[i]
        if i % 2 == 0:
            male_count += 1
            males[id] = entries[id]
        else:
            female_count += 1
            females[id] = entries[id]

    input_data = InputData()
    input_data.female = females
    input_data.male = males
    input_data.names_map = names
    return input_data


def read_output_data_from_file(path):
    output_data = OutputData()
    with open(path, mode='r') as file:
        for line in file:
            if re.match(r"^.+ -- .+", line):
                fields = line.split(" ")
                male = fields[0]
                female = fields[2][:-1]
                output_data.male_to_female_matchings.append((male, female))
    return output_data


def read_input_data_from_file(path):
    return read_input_file_into_entries(path)


def get_in_out_paths_in_directory(dir_path):
    files = [f for f in os.listdir(dir_path) if (isfile(join(dir_path, f)) and f.endswith(".txt"))]
    in_files = [f for f in files if f.endswith("-in.txt")]
    out_files = [f for f in files if f.endswith("-out.txt")]

    entries = []
    for in_file in in_files:
        shared_name = in_file[:-7]
        matching_out_file = next(f for f in out_files if re.fullmatch(shared_name+"-out.txt", f) is not None)
        entries.append(FileEntry(dir_path, in_file, matching_out_file))

    return entries


class InputData:
    names_map: dict
    male: dict
    female: dict

    def __init__(self) -> None:
        super().__init__()
        self.male = {}
        self.female = {}


class OutputData:
    male_to_female_matchings: list

    def __init__(self) -> None:
        super().__init__()
        self.male_to_female_matchings = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, OutputData):
            return False

        return set(self.male_to_female_matchings) == set(o.male_to_female_matchings)

    def __str__(self) -> str:
        return f"OutputData, male to female => {self.male_to_female_matchings}"

    def __repr__(self) -> str:
        return f"OutputData, male to female => {self.male_to_female_matchings}"


class FileEntry:
    _directory: str
    _input_path: str
    _output_path: str

    def __init__(self, directory, input, output) -> None:
        super().__init__()
        self._input_path = input
        self._output_path = output
        self._directory = directory

    def __str__(self) -> str:
        return f"FileEntry => input_path: {self._input_path}, output_path: {self._output_path}"

    def __repr__(self) -> str:
        return f"FileEntry => input_path: {self._input_path}, output_path: {self._output_path}"

    def get_full_input_path(self):
        return os.path.join(self._directory, self._input_path)

    def get_full_output_path(self):
        return os.path.join(self._directory, self._output_path)








