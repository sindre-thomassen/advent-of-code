#!/usr/bin/python3
from typing import List, Tuple

class OutOfRoomError(Exception):
    pass

def get_input(filename:str) -> List[str]:
    with open(filename) as file:
        lines = file.read().splitlines()
        return lines

def find_starting_guard(room_map: List[List[str]]) -> Tuple[int,int,int,int]:
    for y in range(len(room_map)):
        for x in range(len(room_map[y])):
            char = room_map[y][x]
            if char == "^":
                return x, y, 0, -1
            if char == ">":
                return x, y, 1, 0
            if char == "v":
                return x, y, 0, 1
            if char == "<":
                return x, y, -1, 0
    return -1, -1, 0, 0

def get_guard_symbol(dx, dy) -> str:
    if dx == 0 and dy == -1:
        return "^"
    if dx == 1 and dy == 0:
        return ">"
    if dx == 0 and dy == 1:
        return "v"
    if dx == -1 and dy == 0:
        return "<"
    return "?"

def turn_guard(guard: Tuple[int,int,int,int]) -> Tuple[int,int,int,int]:
    x, y, dx, dy = guard
    if dx == 0 and dy == -1:
        return x, y, 1, 0
    if dx == 1 and dy == 0:
        return x, y, 0, 1
    if dx == 0 and dy == 1:
        return x, y, -1, 0
    if dx == -1 and dy == 0:
        return x, y, 0, -1
    return x, y, dx, dy

def move_guard(room_map: List[List[str]], guard: Tuple[int,int,int,int], has_moved: str = 'X') -> Tuple[int,int,int,int]:
    x, y, dx, dy = guard
    try:
        if room_map[y+dy][x+dx] == "#":
            turned_guard = turn_guard(guard)
            x, y, dx, dy = turned_guard
            room_map[y][x] = get_guard_symbol(dx, dy)
            return turned_guard
        room_map[y][x] = has_moved
        room_map[y+dy][x+dx] = get_guard_symbol(dx, dy)
        return x+dx,y+dy, dx, dy
    except IndexError:
        room_map[y][x] = has_moved
        raise OutOfRoomError("Guard moved out of room")

def parse_data(data: List[str]) -> Tuple[List[List[str]], Tuple[int,int,int,int]]:
    room_map = list()
    for y,line in enumerate(data):
        row = list()
        for x,c in enumerate(line):
            row.append(c)
        room_map.append(row)

    guard = find_starting_guard(room_map)
    return room_map, guard

def print_map(room_map: List[List[str]]):
    for row in room_map:
        print("".join(row))
    print()

if __name__ == "__main__":
    input_data = get_input("./input.txt")
    room_map, guard = parse_data(input_data)
    print_map(room_map)

    try:
        while True:
            guard = move_guard(room_map, guard)
            # print_map(room_map)
    except OutOfRoomError:
        pass

    print_map(room_map)

    result = sum([row.count("X") for row in room_map])
    print(result)