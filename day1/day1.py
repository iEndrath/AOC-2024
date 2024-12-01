def append_numbers(line, left, right):
    left_number = line[0:5]
    right_number = line[8:13]
    left.append(int(left_number))
    right.append(int(right_number))
    return
    
def main(choice):
    #read and create left & right list
    f = open("day1\input.txt")
    left_list = []
    right_list = []
    for line in f:
        append_numbers(line, left_list, right_list)
    
    if choice == "1":
        total_distance = 0
        left_list.sort() 
        right_list.sort()

        for i in range(0, len(left_list)):
            total_distance += max(left_list[i], right_list[i]) - min(left_list[i], right_list[i])
        
        print(total_distance)
    else:
        similarity_score = 0
        for i in range(0, len(left_list)):
            total_appearances = 0
            for j in range(0, len(right_list)):
                if left_list[i] == right_list[j]:
                    total_appearances += 1
            similarity_score += left_list[i] * total_appearances
        print(similarity_score)

choice = input("part 1 or 2? ")
main(choice)
