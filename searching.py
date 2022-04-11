import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r') as json_file:
        json_object = json.load(json_file)
    if isinstance(json_object, dict) and field in json_object:
        return json_object[field]


def linear_search(haystack, needle):
    needle_occurrence = {
        'positions': [],
        'count': 0
    }

    for i in range(len(haystack)):
        if haystack[i] == needle:
            needle_occurrence['positions'].append(i)
            needle_occurrence['count'] += 1

    return needle_occurrence


def pattern_search(sequence, pattern):
    pattern_occurrence = set()

    # Special variant
    for i in range(len(sequence) - len(pattern) + 1):
        for pattern_i in range(len(pattern)):
            if sequence[i + pattern_i] != pattern[pattern_i]:
                break
            if pattern_i == len(pattern) - 1:
                pattern_occurrence.add(i)
        # Normal variant
        #  if sequence[i: i + len(pattern)] == pattern:
        #      pattern_occurrence.add(i)

    return pattern_occurrence


def binary_search(sorted_list, founded):
    left = 0
    right = len(sorted_list) - 1
    pivot = len(sorted_list) // 2

    while left <= right:
        pivot = (left + right) // 2
        if founded == sorted_list[pivot]:
            return pivot
        elif founded > sorted_list[pivot]:
            left = pivot + 1
        else:
            right = pivot


def main():
    json_file_name = 'sequential.json'

    unordered_numbers = read_data(json_file_name, 'unordered_numbers')
    number_occurrence = linear_search(unordered_numbers, -5)
    print(f'List of unordered numbers: {unordered_numbers}\n'
          f'Number {-5} is {number_occurrence["count"]} times in list at positions {number_occurrence["positions"]}')

    dna_sequence = read_data(json_file_name, 'dna_sequence')
    gcg_occurrence = pattern_search(dna_sequence, 'GCG')
    print(f'DNA sequence: {dna_sequence},\n'
          f'Pattern {"GCG"} is in DNA sequence at positions {gcg_occurrence}')

    sorted_numbers = read_data(json_file_name, 'ordered_numbers')
    num_index = binary_search(sorted_numbers, -51)
    print(f'List of sorted numbers: {sorted_numbers}\n'
          f'Founded number {-51} is in index {num_index}')


if __name__ == '__main__':
    main()
