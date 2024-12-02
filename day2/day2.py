def is_safe(report, choice):
    int_list = []
    for i in range(0, len(report)):
        int_list.append(int(report[i]))
    
    problem_dampener = False

    if choice == "2":
        problem_dampener = True

    #check ascending first
    for i in range(1, len(int_list)):
        x = int_list[i]
        y = int_list[i-1]
        d = abs(x - y)
        if (not (y < x and d <= 3 and d >= 1)) and problem_dampener:
            copy1 = report.copy()
            copy1.pop(i)
            copy2 = report.copy()
            copy2.pop(i-1)
            #if it's safe without either of the elements, then the report has been fixed, otherwise, continue
            if (is_safe(copy1, "1") or is_safe(copy2, "1")):
                return True
            else:
                break
        elif (not (x < y and d <= 3 and d >= 1)) and not problem_dampener:
            break
        elif i == len(int_list) -1:
            return True
        
    #check decending 
    for i in range(1, len(int_list)):
        x = int_list[i]
        y = int_list[i-1]
        d = abs(x - y)
        if (not (y > x and d <= 3 and d >= 1)) and problem_dampener:
            copy1 = report.copy()
            copy1.pop(i)
            copy2 = report.copy()
            copy2.pop(i-1)
            #if it's safe without either of the elements, then the report has been fixed, otherwise, continue
            if (is_safe(copy1, "1") or is_safe(copy2, "1")):
                return True
            else:
                break
        elif (not (x > y and d <= 3 and d >= 1)) and not problem_dampener:
            break
        elif i == len(int_list) -1:
            return True
    
    return False



def main(choice):
    f = open("day2\input.txt")
    reports = []
    for line in f:
        reports.append(line)
    
    amount_safe = 0
    for report in reports:
        report = report.split()
        if is_safe(report, choice):
            amount_safe +=1
    
    print(amount_safe)


choice = input("part 1 or 2? ")
main(choice)