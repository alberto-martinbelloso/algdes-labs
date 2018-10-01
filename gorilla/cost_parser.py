def parse_cost_file(file_name: str) -> dict:
    main_dict = {}
    try:
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
    except FileNotFoundError:
        print("Cost file not found")

    return main_dict


