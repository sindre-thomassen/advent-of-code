from tqdm import tqdm

# Stone that change when you blink
def part_1(stones, n):
    """
    From the initial list of stones, calculate the number of stones after n number of blinks
    :param stones:
    :param n:
    :return: number of stones after n number of blinks
    """

    # We want the total number of stones at the end, process each individual stone to save memory when n is large
    total = 0
    for stone in tqdm(stones):
        total += _blink(stone, n)

    return total


# Recursive method to calculate the total number of stones after n number of blinks
def _blink(stone, max_blinks, current_blink=0):
    """
    Recursive method to calculate the total number of stones after n number of blinks
    :param stone:
    :param max_blinks:
    :param current_blink:
    :return:
    """
    if current_blink == max_blinks:
        return 1

    new_stones = _transform(stone)
    n = 0
    for new_stone in new_stones:
        n += _blink(new_stone, max_blinks, current_blink + 1)

    return n


def _transform(stone):
    if stone == 0:
        return [1]

    # Split stone into two parts on the middle
    if len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        return [int(str(stone)[:half]), int(str(stone)[half:])]
    else:
        return [stone * 2024]


if __name__=="__main__":
    with open("input.txt", "r") as file:
        stones = list(map(int, file.readline().split()))

    print(part_1(stones, 25))
    print(part_1(stones, 75))