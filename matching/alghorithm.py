from copy import copy

from data_extractor import OutputData, InputData


def gale_shapely(input_data: InputData):
    current_matchings = {}
    males = input_data.male
    females = input_data.female

    print(f"Males => {[m for m in males]}")
    print(f"Females => {[f for f in females]}")
    print(f"Males len => {len(males)}")
    print(f"Females len => {len(females)}")

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
            if len(male_preferences) == 0:
                del males[male_key]

    return dictionary_matchings_to_output_data(current_matchings)


def dictionary_matchings_to_output_data(dictionary_matchings):
    output_data = OutputData()
    for female in dictionary_matchings:
        male = dictionary_matchings[female]
        output_data.male_to_female_matchings.append((male, female))
    return output_data
