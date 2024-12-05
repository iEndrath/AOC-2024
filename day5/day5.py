def main(choice):
    #read input from file and parse it
    f = open("day5\input.txt")
    rules = []
    pages = []
    for line in f:
        if "|" in line:
            rule = line.split("|")
            for i in range(0, len(rule)):
                rule[i] = int(rule[i])
            rules.append(rule)
        elif line == "\n":
            True
        else:
            page = line.split(",")
            for i in range(0, len(page)):
                page[i] = int(page[i])
            pages.append(page)

    total = 0
    fix = True
    if choice == "1":
        fix = False
    for page in pages:
        if check_page(rules, page, fix):
            total += page[len(page) // 2]
        
    print(total)



def check_page(rules, page, fix):
    if fix:
        #part 2
        for rule in rules:
            x = rule[0]
            y = rule[1]
            fixed = False
            if x in page and y in page:
                x_index = page.index(x)
                y_index = page.index(y)
                if x_index > y_index:
                    fix_it(rules, page)
                    fixed = True
                    break
        return fixed
    else:
        #part 1
        for rule in rules:
            x = rule[0]
            y = rule[1]
            if x in page and y in page:
                x_index = page.index(x)
                y_index = page.index(y)
                if x_index > y_index:
                    return False
        return True

def fix_it(rules, page):
    for rule in rules:
        x = rule[0]
        y = rule[1]
        if x in page and y in page:
            x_index = page.index(x)
            y_index = page.index(y)
            if x_index > y_index:
                page[x_index], page[y_index] = page[y_index], page[x_index]
                fix_it(rules, page)
    return


main(input("part 1 or 2? "))