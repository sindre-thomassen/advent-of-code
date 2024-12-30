import re
from tqdm import tqdm

def run(pattern, strings):
    n_valid = 0

    for string in tqdm(strings):
        if re.fullmatch(pattern, string):
            n_valid += 1

    return n_valid

def build_pattern(segments):
    # units = [x for x in segments if len(x) == 1]
    # sub_pattern = "(" + "|".join(units) + ")*"

    # Remove all segments consisting of only one character segments

    pattern = "("

    # The final string should be any combinations of the segments
    for segment in segments:
        # if re.fullmatch(sub_pattern, segment) and len(segment) > 1:
        #     continue

        pattern += segment + "|"

    # Remove the last "|"
    pattern = pattern[:-1]

    pattern += ")*"
    return pattern

def optimize_pattern(segments):
    min_size, max_size = min(len(x) for x in segments), max(len(x) for x in segments)

    unit_segments = [x for x in segments if len(x) == min_size]
    _segments = [segment for segment in segments if len(segment) != min_size]

    # Find all segments which are not a multiple of the smallest segment
    for i in range(min_size + 1, max_size + 1):
        sub_pattern = build_pattern(unit_segments)
        remaining_segments = []

        for segment in _segments:
            if len(segment) == i and not re.fullmatch(sub_pattern, segment): # Can't be built without additional segments. Add unit
                unit_segments.append(segment)

            elif len(segment) > i and not re.fullmatch(sub_pattern, segment):
                # Can't be built without additional segments. Look at again with additional unit segments
                remaining_segments.append(segment)

        _segments = remaining_segments

    return build_pattern(unit_segments)

if __name__=="__main__":
    with open("input.txt", "r") as file:
        segments = file.readline().strip().split(", ")
        pattern = optimize_pattern(segments)

        file.readline()
        strings = file.read().splitlines()

    print(run(pattern, strings))