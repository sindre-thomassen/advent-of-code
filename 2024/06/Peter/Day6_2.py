#!/usr/bin/python3
from typing import Tuple, Set, List


from Day6_1 import get_input, print_map, parse_data, move_guard, get_guard_symbol, turn_guard, OutOfRoomError


def register_guard_status(guard_positions, guard)-> None:
    guard_positions.add(guard)

def check_possible_loop(room_map, guard_positions, guard: Tuple[int,int,int,int]) -> Tuple[bool, Tuple[int, int] or None]:
    x, y, dx, dy = guard
    before = len(guard_positions)
    #first check to see if it is possible to place a block infront of current guard position and direction
    if not (0 <= y + dy < len(room_map) and 0 <= x + dx < len(room_map[y])):
        return False, None
    # already an object infront of guard
    if room_map[y + dy][x + dx] == "#":
        return False, None
    # already been in this position, so could be no block there from beginning
    if room_map[y + dy][x + dx] == "X":
        return False, None
    room_map[y + dy][x + dx] = "#" # place block infront of guard

    guard = move_guard(room_map, guard)

    # will moving the guard send him into a location and direction he has previously been in?
    while not guard in guard_positions:
        register_guard_status(guard_positions, guard)
        try:
            guard = move_guard(room_map, guard, "*")
        except OutOfRoomError:
            return False, None
    room_map[y + dy][x + dx] = "O"
    #print_map(room_map)
    after = len(guard_positions)
    #print(f"Before: {before}, After: {after}, Guardmoves: {after-before}")
    return True, (x+dx, y+dy)

if __name__ == "__main__":
    input_data = get_input("./input.txt")

    room_map, guard = parse_data(input_data)
    guard_start_x, guard_start_y, guard_start_dx, guard_start_dy = guard
    original_map = [row.copy() for row in room_map]
    guard_positions: Set[Tuple[int, int, int, int]] = set()
    result_set = set()
    try:
        while True:
            #print("\n#", end=" ")
            register_guard_status(guard_positions, guard)

            map_copy = [row.copy() for row in room_map]
            guard_positions_copy = guard_positions.copy()

            possible_loop, loop_position = check_possible_loop(map_copy, guard_positions_copy, guard)
            if possible_loop:
                loop_x, loop_y = loop_position
                #print(f"Loop detected at {loop_x},{loop_y}")
                if loop_x == guard_start_x and loop_y == guard_start_y:
                    print("Loop is at start position")
                else:
                    result_set.add(loop_position)
            guard = move_guard(room_map, guard)
    except OutOfRoomError:
        pass

    for position in result_set:
        original_map[position[1]][position[0]] = "O"
    print_map(original_map)
    print(len(result_set))
    # gives wrong answer on real input, dunno why