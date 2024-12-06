import copy
#part 1
def main():
    f = open("day6\input.txt")
    map = []
    for row in f:
        row = list(row)
        row.remove("\n")
        map.append(row)
    f.close()

    position = find_guard(map)
    row = position[0]
    col = position[1]
    while True:
        match map[row][col]:
            case "^":
                if row == 0:
                    break
                move_to = map[row - 1][col]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    map[row][col] = "X"
                    map[row - 1][col] = "^"
                    row = row - 1

            case "<":
                if col == 0:
                    break
                move_to = map[row][col - 1]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    map[row][col] = "X"
                    map[row][col - 1] = "<"
                    col = col - 1
            case ">":
                if col == len(map[0]) - 1:
                    break
                move_to = map[row][col + 1]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    map[row][col] = "X"
                    map[row][col + 1] = ">"
                    col = col + 1
            case "v":
                if row == len(map) - 1:
                    break
                move_to = map[row + 1][col]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    map[row][col] = "X"
                    map[row + 1][col] = "v"
                    row = row + 1
    map[row][col] = "X"
    total = 0
    for row in map:
        string = ""
        for element in row:
            string += element
            if element == "X":
                total += 1
        print(string)
    print(total)

#part 2
def main2():
    f = open("day6\input.txt")
    map = []
    for row in f:
        row = list(row)
        row.remove("\n")
        map.append(row)
    f.close()

    #find original path first, obstacle must be on one of the x's

    position = find_guard(map)
    og_row = position[0]
    og_col = position[1]
    og_map = copy.deepcopy(map)
    row = position[0]
    col = position[1]
    while True:
        match map[row][col]:
            case "^":
                if row == 0:
                    break
                move_to = map[row - 1][col]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    map[row][col] = "X"
                    map[row - 1][col] = "^"
                    row = row - 1

            case "<":
                if col == 0:
                    break
                move_to = map[row][col - 1]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    map[row][col] = "X"
                    map[row][col - 1] = "<"
                    col = col - 1
            case ">":
                if col == len(map[0]) - 1:
                    break
                move_to = map[row][col + 1]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    map[row][col] = "X"
                    map[row][col + 1] = ">"
                    col = col + 1
            case "v":
                if row == len(map) - 1:
                    break
                move_to = map[row + 1][col]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    map[row][col] = "X"
                    map[row + 1][col] = "v"
                    row = row + 1




    total = 0
    for r in range(0, len(map)):
        for c in range(0, len(map[0])):
            if map[r][c] == "X" and not (r == og_row and c == og_col):
                map_copy = copy.deepcopy(og_map)
                map_copy[r][c] = "#"
                if detect_loop(map_copy, r, c):
                    total += 1
    print(total)


def detect_loop(map, row, col):
    position = find_guard(map)
    row = position[0]
    col = position[1]
    looped = 0
    while True:
        if looped >= len(map) * 4:
            return True
        match map[row][col]:
            case "^":
                if row == 0:
                    break
                move_to = map[row - 1][col]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    if move_to == "X":
                        looped += 1
                    else:
                        looped = 0
                    map[row][col] = "X"
                    map[row - 1][col] = "^"
                    row = row - 1

            case "<":
                if col == 0:
                    break
                move_to = map[row][col - 1]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    if move_to == "X":
                        looped += 1
                    else:
                        looped = 0
                    map[row][col] = "X"
                    map[row][col - 1] = "<"
                    col = col - 1
            case ">":
                if col == len(map[0]) - 1:
                    break
                move_to = map[row][col + 1]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    if move_to == "X":
                        looped += 1
                    else:
                        looped = 0
                    map[row][col] = "X"
                    map[row][col + 1] = ">"
                    col = col + 1
            case "v":
                if row == len(map) - 1:
                    break
                move_to = map[row + 1][col]
                if move_to == "#":
                    turn_right(map, row, col)
                else:
                    if move_to == "X":
                        looped += 1
                    else:
                        looped = 0
                    map[row][col] = "X"
                    map[row + 1][col] = "v"
                    row = row + 1
    return False




 
def turn_right(map, row, col):
    orientations = ["^", ">", "v", "<"]
    index = orientations.index(map[row][col])
    index += 1
    index = index % 4
    map[row][col] = orientations[index]

def find_guard(map):
    r = -1
    c = -1
    for i in range(0, len(map)):
        if "^" in map[i] :
            r = i
            c = map[i].index("^")
            break
        if "<" in map[i]:
            r = i
            c = map[i].index("<")
            break
        if ">" in map[i]:
            r = i
            c = map[i].index(">")
            break
        if "v" in map[i]:
            r = i
            c = map[i].index("v")
            break
    return (r, c)

if input("part 1 or 2? ") == "1":
    main()
else:
    main2()