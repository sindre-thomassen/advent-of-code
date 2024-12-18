import numpy as np

def part_1(INPUT):
    files = INPUT[::2]
    total_files = sum(files)
    empties = INPUT[1::2]

    space = [0] * files.pop(0)

    for i in range(len(files)):
        space += ['.'] * empties[i]
        space += [f'{i+1}'] * files[i]

    final_space = space[:total_files]
    extras = [x for x in space[total_files:] if x != '.']

    indices = [i for i, x in enumerate(final_space) if x == '.']

    for index in indices:
        final_space[index] = extras.pop()

    return sum([(i) * int(x) for i, x in enumerate(final_space)])

def part_2(INPUT):
    files = INPUT[::2]
    total_files = sum(files)
    empties = INPUT[1::2]

    # Save file system in format (filename, size)
    space = [(0, files.pop(0))]

    # Setup files system, alternating between empty space and files
    for i in range(len(files)):
        space += [(-1, empties[i]), (i+1, files[i])]

    unique_files = [file for file in space[::-1] if file[0] != -1]

    # Attempt to move rightmost file to the leftmost empty space
    for file in unique_files:
        file_index = space.index(file)

        # Try to find leftmost biggest empty space that can fit file
        for i in range(file_index):
            if space[i][0] == -1 and space[i][1] >= file[1]:
                empty_space = space[i]

                # Move file
                # Change file to empty space
                space[file_index] = (-1, file[1])

                if empty_space[1] > file[1]:
                    # Split empty space
                    space.insert(i, (file[0], file[1]))
                    space[i+1] = (-1, empty_space[1] - file[1])
                else:
                    space[i] = (file[0], file[1])

                break

    final_space = []
    for file in space:
        final_space += ['.'] * file[1] if file[0] == -1 else [f'{file[0]}'] * file[1]

    return sum([int(x) * i for i, x in enumerate(final_space) if x != '.'])

if __name__=="__main__":
    with open("input.txt", "r") as file:
        INPUT = [int(x) for x in file.read().strip()]

    print(part_1(INPUT))
    print(part_2(INPUT))



# 5220179521: Too low