import os


def parse_file(file_name):
    main_dict = {}
    with open(file_name) as file:
        scores = []
        split = []

        for line in file:
            if line.startswith('#'):
                continue
            if line.startswith(' '):
                split = line.split(None)
                continue
            scores.append(line.split(None))

            i = 1
        for char in split:
            inner_dict = {}
            for score in scores:
                inner_dict[score[0]] = score[i]
            main_dict[char] = inner_dict
            i = i + 1
    return main_dict


results = parse_file("../data/BLOSUM62.txt")
# print(results['A']['A'])  # 4
# print(results['A']['F'])  # -2
# print(results['R']['R'])  # 5

for k in results:
    line = [f"{j}: {results[k][j]}" for j in results[k]]
    print(f"{k} => {line}")
