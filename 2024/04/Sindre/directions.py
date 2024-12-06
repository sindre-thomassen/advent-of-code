# Check if three next letters horizontally spells MAS
def check_horizontally(INPUT, x, y):
    left, right = True, True

    for i, c in enumerate(["M", "A", "S"]):
        # Check to the right
        if (x+(i+1) >= len(INPUT[0]) or INPUT[y][x+(i+1)] != c) and right:
            right = False

        # Check to the left
        if (x - (i+1) < 0 or INPUT[y][x-(i+1)] != c) and left:
            left = False

        if not left and not right:
            return 0

    return int(left) + int(right)


# Check it three next letters vertically spells MAS
def check_vertically(INPUT, x, y):
    up, down = True, True

    for i, c in enumerate(["M", "A", "S"]):
        # Check down
        if (y+(i+1) >= len(INPUT) or INPUT[y+(i+1)][x] != c) and down:
            down = False

        # Check up
        if (y - (i+1) < 0 or INPUT[y-(i+1)][x] != c) and up:
            up = False

        if not up and not down:
            return 0

    return int(up) + int(down)


# Check if three next letters diagonally spells MAS
def check_diagonally(INPUT, x, y):
    nw, ne, sw, se = True, True, True, True
    LETTERS = ["M", "A", "S"]

    for i in range(3):
        # Check nw
        if (x - (i+1) < 0 or y - (i+1) < 0 or INPUT[y-(i+1)][x-(i+1)] != LETTERS[i]) and nw:
            nw = False

        # Check ne
        if (x+(i+1) >= len(INPUT[0]) or y - (i+1) < 0 or INPUT[y-(i+1)][x+(i+1)] != LETTERS[i]) and ne:
            ne = False

        # Check sw
        if (x - (i+1) < 0 or y+(i+1) >= len(INPUT) or INPUT[y+(i+1)][x-(i+1)] != LETTERS[i]) and sw:
            sw = False

        # Check se
        if (x+(i+1) >= len(INPUT[0]) or y+(i+1) >= len(INPUT) or INPUT[y+(i+1)][x+(i+1)] != LETTERS[i]) and se:
            se = False

        if not any([nw, ne, sw, se]):
            return 0

    return int(nw) + int(ne) + int(sw) + int(se)

def check_cross(INPUT, x, y):
    if x == 0 or y == 0 or x == len(INPUT[0])-1 or y == len(INPUT)-1:
        return False

    se = INPUT[y-1][x-1] == "M" and INPUT[y+1][x+1] == "S"
    sw = INPUT[y-1][x+1] == "M" and INPUT[y+1][x-1] == "S"
    ne = INPUT[y+1][x-1] == "M" and INPUT[y-1][x+1] == "S"
    nw = INPUT[y+1][x+1] == "M" and INPUT[y-1][x-1] == "S"

    return ((se or nw) and (sw or ne))
