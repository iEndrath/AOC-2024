def main(choice):
    f = open("day8\input.txt")
    map = []
    for line in f:
        map.append(list(line)[0:-1:])
        
    antennas = set()
    height = len(map)
    width = len(map[0])
    for row in range(0, height):
        for col in range(0, width):
            if map[row][col] != ".":
                antennas.add(map[row][col])
    
    all_antinodes = []
    for antenna in antennas:
        positions = []
        for row in range(0, height):
            for col in range(0, width):
                if map[row][col] == antenna:
                    positions.append((row, col))
        for position1 in positions:
            for position2 in positions:
                if position1 != position2:
                    dis_r = position2[0] - position1[0]
                    dis_c = position2[1] - position1[1]
                    anti_r = position2[0]
                    anti_c = position2[1] 
                    while anti_r in range(0, height) and anti_c in range(0, width):
                        anti_r += dis_r
                        anti_c += dis_c
                        if anti_r in range(0, height) and anti_c in range(0, width) and not ((anti_r, anti_c) in all_antinodes):
                            all_antinodes.append((anti_r, anti_c))
                        if choice == "1":
                            break
                        elif position1[0] in range(0, height) and position1[1] in range(0, width) and not ((position1[0], position1[1]) in all_antinodes):
                            all_antinodes.append((position1[0], position1[1]))

                    

    
    print(len(all_antinodes))

main(input("part 1 or 2? "))