XMAS = "XMAS"

def main(choice):
    f = open("day4\input.txt")
    #puzzle will not change (immutable)
    puzzle = []
    for line in f:
        puzzle.append(line)

    total = 0

    rows = len(puzzle)
    columns = len(puzzle[0])
    if choice == "1":
        for row in range(0, rows):
            for col in range(0, columns):
                total += check_all(puzzle, row, col)
    else:
        for row in range(0, rows):
            for col in range(0, columns):
                total += check_cross(puzzle, row, col)
    print(total)
            
def check_all(puzzle, row, col):
    return check_horizontal(puzzle, row, col) + check_vertical(puzzle, row, col) + check_diagonal(puzzle, row, col)

def check_horizontal(puzzle, row, col):
    amount = 0
    if col >=3:
        attempt = ""
        for i in range(0, 4):
            attempt += puzzle[row][col - i]
        if XMAS == attempt:
            amount += 1
    if col <= len(puzzle[0]) - 4:
        attempt = ""
        for i in range(0, 4):
            attempt += puzzle[row][col + i]
        if XMAS == attempt:
            amount += 1
    return amount
            
def check_vertical(puzzle, row, col):
    amount = 0
    if row >= 3:
        attempt = ""
        for i in range(0, 4):
            attempt += puzzle[row - i][col]
        if XMAS == attempt:
            amount += 1
    if row <= len(puzzle) - 4:
        attempt = ""
        for i in range(0, 4):
            attempt += puzzle[row + i][col]
        if XMAS == attempt:
            amount += 1
    return amount

def check_diagonal(puzzle, row, col):
    amount = 0
    if row >= 3 and col >= 3:
        attempt = ""
        for i in range(0, 4):
            attempt += puzzle[row - i][col - i]
        if XMAS == attempt:
            amount += 1
    if row >= 3 and col <= len(puzzle[0]) - 4:
        attempt = ""
        for i in range(0, 4):
            attempt += puzzle[row - i][col + i]
        if XMAS == attempt:
            amount += 1
    if row <= len(puzzle) - 4 and col >= 3:
        attempt = ""
        for i in range(0, 4):
            attempt += puzzle[row + i][col - i]
        if XMAS == attempt:
            amount += 1
    if row <= len(puzzle) - 4 and col <= len(puzzle[0]) - 4:
        attempt = ""
        for i in range(0, 4):
            attempt += puzzle[row + i][col + i]
        if XMAS == attempt:
            amount += 1
    return amount
    
def check_cross(puzzle, row, col):
    if puzzle[row][col] == "A":
        if check_LR(puzzle, row, col) and check_RL(puzzle, row, col):
            return 1
    return 0

def check_LR(puzzle, row, col):
    if row in range(1, len(puzzle) - 1) and col in range(1, len(puzzle[0]) - 1):
        string = puzzle[row - 1][col - 1] + puzzle[row][col] + puzzle[row + 1][col + 1]
        if string == "MAS" or string[::-1] == "MAS":
            return True
    return False

def check_RL(puzzle, row, col):
    if row in range(1, len(puzzle) - 1) and col in range(1, len(puzzle[0]) - 1):
        string = puzzle[row + 1][col - 1] + puzzle[row][col] + puzzle[row - 1][col + 1]
        if string == "MAS" or string[::-1] == "MAS":
            return True
    return False

main(input("part 1 or 2?: "))