from data_extractor import OutputData, InputData
import time


def gale_shapely(input_data: InputData):
    current_matchings = {}
    males = input_data.male
    females = input_data.female

    start = round((time.time() * 1000), 2)
    average = 0
    counter = 0

    while len(current_matchings) != len(females):
        male_keys = list(males.keys())
        for male_key in male_keys:
            male_preferences = males[male_key]
            if male_key not in current_matchings.values():
                female_to_propose_to = male_preferences.pop(0)
                female_preferences = females[female_to_propose_to]
                if female_to_propose_to not in current_matchings:
                    current_matchings[female_to_propose_to] = male_key
                elif female_preferences.index(male_key) < female_preferences.index(
                        current_matchings[female_to_propose_to]):
                    current_matchings[female_to_propose_to] = male_key
                average += (round((time.time() * 1000), 2) - start)
                counter += 1
            if len(male_preferences) == 0:
                del males[male_key]

    average = round(average / counter, 2)
    end = round((time.time() * 1000) - start, 2)

    print('INFO => Total algorithm time is {} '.format(end))
    print('INFO => Average time to find a match is {} for {} matches. '.format(average, len(current_matchings)))
    return ids_to_names_mapping(current_matchings, input_data)


def ids_to_names_mapping(curent_matchings, input_data):
    new_mapped_matchings = OutputData()
    for key, value in curent_matchings.items():
        mapped_key = input_data.names_map[key]
        mapped_value = input_data.names_map[value]
        new_mapped_matchings.male_to_female_matchings.append((mapped_value, mapped_key))

    return new_mapped_matchings
