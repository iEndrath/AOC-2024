def main():
    f = open("day3\input.txt", "r")
    raw_input = f.read()
    f.close()

    MUL ="mul("
    DO = "do()"
    DONT = "don't()"

    i = 0
    do = 0
    dont = 0
    doing = True
    x = ""
    y = ""
    total = 0
    doing_x = True
    for char in raw_input:
        if char == "m":
            i = 1
            doing_x = True
            x = ""
            y = ""
            do = 0
            dont = 0
        elif char == "d":
            i = 0
            doing_x = True
            x = ""
            y = ""
            dont = 1
            do = 1
        elif i <= 3 and char == MUL[i] :
            do = 0
            dont = 0
            i += 1
        elif i > 3:
            do = 0
            dont = 0
            if doing_x and len(x) < 3:
                if char == ",":
                    doing_x = False
                else:
                    x += char
            elif doing_x and len(x) == 3:
                if char != ",":
                    i = 0
                    doing_x = True
                    x = ""
                    y = ""
                else:
                    doing_x = False
            elif not doing_x and len(y) < 3:
                if char == ")":
                    try:
                        if doing:
                            total += int(x) * int(y)
                        i = 0
                        doing_x = True
                        x = ""
                        y = ""
                    except:
                        i = 0
                        doing_x = True
                        x = ""
                        y = ""
                else:
                    y += char

            elif not doing_x and len(y) == 3:
                if char != ")":
                    i = 0
                    doing_x = True
                    x = ""
                    y = ""
                else:
                    try:
                        if doing:
                            total += int(x) * int(y)
                        i = 0
                        doing_x = True
                        x = ""
                        y = ""
                    except:
                        i = 0
                        doing_x = True
                        x = ""
                        y = ""
        elif do <= 1 and DO[do] == char:
            i = 0
            do += 1
            dont += 1
        elif do < len(DO) and DO[do] == char:
            i = 0
            do += 1
            dont = 0
            if do == len(DO):
                i = 0
                doing = True
                dont = 0
                do = 0
        elif dont < len(DONT) and DONT[dont] == char:
            dont += 1
            do = 0
            if dont == len(DONT):
                i = 0
                doing = False
                dont = 0 
                do = 0
        else:
            i = 0
            doing_x = True
            x = ""
            y = ""
            do = 0
            dont = 0
    print(total)


            


main()