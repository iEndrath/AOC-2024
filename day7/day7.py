
def main(choice):
    f = open("day7\input.txt")
    calibrations = []
    for line in f:
        calibration = []
        split_line = line.split(" ")
        calibration.append(int(split_line.pop(0)[0:-1:]))
        numbers = []
        for number in split_line:
            numbers.append(int(number))
        calibration.append(numbers)
        calibrations.append(calibration)

    total = 0
    for calibration in calibrations:
        if backtracking(calibration, choice):
            total += calibration[0]
    print(total)


def backtracking(solution, choice):
    examination = examine(solution)
    if examination == "accept":
        return True
    elif examination != "abort":
        for p in extend(solution, choice):
            if backtracking(p, choice):
                return True
        return False
    return False

def examine(solution):
    numbers = solution[1]
    if len(numbers) != 1:
        return "continue"
    else:
        if numbers[0] == solution[0]:
            return "accept"
        else:
            return "abort"

def extend(solution, choice):
    solutions = []
    numbers = solution[1]
    copy1 = numbers.copy()
    copy2 = numbers.copy()

    #*
    x = copy1.pop(0)
    y = copy1.pop(0)
    copy1.insert(0, x * y)

    #+
    x = copy2.pop(0)
    y = copy2.pop(0)
    copy2.insert(0, x + y)

    if choice == "2":
        copy3 = numbers.copy()
        x = copy3.pop(0)
        y = copy3.pop(0)
        concat = int(str(x) + str(y))
        copy3.insert(0, concat)
        solutions.append([solution[0], copy3])

    solutions.append([solution[0], copy1])
    solutions.append([solution[0], copy2])
    
    return solutions


main(input("part 1 or 2? "))